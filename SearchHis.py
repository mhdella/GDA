""" opens search history from google """
import json
import os
from datetime import datetime
import csv
import pandas
from collections import Counter

file_path = '/Users/MEHRA/Documents/Notebooks/Takeout 2/Searches/'
file_list = os.listdir(file_path)

# converting json file to list of dictionaries
def json_to_list(file_path, file_name):
        json_file = open(file_path + file_name)
        gdic_zero = json.load(json_file)
        json_file.close()
        gdic_one = gdic_zero['event']
        return gdic_one

# Combining all the files into one list
combined = []
for file in file_list:
     combined += json_to_list(file_path, file)

# Cleaning up the list
records = {}
ymonth = []
binset = set()
for i in range(len(combined)): #len(combined)):
    timestamp = combined[i]['query']['id'][0]['timestamp_usec'][:10]
    gooddate = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    shortdate =datetime.fromtimestamp(int(timestamp)).strftime('%Y') #-%m')
    ymonth.insert(i, shortdate)
    binset.add(shortdate)
    term = combined[i]['query']['query_text']
    records[gooddate] = term

bins = list(binset)

# Printing into csv file
#with open('SearchOutput.csv', 'w', newline='') as csvfile:
#    record_writer = csv.writer(csvfile, delimiter=',',
#                                quotechar = '"',
#                                quoting=csv.QUOTE_MINIMAL)
#    for rtime, rterm in records.items():
#        record_writer.writerow([rtime,rterm])

letter_counts = Counter(ymonth)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar',title ='Number of Searches per Year',legend=False)
