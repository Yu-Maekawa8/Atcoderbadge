import json
import requests

USERNAME = "Y_Maekawa"  # あなたのAtCoder ID

# AtCoder Problems API
url = f"https://kenkoooo.com/atcoder/atcoder-api/results?user=Y_Maekawa"
res = requests.get("https://kenkoooo.com/atcoder/#/table/Y_maekawa")
submissions = res.json()

# ユニークな問題IDでACされたものをカウント
ac_problems = {s['problem_id'] for s in submissions if s['result'] == 'AC'}

# バッジ形式に整形
badge = {
    "schemaVersion": 1,
    "label": "AC problems",
    "message": f"{len(ac_problems)} solved",
    "color": "brightgreen"
}

# JSONファイルに保存
with open("solved.json", "w") as f:
    json.dump(badge, f)
