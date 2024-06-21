import csv
import json

# Read CSV file
csv_file_path = 'wine_data.csv'
json_file_path = 'data.json'

data = []
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Write JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Print JSON object
print(json.dumps(data, indent=4))
