# Import JSON package and API requests Library
import json
import requests
import os
import time
import numpy as np
# Locate the file directory of this python file
# change the working directory to this location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# This is to print the total operation time
start_time = time.time()

i = 1
data = []
while i < 244:
    link = "https://theyvoteforyou.org.au/api/v1/policies/" + \
        str(i) + ".json?key=QNhXYGZ%2FWfCivHEXRVVj"
    response = requests.get(
        link)
    item_dict = response.json()
    data.append({
        'name': item_dict['name'],
        'number of division to pass': len(item_dict['policy_divisions']),
    })
    i = i + 1


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

# # This is to print the total operation time
print("--- %s seconds ---" % (time.time() - start_time))
