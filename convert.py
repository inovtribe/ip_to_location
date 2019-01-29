import requests
import json
import csv
import time

url = 'http://ip-api.com/json/'
resultMap = []

# Input
with open('test_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        resultRow = []
        for cell in row:
            cell = cell.replace(" ", "")
            time.sleep(0.5)
            r = requests.get(url + cell)
            data = json.loads(r.text)
            print("country:" + data["country"] + ", city:" + data["city"])
            map = {'country': data["country"], 'city': data["city"]}
            resultRow.append(map)
        resultMap.append(resultRow)

# Output
output_file = 'output.csv'
with open(output_file, mode='w') as f:
    for row in resultMap:
        for i in range(len(row)):
            cell = row[i]
            f.write(cell['country'].encode('utf-8'))
            f.write(',')
            f.write(cell['city'].encode('utf-8'))
            if (len(row) - 1 > i):
                f.write(',')
        f.write('\n')
