# Inning.py (野球ルール完全対応版)

from Player import Lineup
from Versus import VersusCard, Batter  # Batterクラスを直接使用


class Inning:
    """
    イニングの進行を管理し、野球の基本ルール（B/S/O、走塁、安打種別）に対応する。
    """

    def __init__(self, team_name, team_lineup, opponent_pitcher_name):
        self.team_name = team_name
        self.lineup = team_lineup
        self.opponent_pitcher_name = opponent_pitcher_name
        self.outs = 0
        self.runs = 0
        self.hits = 0
        self.errors = 0
        self.at_bat_records = []

        # 走者の状態を管理 (False: 塁上無し, True: 塁上あり)
        # 0: 本塁, 1: 一塁, 2: 二塁, 3: 三塁
        self.bases = [False, False, False]

    def _get_pitch_result_input(self):
        """一球ごとの入力を受け付ける。"""
        print("  Pitch: [B]all, [S]trike, [I]n Play (打球), [W]alk, [O]ut を入力: ")
        while True:
            pitch_result = input("  Input: ").strip().lower()
            if pitch_result in ['b', 's', 'i', 'w', 'o']:
                return pitch_result
            print("無効な入力です。B, S, I, W, O のいずれかを入力してください。")

    def _get_in_play_result_input(self):
        """打球の場合の最終結果（安打種別またはアウト）を受け付ける。"""
        while True:
            result = input("  In Play Result: [1]B, [2]B, [3]B, [H]R, [O]ut, [E]rror を入力: ").strip().lower()
            if result in ['1b', '2b', '3b', 'hr', 'o', 'e']:
                return result
            print("無効な入力です。1B, 2B, 3B, HR, O, E のいずれかを入力してください。")

    def _advance_runners(self, base_gain, is_walk=False, is_error=False):
        """
        走者を動かし、得点(runs)と安打(hits)/失策(errors)を更新する。
        :param base_gain: 進む塁数 (1 for 1B/Walk/Error, 2 for 2B, 3 for 3B, 4 for HR)
        """
        new_bases = [False, False, False]  # 次のイニングのための新しいベース状態
        score_this_play = 0

        # 本塁にいる走者（本塁、三塁、二塁、一塁の順に処理）
        for i in range(3, 0, -1):
            if self.bases[i - 1]:  # 塁上に走者がいる場合
                destination_base = i + base_gain

                if destination_base >= 4:
                    score_this_play += 1
                elif destination_base == 1:
                    new_bases[0] = True
                elif destination_base == 2:
                    new_bases[1] = True
                elif destination_base == 3:
                    new_bases[2] = True

        # 打者を塁上に置く
        if base_gain == 4:
            score_this_play += 1  # 打者自身も得点
        elif base_gain >= 1:
            new_bases[base_gain - 1] = True  # 打者を対応する塁に置く

        # 最終的な塁上の状態を更新
        self.bases = new_bases
        self.runs += score_this_play

        # 記録の更新
        if base_gain > 0 and not is_walk and not is_error:
            self.hits += 1
        elif is_error:
            self.errors += 1

        print(f"  --> 得点: {score_this_play} (合計: {self.runs})")
        print(f"  --> 現在の走者: {new_bases}")

    def _simulate_at_bat(self):
        """一打席のシミュレーションを実行する。"""
        current_batter_obj = self.lineup.get_current_batter()
        batter = Batter(current_batter_obj.name)  # カウント処理用のBatterオブジェクト

        print("\n--- New Batter ---")

        while batter.result is None and self.outs < 3:
            # カウント表示と対戦カード表示
            print(f"  Count: {batter.ball} Ball, {batter.strike} Strike. {self.outs} Out(s).")
            print(f"  Bases: 1B:{self.bases[0]} 2B:{self.bases[1]} 3B:{self.bases[2]}")
            card = VersusCard(self.opponent_pitcher_name, batter.name)
            card.display_card()

            pitch = self._get_pitch_result_input()

            base_gain = 0
            is_walk, is_error = False, False

            if pitch == 'b':
                batter.ball += 1
                if batter.ball == 4: batter.result = 'Walk'

            elif pitch == 's':
                batter.strike += 1
                if batter.strike == 3: batter.result = 'Out'  # StrikeOut

            elif pitch == 'w':
                batter.result = 'Walk'

            elif pitch == 'o':
                batter.result = 'Out'  # Out (犠牲フライやゴロなど)

            elif pitch == 'i':  # In Play (打球)
                result = self._get_in_play_result_input()

                if result == 'o':
                    batter.result = 'Out'
                elif result == 'e':
                    batter.result = 'Error'
                    is_error = True
                    base_gain = 1  # 打者は最低一塁へ
                else:  # 安打
                    batter.result = result.upper()
                    base_gain = int(result[0])

        if batter.result is not None:
            print(f"*** At Bat End: {batter.result} ***")

            # --- 打席結果の処理 ---
            if batter.result in ['Out', 'StrikeOut']:
                self.outs += 1
                # アウトカウントが加算されたことを記録
                self.at_bat_records.append({'batter': batter.name, 'result': batter.result})
                # 走塁は複雑なため、今回はアウトでは走者は動かない（将来の拡張点）

            elif batter.result == 'Walk':
                self._advance_runners(base_gain=1, is_walk=True)
                self.at_bat_records.append({'batter': batter.name, 'result': 'Walk'})

            elif batter.result.endswith('B') or batter.result == 'HR':
                # 安打種別に基づいて走者を進める
                if batter.result == 'HR':
                    base_gain = 4
                else:
                    base_gain = int(batter.result[0])
                self._advance_runners(base_gain=base_gain)
                self.at_bat_records.append({'batter': batter.name, 'result': batter.result})

            elif batter.result == 'Error':
                self._advance_runners(base_gain=1, is_error=True)
                self.at_bat_records.append({'batter': batter.name, 'result': 'Error'})

        if self.outs == 3:
            print("!!! Three Outs! Change of Sides! !!!")

    def get_half_inning_score(self, inning_num, half_inning):
        """
        イニングの表または裏のシミュレーションを実行し、R, H, Eを返す。
        """
        print(f"\n--- {inning_num}回{half_inning} --- ({self.team_name}の攻撃)")

        # イニング開始時のリセット
        self.outs = 0
        self.runs = 0
        self.hits = 0
        self.errors = 0
        self.at_bat_records = []
        self.bases = [False, False, False]  # 走者なし

        # 3アウトになるまで打席を続ける
        while self.outs < 3:
            self._simulate_at_bat()

        # R, H, E をGameScoreに渡す
        r = self.runs
        h = self.hits
        e = self.errors

        return r, h, e, self.at_bat_records
