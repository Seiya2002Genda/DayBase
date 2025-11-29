# Inning.py

class Inning:
    """
    イニングごとのスコア入力を処理するクラス。
    """
    def __init__(self, team_name):
        self.team_name = team_name

    def get_half_inning_score(self, inning_num, half_inning):
        """
        イニングの表または裏のスコア入力を受け付け、R, H, Eを返す。
        :param half_inning: '表' または '裏'
        :return: (r, h, e)
        """
        print(f"\n--- {inning_num}回{half_inning} --- ({self.team_name}の攻撃)")
        try:
            score_input = input(f"{inning_num}回{half_inning} (R,H,E) を入力してください（カンマ区切り、例: 1,2,0）: ")
            r, h, e = map(int, score_input.split(','))
            return r, h, e
        except (ValueError, IndexError):
            print("!! 無効な入力です。0,0,0とみなします。")
            return 0, 0, 0