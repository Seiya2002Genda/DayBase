# SaveCSV.py (Pandas不使用版)

import csv
import datetime
import os


class SaveCSV:
    """
    試合結果のデータを整形し、CSVファイルとして保存するクラス。
    （Python標準のcsvモジュールを使用）
    """

    def __init__(self, home_team, opponent_team):
        self.home_team = home_team
        self.opponent_team = opponent_team

    def save_results(self, score_data):
        """
        最終スコアデータを整形し、CSVとして保存する。
        """
        # 1. ヘッダーとデータをリストとして整形

        # ヘッダー行: チーム名に基づいて動的に生成
        away_team_run_col = f'{self.opponent_team}_R'
        home_team_run_col = f'{self.home_team}_R'
        header = ['Inning', away_team_run_col, home_team_run_col]

        # 2. 9イニングのスコア行を作成
        data_rows = []
        # スコアデータは0-8インデックスで保存されている
        away_runs = score_data['away_runs']
        home_runs = score_data['home_runs']

        for i in range(9):
            row = [
                i + 1,  # Inning
                away_runs[i],  # Away Runs
                home_runs[i]  # Home Runs
            ]
            data_rows.append(row)

        # 3. 合計スコア、安打(H)、失策(E)の行を作成

        # TOTAL行
        data_rows.append([
            'TOTAL',
            score_data['away_total_runs'],
            score_data['home_total_runs']
        ])

        # HITS行
        data_rows.append([
            'HITS',
            score_data['away_hits'],
            score_data['home_hits']
        ])

        # ERRORS行
        data_rows.append([
            'ERRORS',
            score_data['away_errors'],
            score_data['home_errors']
        ])

        # 4. ファイル名と保存
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'BaseballScore_{timestamp}.csv'

        try:
            # 'w' モードでファイルを開き、csv.writerで書き込む
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)

                # ヘッダーを書き込む
                writer.writerow(header)

                # スコアデータを書き込む
                writer.writerows(data_rows)

            print(f"\n✅ 試合結果を '{filename}' に保存しました。")

        except Exception as e:
            # ファイル書き込み失敗時のエラー処理
            print(f"\n❌ CSVファイルの保存中にエラーが発生しました: {e}")