# scripts/convert_csv_to_json.py

import csv
import json
import requests
import sys
from io import StringIO

# 外部CSVのURL（例：政府統計ポータルなどのオープンデータ）
CSV_URL = "https://raw.githubusercontent.com/ejujonhyqo/jsonconv/refs/heads/main/coffee.csv"
OUTPUT_PATH = "data/data.json"

def fetch_csv(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def csv_to_json(csv_data):
    csv_file = StringIO(csv_data)
    reader = csv.DictReader(csv_file)
    return list(reader)

def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    try:
        csv_data = fetch_csv(CSV_URL)
        json_data = csv_to_json(csv_data)
        save_json(json_data, OUTPUT_PATH)
        print("JSON conversion completed.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
