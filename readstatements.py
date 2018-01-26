import csv
import pandas as pd
import os
import glob

df = pd.DataFrame(columns=['Txn Date', 'Value Date', 'Description', 'Ref No', 'Debit', 'Credit', 'Balance'])
'''
directory = "/home/deepak/py/farm/source/sbi/"
for file in os.listdir(directory):
    if file.endswith(".csv"):
        with open('farmSbiConsolidated.csv', 'a') as g:
            with open(os.path.join(directory, file), 'r') as f:
                reader = csv.reader(f)
                rawdata = []
                rawdata = list(reader)
                endrow = len(rawdata) - 2
                rawdata = rawdata[20:endrow]
                rawdata_df = pd.DataFrame(rawdata)
                rawdata_df.to_csv(g, header=False)
            f.close()
        g.close()
'''
farmConsolidated = pd.read_csv('farmSbiConsolidated.csv', header=None, names=['Txn Date', 'Value Date', 'Description', 'Ref No', 'Debit', 'Credit', 'Balance'])
farmConsolidated.to_csv('consolidatedWithHeaders.csv')
#print(df[0])