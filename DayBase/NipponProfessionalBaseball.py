# NipponProfessionalBaseball.py

class NPBScoreboard:
    """
    スコアボードの表示整形と勝敗判定を行うクラス。
    """

    def __init__(self, home_team, opponent_team):
        self.home_team = home_team
        self.opponent_team = opponent_team
        # チーム名カラム幅を25に固定し、桁揃えを実現
        self.TEAM_COL_WIDTH = 25

    def display_scoreboard(self, inning_num, score_data):
        """
        現在のスコアボードを表示する。
        """
        # 3-1. ヘッダーの整形 (各イニング番号を2桁で右寄せ)
        runs_header = "".join(f"{i:2}" for i in range(1, 10))
        rhe_header = " R H E"

        # 3-2. スコアの文字列整形 (各スコアを2桁で右寄せ)
        home_runs_str = "".join(f"{r:2}" for r in score_data["home_runs"])
        away_runs_str = "".join(f"{r:2}" for r in score_data["away_runs"])

        # 3-3. スコアボードの出力 (アウェイチームを上に、ホームチームを下に配置)
        output = (f"\n========== {inning_num}回終了時のスコアボード ==========\n"
                  # ヘッダー行: チーム名のカラム幅(25)を空けて、イニングヘッダーと RHE ヘッダーを表示
                  f"VS{'-' * (self.TEAM_COL_WIDTH - 2)} {runs_header} |{rhe_header}\n"

                  # アウェイチーム（ビジター）の表示 (上段)
                  f"{self.opponent_team:<{self.TEAM_COL_WIDTH}} {away_runs_str} | {score_data['away_total_runs']:2} {score_data['away_hits']:2} {score_data['away_errors']:2}\n"

                  # ホームチームの表示 (下段)
                  f"{self.home_team:<{self.TEAM_COL_WIDTH}} {home_runs_str} | {score_data['home_total_runs']:2} {score_data['home_hits']:2} {score_data['home_errors']:2}\n")

        # 3-4. 勝敗判定（リード状況）
        if score_data['home_total_runs'] > score_data['away_total_runs']:
            output += "Home Team Leads!"
        elif score_data['home_total_runs'] < score_data['away_total_runs']:
            output += "Opponent Team Leads!"
        else:
            output += "Tie Score!"

        print(output)

    def display_final_result(self, score_data):
        """
        最終結果を表示する。
        """
        home_runs = score_data['home_total_runs']
        away_runs = score_data['away_total_runs']

        print("\n" + "=" * 55)
        print("========== 最終結果 ==========")
        if home_runs > away_runs:
            print(f"{self.home_team}の勝利！ ({home_runs} - {away_runs})")
        elif home_runs < away_runs:
            print(f"{self.opponent_team}の勝利！ ({away_runs} - {home_runs})")
        else:
            print(f"引き分け！ ({home_runs} - {away_runs})")
        print("=" * 55)