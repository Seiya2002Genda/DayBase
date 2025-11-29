# main.py (最終修正版)

from SetVersus import SetVersus
from GameScore import GameScore
from Inning import Inning
from NipponProfessionalBaseball import NPBScoreboard
from SaveCSV import SaveCSV
from Player import Lineup


def main():
    print("--- NPB スコアボードシミュレータ ---")

    # 1. 対戦チームの設定
    versus = SetVersus()
    home_team, opponent_team = versus.set_teams()

    # 2. ラインナップの設定
    home_lineup = Lineup(home_team)
    home_lineup.set_starting_lineup()

    away_lineup = Lineup(opponent_team)
    away_lineup.set_starting_lineup()

    # 3. 投手の設定
    print("\n--- 先発投手の設定 ---")
    # アウェイチームの先発投手 (ホームチームが守備)
    home_pitcher = input(f"  {home_team}の先発投手名: ").strip()
    if not home_pitcher: home_pitcher = "Home Pitcher"

    # ホームチームの先発投手 (アウェイチームが守備)
    away_pitcher = input(f"  {opponent_team}の先発投手名: ").strip()
    if not away_pitcher: away_pitcher = "Away Pitcher"

    print(f"✅ 設定完了: {home_team} ({home_pitcher}) vs {opponent_team} ({away_pitcher})")

    # 4. ゲームスコア、スコアボード、CSVセーバーの初期化
    game_score = GameScore(home_team, opponent_team)
    scoreboard = NPBScoreboard(home_team, opponent_team)
    csv_saver = SaveCSV(home_team, opponent_team)

    # 5. 9イニングのシミュレーション
    for inning in range(1, 10):
        # 5-1. 表 (アウェイチームの攻撃) -> ホーム投手 (home_pitcher) が投げる
        away_inning = Inning(opponent_team, away_lineup, home_pitcher)
        # R, H, E は Inning.py の内部シミュレーションによって確定する
        r, h, e, records = away_inning.get_half_inning_score(inning, '表')
        game_score.record_inning_score(inning, is_home_team=False, r=r, h=h, e=e, at_bat_records=records)

        # 5-2. 裏 (ホームチームの攻撃) -> アウェイ投手 (away_pitcher) が投げる
        home_inning = Inning(home_team, home_lineup, away_pitcher)
        # R, H, E は Inning.py の内部シミュレーションによって確定する
        r, h, e, records = home_inning.get_half_inning_score(inning, '裏')
        game_score.record_inning_score(inning, is_home_team=True, r=r, h=h, e=e, at_bat_records=records)

        # 5-3. スコアボードの表示
        scoreboard.display_scoreboard(inning, game_score.get_score_data())

    # 6. 最終結果の表示とCSV保存
    final_data = game_score.get_score_data()
    scoreboard.display_final_result(final_data)

    # 7. 打席結果の履歴を表示
    game_score.display_at_bat_history()

    # 8. CSVファイルへの保存
    csv_saver.save_results(final_data)


if __name__ == '__main__':
    main()