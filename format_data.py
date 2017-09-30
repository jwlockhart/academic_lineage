import pandas as pd
import numpy as np
import json
import sys

#titlecase disabled here only because it is not commonly installed
#from titlecase import titlecase

#csv files with information about people and the links between them
#edit the example files with your data (e.g. in excel) and save them as `.csv`
people_file = 'people.csv'
links_file = 'links.csv'

#read in data
print('Reading in data from', people_file , 'and', links_file, '...')
people = pd.read_csv(people_file)
links = pd.read_csv(links_file)

'''
#fixes dissertation titles to have title case. Library limited to english NYT style guide.
def titles(t):
    s = ''
    try:
        if not np.isnan(t):
            s = titlecase(t)
    except: 
        s = titlecase(t)
    return s

people['dissertation_title'] = people.dissertation_title.apply(titles)
'''

#hackish solution to data type issues
def other_string(t):
    s = ''
    try:
        if not np.isnan(t):
            s = str(t)
    except: 
        s = str(t)
    return s

#creates the text for when users hover over people.
def desc(r):
    text = ''
    text += r['name']
    text += '\nGraduated in ' + other_string(r.year_graduated)
    text += '\nfrom ' + other_string(r.university)
    text += '\nField: ' + other_string(r.department)
    text += '\nDissertation: ' + other_string(r.dissertation_title)
    
    return text

people['description'] = people.apply(desc, axis=1)

#convert the cleaned up data to json format
tmp = json.dumps({'nodes': people.to_dict(orient='records'), 
            'links': links.to_dict(orient='records')}).replace('NaN', '\"Unknown\"')

#save the json file
with open('data.json', 'wt') as f:
    f.write(tmp)

print('Done formatting data!')