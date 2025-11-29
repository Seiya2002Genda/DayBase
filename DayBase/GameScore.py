# GameScore.py

class GameScore:
    """
    試合全体のスコア（R, H, E）を管理するクラス。
    """

    def __init__(self, home_team, opponent_team):
        self.home_team = home_team
        self.opponent_team = opponent_team

        # 9イニング分の得点(R)を記録するリスト
        self.home_runs = [0] * 9
        self.away_runs = [0] * 9

        # H (安打)と E (失策)のトータルを記録する変数
        self.home_hits = 0
        self.home_errors = 0
        self.away_hits = 0
        self.away_errors = 0

        # 累計得点 (R) を保持する変数
        self.home_total_runs = 0
        self.away_total_runs = 0

    def record_inning_score(self, inning_num, is_home_team, r, h, e):
        """
        指定されたイニングのスコアを記録し、累計を更新する。
        :param inning_num: 1-9のイニング番号
        :param is_home_team: Trueならホームチーム、Falseならアウェイチームのスコア
        """
        inning_index = inning_num - 1

        if is_home_team:
            self.home_runs[inning_index] = r
            self.home_total_runs += r
            self.home_hits += h
            self.home_errors += e
        else:
            self.away_runs[inning_index] = r
            self.away_total_runs += r
            self.away_hits += h
            self.away_errors += e

    def get_score_data(self):
        """スコアボード表示に必要なデータを辞書として返す。"""
        return {
            "home_runs": self.home_runs,
            "away_runs": self.away_runs,
            "home_total_runs": self.home_total_runs,
            "away_total_runs": self.away_total_runs,
            "home_hits": self.home_hits,
            "away_hits": self.away_hits,
            "home_errors": self.home_errors,
            "away_errors": self.away_errors,
        }