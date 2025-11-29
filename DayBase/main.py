# main.py (修正版)

from SetVersus import SetVersus
from GameScore import GameScore
from Inning import Inning
from NipponProfessionalBaseball import NPBScoreboard
from SaveCSV import SaveCSV


def main():
    """
    試合の進行ロジック。
    """

    # 1. 対戦チームの設定
    versus = SetVersus()
    home_team, opponent_team = versus.set_teams()

    print(f"\n--- Game Start ---")
    print(f"Home: {home_team}")
    print(f"Away: {opponent_team}")

    # 2. ゲームスコアとスコアボードオブジェクトの初期化
    game_score = GameScore(home_team, opponent_team)
    scoreboard = NPBScoreboard(home_team, opponent_team)
    csv_saver = SaveCSV(home_team, opponent_team)  # SaveCSVオブジェクトを初期化

    # 3. 9イニングのシミュレーション
    for inning in range(9):
        inning_num = inning + 1

        # 3-1. 1回表 (アウェイチームの攻撃)
        away_inning = Inning(opponent_team)
        r, h, e = away_inning.get_half_inning_score(inning_num, '表')
        game_score.record_inning_score(inning_num, is_home_team=False, r=r, h=h, e=e)

        # 3-2. 1回裏 (ホームチームの攻撃)
        home_inning = Inning(home_team)
        r, h, e = home_inning.get_half_inning_score(inning_num, '裏')
        game_score.record_inning_score(inning_num, is_home_team=True, r=r, h=h, e=e)

        # 3-3. スコアボードの表示
        scoreboard.display_scoreboard(inning_num, game_score.get_score_data())

    # 4. 最終結果の表示
    final_data = game_score.get_score_data()
    scoreboard.display_final_result(final_data)

    # 5. CSVファイルへの保存 (NEW!)
    csv_saver.save_results(final_data)


if __name__ == "__main__":
    # Pandasライブラリが必要なため、実行環境にインストールされている必要があります。
    try:
        main()
    except ImportError:
        print("\n[エラー]: 必要なライブラリ (Pandas) が見つかりません。")
        print("Pandasをインストールしてください: pip install pandas")