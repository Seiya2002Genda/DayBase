
global Home_team, opponent_team
global central_league, pacific_league

# Regular Season
# Choice League
NPB = input("Central League or Pacific League?: \n"
            "1. Central League\n"
            "2. Pacific League\n"
            "Choice: ")

# Central League Section
if NPB == "Central League" or NPB == "1":
    central_league = ("\nHanshin Tigers\n"
                      "Yokohama DeNA Baystars\n"
                      "Yomiuri Giants\n"
                      "Hiroshima Toyo Carp\n"
                      "Tokyo Yakult Swallows\n"
                      "Chuunichi Dragons\n")

    Home_team = input(f"{central_league}"
                      f"Choose Home Team: ")
    opponent_team =  input(f"{central_league}"
                           f"Choose Away Team:")

# Pacific League Section
elif NPB == "Pacific League" or NPB == "2":
    pacific_league = ("\nSoftBank Hawks\n"
                      "Nippon-Ham Fighters\n"
                      "Orix Buffaloes\n"
                      "Tohoku Rakuten Eagles\n"
                      "Saitama Seibu Lions\n"
                      "Chiba Lotte Marines\n")

    Home_team = input(f"{pacific_league}"
                      f"Choose Home Team: ")
    opponent_team =  input(f"{pacific_league}"
                           f"Choose Away Team: ")

# Game Results
# 1. チーム名とスコア記録用リストの定義
# ユーザーの画像に合わせてチーム名を設定（必要に応じてここを変更してください）
Home_team = Home_team
opponent_team = opponent_team

# 9イニング分の得点(R)を記録するリスト
home_runs = [0] * 9
away_runs = [0] * 9

# H (安打)と E (失策)のトータルを記録する変数
home_hits = 0
home_errors = 0
away_hits = 0
away_errors = 0

# 累計得点 (R) を保持する変数
home_total_runs = 0
away_total_runs = 0

# --- ループの開始 (9イニング分実行) ---

for inning in range(9):
    inning_num = inning + 1

    # ---------------------------
    # 2. 1回表/裏の入力処理 (手入力)
    # ---------------------------

    # --- 2-1. 1回表 (アウェイチームの攻撃) の入力 ---
    # 連続で入力できるように、print文で区切りを明示
    print(f"\n--- {inning_num}回表 --- ({opponent_team}の攻撃)")
    try:
        # 入力は「得点,安打,失策」のようにカンマ区切りで受け取る
        score_input = input(f"{inning_num}回表 (R,H,E) を入力してください（カンマ区切り、例: 1,2,0）: ")
        # 入力を整数に変換し、R, H, E に割り当て
        r, h, e = map(int, score_input.split(','))
    except (ValueError, IndexError):
        print("!! 無効な入力です。0,0,0とみなします。")
        r, h, e = 0, 0, 0

    # スコアをリストに格納し、累計を更新
    away_runs[inning] = r
    away_total_runs += r
    away_hits += h
    away_errors += e

    # --- 2-2. 1回裏 (ホームチームの攻撃) の入力 ---
    print(f"\n--- {inning_num}回裏 --- ({Home_team}の攻撃)")
    try:
        score_input = input(f"{inning_num}回裏 (R,H,E) を入力してください（カンマ区切り、例: 0,1,0）: ")
        r, h, e = map(int, score_input.split(','))
    except (ValueError, IndexError):
        print("!! 無効な入力です。0,0,0とみなします。")
        r, h, e = 0, 0, 0

    # スコアをリストに格納し、累計を更新
    home_runs[inning] = r
    home_total_runs += r
    home_hits += h
    home_errors += e

    # ---------------------------
    # 3. スコアボードの表示 (桁揃えと配置修正済み)
    # ---------------------------

    # 3-1. ヘッダーの整形 (各イニング番号を2桁で右寄せ)
    runs_header = "".join(f"{i:2}" for i in range(1, 10))
    # R H E のヘッダー (各2桁幅を確保)
    rhe_header = " R H E"

    # 3-2. スコアの文字列整形 (各スコアを2桁で右寄せ)
    home_runs_str = "".join(f"{r:2}" for r in home_runs)
    away_runs_str = "".join(f"{r:2}" for r in away_runs)

    # 3-3. スコアボードの出力 (アウェイチームを上に、ホームチームを下に配置)
    # チーム名カラム幅を25に固定し、桁揃えを実現
    output = (f"\n========== {inning_num}回終了時のスコアボード ==========\n"
              # ヘッダー行: チーム名のカラム幅(25)を空けて、イニングヘッダーと RHE ヘッダーを表示
              f"VS{'-' * 23} {runs_header} |{rhe_header}\n"

              # アウェイチーム（ビジター）の表示 (上段)
              f"{opponent_team:<25} {away_runs_str} | {away_total_runs:2} {away_hits:2} {away_errors:2}\n"

              # ホームチームの表示 (下段)
              f"{Home_team:<25} {home_runs_str} | {home_total_runs:2} {home_hits:2} {home_errors:2}\n")

    # 3-4. 勝敗判定（リード状況）
    if home_total_runs > away_total_runs:
        output += "Home Team Leads!"
    elif home_total_runs < away_total_runs:
        output += "Opponent Team Leads!"
    else:
        output += "Tie Score!"

    print(output)

# ---------------------------
# 4. 最終結果の表示 (ループ終了後)
# ---------------------------

print("\n" + "=" * 55)
print("========== 最終結果 ==========")
if home_total_runs > away_total_runs:
    print(f"{Home_team}の勝利！ ({home_total_runs} - {away_total_runs})")
elif home_total_runs < away_total_runs:
    print(f"{opponent_team}の勝利！ ({away_total_runs} - {home_total_runs})")
else:
    # 9回終了時点で同点の場合
    print(f"引き分け！ ({home_total_runs} - {away_total_runs})")
print("=" * 55)