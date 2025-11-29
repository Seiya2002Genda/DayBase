# NipponProfessionalBaseball.py

class NPBDefinition:
    """NPBのリーグとチームの定義を保持する。"""

    CENTRAL_LEAGUE = {
        "1": "Hanshin Tigers", "2": "Yokohama DeNA Baystars", "3": "Yomiuri Giants",
        "4": "Hiroshima Toyo Carp", "5": "Tokyo Yakult Swallows", "6": "Chuunichi Dragons"
    }
    PACIFIC_LEAGUE = {
        "1": "SoftBank Hawks", "2": "Nippon-Ham Fighters", "3": "Orix Buffaloes",
        "4": "Tohoku Rakuten Eagles", "5": "Saitama Seibu Lions", "6": "Chiba Lotte Marines"
    }


class NPBScoreboard:
    """
    試合のスコアボードを表示するクラス。
    """

    def __init__(self, home_team, opponent_team):
        self.home_team = home_team
        self.opponent_team = opponent_team

    def display_scoreboard(self, current_inning, score_data):
        """現在のスコアボードを表示する。（画像 `image_b897f1.png` の形式）"""
        away_runs = score_data['away_runs']
        home_runs = score_data['home_runs']

        # R, H, Eの合計値を計算
        away_total_runs = score_data['away_total_runs']
        home_total_runs = score_data['home_total_runs']
        away_hits = score_data['away_hits']
        home_hits = score_data['home_hits']
        away_errors = score_data['away_errors']
        home_errors = score_data['home_errors']

        # スコアボードの表示
        print(f"\n======== {current_inning}回終了時のスコアボード ========")
        print(f"VS------------------ 1 2 3 4 5 6 7 8 9 | R H E")

        # アウェイチームの行
        away_score_line = "".join(f"{r:2}" for r in away_runs)
        print(f"{self.opponent_team:<20}{away_score_line[:18]} | {away_total_runs:1} {away_hits:1} {away_errors:1}")

        # ホームチームの行
        home_score_line = "".join(f"{r:2}" for r in home_runs)
        print(f"{self.home_team:<20}{home_score_line[:18]} | {home_total_runs:1} {home_hits:1} {home_errors:1}")

        # 勝敗判定
        if home_total_runs > away_total_runs:
            print(f"{self.home_team} Leads!")
        elif home_total_runs < away_total_runs:
            print(f"{self.opponent_team} Leads!")
        else:
            print("Tie Score!")

    def display_final_result(self, score_data):
        """最終結果を表示する。（画像 `image_b8942e.png` の形式）"""
        home_total = score_data['home_total_runs']
        away_total = score_data['away_total_runs']

        print("\n================ 最終結果 ================")
        if home_total > away_total:
            print(f"{self.home_team}の勝利！ ({home_total} - {away_total})")
        elif home_total < away_total:
            print(f"{self.opponent_team}の勝利！ ({away_total} - {home_total})")
        else:
            print(f"引き分け ({home_total} - {away_total})")
        print("==========================================")