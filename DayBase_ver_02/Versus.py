# Versus.py

class Pitcher:
    """投手側の管理クラス"""

    def __init__(self, player_name):
        self.name = player_name


class Batter:
    """打者側の管理クラス（カウント管理機能を追加）"""

    def __init__(self, player_name):
        self.name = player_name
        self.ball = 0
        self.strike = 0
        self.result = None  # 打席結果: '1B', '2B', '3B', 'HR', 'Out', 'Walk'


class VersusCard:
    """一打席ごとの対戦カードとカウントを管理する。"""

    def __init__(self, pitcher_name, batter_name):
        self.pitcher = Pitcher(pitcher_name)
        self.batter = Batter(batter_name)
        # カウントはBatterオブジェクトに持たせるため、ここでは使わないが互換性のため残す
        self.ball = 0
        self.strike = 0
        self.at_bat_result = None

    def display_card(self):
        """現在の対戦カードを表示する。"""
        # カウントはBatterオブジェクトから取得し、Inning.pyで表示する
        print(f"\n  VS: {self.pitcher.name} vs {self.batter.name}")