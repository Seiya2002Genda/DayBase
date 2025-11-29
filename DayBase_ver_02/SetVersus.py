# SetVersus.py

from NipponProfessionalBaseball import NPBDefinition


class SetVersus:
    """対戦するホームチームとアウェイチームを設定するクラス。"""

    def __init__(self):
        self.home_team = ""
        self.opponent_team = ""
        self.central_league = NPBDefinition.CENTRAL_LEAGUE
        self.pacific_league = NPBDefinition.PACIFIC_LEAGUE

    def _get_league_choice(self):
        """リーグ選択の入力を受け付ける。"""

        print("\nCentral League or Pacific League?:")
        print("  1. Central League")
        print("  2. Pacific League")

        while True:
            NPB = input("Choice (1 or 2): ").strip()

            if NPB == "1":
                return "Central League", self.central_league
            elif NPB == "2":
                return "Pacific League", self.pacific_league
            else:
                print("無効な選択です。'1' または '2' を入力してください。")

    def _get_team_choice(self, league_name, league_teams):
        """リーグに基づきチームを選択する。"""
        teams_str = f"\n--- {league_name} Teams ---\n"
        for i, team in league_teams.items():
            teams_str += f"{i}. {team}\n"

        # ホームチーム選択
        while True:
            choice = input(f"{teams_str}Choose Home Team (Number): ")
            if choice in league_teams:
                self.home_team = league_teams[choice]
                break
            print("無効な選択です。再度入力してください。")

        # アウェイチーム選択
        while True:
            choice = input(f"{teams_str}Choose Away Team (Number): ")
            if choice in league_teams and league_teams[choice] != self.home_team:
                self.opponent_team = league_teams[choice]
                break
            elif choice in league_teams:
                print("ホームチームと同じです。別のチームを選択してください。")
            else:
                print("無効な選択です。再度入力してください。")

    def set_teams(self):
        """チーム設定を実行し、結果を返す。"""
        league_name, league_teams = self._get_league_choice()
        self._get_team_choice(league_name, league_teams)
        return self.home_team, self.opponent_team