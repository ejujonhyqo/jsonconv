import csv
import json
import requests
from pathlib import Path

# 外部CSVのURL（raw.githubusercontent.com のURLを記載）
CSV_URL = "https://raw.githubusercontent.com/ejujonhyqo/jsonconv/refs/heads/main/coffee.csv"

# 出力JSONのパス（リポジトリ内に保存）
JSON_FILE = Path("data/coffee_shops.json")

def csv_to_json():
    # CSVデータを取得
    response = requests.get(CSV_URL)
    response.raise_for_status()
    csv_text = response.text.splitlines()

    # CSVをパース
    reader = csv.DictReader(csv_text)
    data = [row for row in reader]

    # JSONに保存
    JSON_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(JSON_FILE, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    csv_to_json()
