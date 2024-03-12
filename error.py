import json
import csv
import re

json_file = "logs.json"
csv_file = "error_logs.csv"

with open(json_file,'r')as file:
    data = json.load(file)
    with open(csv_file,'w',newline='')as file2:
        writer = csv.writer(file2)
        writer.writerow(['timestamp', 'level', 'message'])
        for entry in data:
            pattern = "ERROR"
            print(entry["level"])
            print(re.search(pattern,entry["level"]))
            if re.search(pattern,entry["level"]):
                entry_data = [entry['timestamp'],"ERROR",entry['message']]
                writer.writerow(entry_data)