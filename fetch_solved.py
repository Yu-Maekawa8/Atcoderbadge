import requests

USERNAME = "Y_Maekawa"

url = f"https://kenkoooo.com/atcoder/atcoder-api/results?user={USERNAME}"

res = requests.get(url)

# ✅ ステータスコードとレスポンスの確認
if res.status_code != 200:
    print(f"Error: Failed to fetch data. Status code: {res.status_code}")
    exit(1)

try:
    submissions = res.json()
except Exception as e:
    print(f"Error parsing JSON: {e}")
    print("Response content:", res.text[:200])  # 念のため一部表示
    exit(1)

# ✅ 正常時の処理（例：AC数カウント）
ac_count = sum(1 for s in submissions if s["result"] == "AC")
print(f"Solved problems: {ac_count}")

# ↓ ファイル出力などの後続処理をここに
