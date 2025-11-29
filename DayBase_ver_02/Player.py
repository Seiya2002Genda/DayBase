# Player.py

class Player:
    """個々の選手を表現するクラス。"""

    def __init__(self, name):
        self.name = name
        self.at_bats = 0
        self.hits = 0


class Lineup:
    """チームのスターティングラインナップを管理し、打順を回すクラス。"""

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
        # 打席記録をGameScoreに渡すため、現在の打者を保持するインデックス
        self.current_batter_index = 0

    def set_starting_lineup(self):
        """ユーザーからラインナップを9人分入力させる。"""
        print(f"\n--- {self.team_name}のスターティングラインナップ入力 ---")
        self.players = []
        for i in range(1, 10):
            while True:
                player_name = input(f"  {i}番打者: ")
                if player_name.strip():
                    self.players.append(Player(player_name))
                    break
                print("名前を入力してください。")
        print(f"✅ {self.team_name}のラインナップが設定されました。")

    def get_current_batter(self):
        """現在の打者を返す。打順を自動的に一つ進める。"""
        batter = self.players[self.current_batter_index]
        self.current_batter_index = (self.current_batter_index + 1) % 9
        return batter