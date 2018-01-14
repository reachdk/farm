import csv
#import pandas as pd
import os
import glob

rawdata1 = []
directory = "/home/deepak/py/farm/source/sbi/"
for file in os.listdir(directory):
    if file.endswith(".csv"):
        with open(os.path.join(directory, file), 'r') as f:
            reader = csv.reader(f)
            rawdata = list(reader)
            endrow = len(rawdata) - 2
            rawdata1 = rawdata[20:endrow]
            #rawdata2 = rawdata1.extend(rawdata)
        f.close()
print(rawdata1)
'''
with open('source/5808JanDec2017.csv', 'r') as f:
    reader = csv.reader(f)
    data5808 = list(reader)

with open('source/7494JanDec2017.csv', 'r') as f:
    reader = csv.reader(f)
    data7494 = list(reader)

with open('source/7494JanDec2017.csv', 'r') as f:
    reader = csv.reader(f)
    data7494 = list(reader)

with open('source/7494JanDec2017.csv', 'r') as f:
    reader = csv.reader(f)
    data7494 = list(reader)

with open('source/7494JanDec2017.csv', 'r') as f:
    reader = csv.reader(f)
    data7494 = list(reader)

with open('source/7494JanDec2017.csv', 'r') as f:
    reader = csv.reader(f)
    data7494 = list(reader)
'''