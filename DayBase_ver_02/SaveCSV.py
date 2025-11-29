# SaveCSV.py

import csv
import datetime


class SaveCSV:
    """試合結果のデータを整形し、CSVファイルとして保存するクラス。"""

    def __init__(self, home_team, opponent_team):
        self.home_team = home_team
        self.opponent_team = opponent_team

    def save_results(self, score_data):
        """最終スコアデータを整形し、CSVとして保存する。"""

        away_team_run_col = f'{self.opponent_team}_R'
        home_team_run_col = f'{self.home_team}_R'

        # 1. ヘッダーとデータをリストとして整形
        header = ['Inning', away_team_run_col, home_team_run_col]
        data_rows = []

        away_runs = score_data['away_runs']
        home_runs = score_data['home_runs']

        # 9イニングのスコア行を作成
        for i in range(9):
            row = [i + 1, away_runs[i], home_runs[i]]
            data_rows.append(row)

        # 合計スコア、安打(H)、失策(E)の行を作成
        data_rows.append(['TOTAL', score_data['away_total_runs'], score_data['home_total_runs']])
        data_rows.append(['HITS', score_data['away_hits'], score_data['home_hits']])
        data_rows.append(['ERRORS', score_data['away_errors'], score_data['home_errors']])

        # 2. ファイル名と保存
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'BaseballScore_{timestamp}.csv'

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(data_rows)

            print(f"\n✅ 試合結果を '{filename}' に保存しました。")

        except Exception as e:
            print(f"\n❌ CSVファイルの保存中にエラーが発生しました: {e}")