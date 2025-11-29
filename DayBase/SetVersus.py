# SetVersus.py

class SetVersus:
    """
    NPBのリーグを選択し、対戦するホームチームとアウェイチームを設定するクラス。
    """

    def __init__(self):
        self.home_team = ""
        self.opponent_team = ""
        self.central_league = {
            "1": "Hanshin Tigers", "2": "Yokohama DeNA Baystars", "3": "Yomiuri Giants",
            "4": "Hiroshima Toyo Carp", "5": "Tokyo Yakult Swallows", "6": "Chuunichi Dragons"
        }
        self.pacific_league = {
            "1": "SoftBank Hawks", "2": "Nippon-Ham Fighters", "3": "Orix Buffaloes",
            "4": "Tohoku Rakuten Eagles", "5": "Saitama Seibu Lions", "6": "Chiba Lotte Marines"
        }

    def _get_league_choice(self):
        """リーグ選択の入力を受け付ける。"""
        NPB = input("Central League or Pacific League?: \n"
                    "1. Central League\n"
                    "2. Pacific League\n"
                    "Choice: ")

        if NPB in ["1", "Central League"]:
            return "Central League", self.central_league
        elif NPB in ["2", "Pacific League"]:
            return "Pacific League", self.pacific_league
        else:
            print("無効な選択です。デフォルトでセントラルリーグを選択します。")
            return "Central League", self.central_league

    def _get_team_choice(self, league_name, league_teams):
        """リーグに基づきチームを選択する。"""
        teams_str = f"\n--- {league_name} Teams ---\n"
        for i, team in league_teams.items():
            teams_str += f"{i}. {team}\n"

        while True:
            choice = input(f"{teams_str}Choose Home Team (Number): ")
            if choice in league_teams:
                self.home_team = league_teams[choice]
                break
            print("無効な選択です。再度入力してください。")

        while True:
            choice = input(f"{teams_str}Choose Away Team (Number): ")
            if choice in league_teams and league_teams[choice] != self.home_team:
                self.opponent_team = league_teams[choice]
                break
            elif league_teams[choice] == self.home_team:
                print("ホームチームと同じです。別のチームを選択してください。")
            else:
                print("無効な選択です。再度入力してください。")

    def set_teams(self):
        """チーム設定を実行し、結果を返す。"""
        league_name, league_teams = self._get_league_choice()
        self._get_team_choice(league_name, league_teams)
        return self.home_team, self.opponent_team