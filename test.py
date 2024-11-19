import csv
from collections import defaultdict
from openpyxl import Workbook

# Initialize dictionaries to store sums for each feature
sums = defaultdict(lambda: defaultdict(int))

# Read the CSV data
csv_data = '''sender,time,success,fail,expire,block,process
24PREMIUM,2024-09-2106:27:41,9087,303,1295,0,5
24PREMIUM,2024-09-2106:28:33,6977,55,965,0,3
24PREMIUM,2024-09-2119:12:22,7398,336,1491,0,5
24PREMIUM,2024-09-2119:13:19,5796,288,912,0,4
24PREMIUM,2024-09-2119:13:20,2472,98,403,0,3
24PREMIUM,2024-09-2119:16:37,7840,467,1682,0,8
24PREMIUM,2024-09-2119:16:41,837,13,150,0,0
24PREMIUM,2024-09-2119:16:44,1718,35,246,0,1
24PREMIUM,2024-09-2119:16:45,829,24,147,0,0
24PREMIUM,2024-09-2119:16:47,860,16,124,0,0
24PREMIUM,2024-09-2119:16:49,4932,197,869,0,2
24PREMIUM,2024-09-2119:16:51,880,5,114,0,1
24PREMIUM,2024-09-2119:16:53,877,9,114,0,0
24PREMIUM,2024-09-2119:16:55,2620,16,360,0,4
24PREMIUM,2024-09-2119:16:57,888,6,96,0,0
24PREMIUM,2024-09-2119:17:20,4880,269,837,0,5
24PREMIUM,2024-09-2119:17:21,3257,173,567,0,3
24PREMIUM,2024-09-2119:17:41,8403,241,1326,0,12
24PREMIUM,2024-09-2119:26:41,18223,641,3125,0,11
24PREMIUM,2024-09-2119:26:42,4211,92,694,0,3
24PREMIUM,2024-09-2119:26:43,7803,106,1087,0,4
24PREMIUM,2024-09-2106:27:41,8396,275,1329,0,0
24PREMIUM,2024-09-2106:28:33,7547,53,929,0,0
24PREMIUM,2024-09-2119:12:22,7883,454,1663,0,0
24PREMIUM,2024-09-2119:13:19,8144,465,1391,0,0
24PREMIUM,2024-09-2119:16:37,7981,422,1597,0,0
24PREMIUM,2024-09-2119:16:44,2498,67,435,0,0
24PREMIUM,2024-09-2119:16:45,862,14,124,0,0
24PREMIUM,2024-09-2119:16:47,816,33,151,0,0
24PREMIUM,2024-09-2119:16:49,4152,131,717,0,0
24PREMIUM,2024-09-2119:16:51,1754,14,232,0,0
24PREMIUM,2024-09-2119:16:53,871,2,127,0,0
24PREMIUM,2024-09-2119:16:55,2625,21,354,0,0
24PREMIUM,2024-09-2119:17:20,8172,442,1386,0,0
24PREMIUM,2024-09-2119:17:41,8443,194,1363,0,0
24PREMIUM,2024-09-2119:26:41,18954,667,3360,0,0
24PREMIUM,2024-09-2119:26:42,3386,82,532,0,0
24PREMIUM,2024-09-2119:26:43,9521,104,1239,0,0'''

# Process the CSV data
reader = csv.DictReader(csv_data.splitlines())
for row in reader:
    time = row['time']
    for feature in ['success', 'fail', 'expire', 'block', 'process']:
        sums[time][feature] += int(row[feature])

# Calculate the total sum for each feature
total_sums = defaultdict(int)
for features in sums.values():
    for feature, value in features.items():
        total_sums[feature] += value

# Create a new workbook and select the active sheet
wb = Workbook()
ws = wb.active
ws.title = "Feature Sums by Time"

# Write headers
headers = ['Time', 'Success', 'Fail', 'Expire', 'Block', 'Process']
ws.append(headers)

# Write data for each time
for time, features in sums.items():
    row = [time]
    for feature in headers[1:]:
        row.append(features[feature.lower()])
    ws.append(row)

# Add a blank row
ws.append([])

# Write total sums
total_row = ['Total']
for feature in headers[1:]:
    total_row.append(total_sums[feature.lower()])
ws.append(total_row)

# Save the workbook
wb.save("feature_sums_by_time.xlsx")

print("Excel file 'feature_sums_by_time.xlsx' has been created with the results.")