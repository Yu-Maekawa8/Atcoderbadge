# count_solved.py
import requests
import json

USERNAME = "Y_Maekawa"  # ← あなたのAtCoderユーザー名

# APIから解答データ取得
url = f"https://kenkoooo.com/atcoder/atcoder-api/results?user={USERNAME}"
response = requests.get(url)
data = response.json()

# ACの一意問題数をカウント
solved = set([d["problem_id"] for d in data if d["result"] == "AC"])

# Shields.io 用 JSON を生成
badge = {
    "schemaVersion": 1,
    "label": "AC problems",
    "message": str(len(solved)),
    "color": "brightgreen"
}

# ファイルに保存
with open("solved.json", "w") as f:
    json.dump(badge, f)
