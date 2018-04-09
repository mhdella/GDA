""" opens search history from google """
import json
import os
from datetime import datetime

file_path = '/Users/MEHRA/Documents/Notebooks/Takeout 2/Searches/'
file_list = os.listdir(file_path)

# converting json file to list of dictionaries
def json_to_list(file_path, file_name):
        json_file = open(file_path + file_name)
        gdic_zero = json.load(json_file)
        json_file.close()
        gdic_one = gdic_zero['event']
        print(len(gdic_one))
        return gdic_one

# combined = []
# for file in file_list:
#     combined += json_to_list(file_path, file)
combined = json_to_list(file_path,file_list[0])

timestamp = combined[0]['query']['id'][0]['timestamp_usec'][:13]
# web:  1475146082971
# inja: 1372549834804729
print(timestamp)
# gooddate = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
# print(gooddate)
print(combined[0]['query']['query_text'])
