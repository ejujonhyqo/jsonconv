import csv
import json
import requests

# まとめたい CSV の URL リスト
csv_urls = [
    "https://raw.githubusercontent.com/ejujonhyqo/jsonconv/refs/heads/main/coffee.csv",
    "https://raw.githubusercontent.com/ejujonhyqo/jsonconv/refs/heads/main/coffee.csv",
]

output_data = []

for url in csv_urls:
    print(f"Fetching {url} ...")
    r = requests.get(url)
    r.raise_for_status()

    lines = r.text.splitlines()
    reader = csv.DictReader(lines)
    for row in reader:
        output_data.append(row)

# JSON として保存（フラットなリスト）
with open("data/coffee_shops.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)
