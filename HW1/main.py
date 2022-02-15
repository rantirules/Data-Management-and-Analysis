import csv
from datetime import datetime
import xmltodict
import json
import xml.etree.ElementTree as ET

# CSV QUESTION 1
data = open('covid.csv', 'r')
reader = csv.reader(data)
header = next(reader) # skip the header row

current_country = ""
for line in data:
    country = line.split(",")[1] # where country is stored
    date = line.split(",")[0] # where the date is stored
    new_cases = line.split(",")[2] # where new cases is stored
    if new_cases == '': # if the cell is empty replace it with '0'
        new_cases = '0'
    elif current_country != country and int(new_cases) > 0:
        print(f"{country} {date}")
        current_country = country

data.close() 
# CSV QUESTION 2
# dictionary of dictionaries of each dates
data = open('covid.csv', 'r')
reader = csv.reader(data)
header = next(reader) # skip the header row
dates = {}
for line in data:
    date = line.split(",")[0] # where the date is stored
    country = line.split(",")[1] # where country is stored
    new_cases = line.split(",")[2] # where new cases is stored
    if new_cases == '': # if the cell is empty replace it with '0'
        new_cases = '0'
    if date not in dates: # only add the dates into the dictionary if it is not present
        dates[date] = {}
        dates[date][country] = int(new_cases)
    else:
        dates[date][country] = int(new_cases)    
# print(dates['2020-02-25'])
dates = dict(sorted(dates.items(), key = lambda x:datetime.strptime(x[0], '%Y-%m-%d')))
dates_new_cases_average = {}
keys = list(dates.keys())
for i, (key,value) in enumerate(dates.items()):
    dates_new_cases_average[key] = 0
    cases_date = []
    if i > 7:
        for j in range(i - 7, i):
            cases_date_country = []
            for country, new_case in dates[keys[j]].items():
                cases_date_country.append(new_case)
            #print(cases_date_country)
            cases_date.append(sum(cases_date_country)/len(cases_date_country))
        dates_new_cases_average[key] = sum(cases_date)/len(cases_date)
    elif i>0 and i<7:
        for j in range(0, i):
            cases_date_country = []
            for country, new_case in dates[keys[j]].items():
                cases_date_country.append(new_case)
            #print(cases_date_country)
            cases_date.append(sum(cases_date_country)/len(cases_date_country))
        dates_new_cases_average[key] = sum(cases_date)/len(cases_date)
    
print(dates_new_cases_average)

# CSV QUESTION 3
keys = list(dates_new_cases_average.keys())
peaks = []
for i, (key, value) in enumerate(dates_new_cases_average.items()):
    if i>0:
        if dates_new_cases_average[keys[i-1]] < value and dates_new_cases_average[keys[i+1]] < value:
            peaks.append(key)
    
print(peaks)


# XML QUESTION 1
with open('station.xml', 'r') as f:
    my_xml = f.read()
    
with open('stationEmail.json', 'w') as f:
    json.dump(xmltodict.parse(my_xml), f)

# XML QUESTION 2)
with open("stationEmail.json", "r") as json_file:
    data = json.load(json_file);
    #print(data)
    root = ET.Element("xml-tables")
    TStable = ET.SubElement(root, "Train_Stations-table")
    stations = data['xml-tables']['Train_Stations-table']['Train_Stations']
    for i in range(len(stations)):
        TS = ET.SubElement(TStable, "Train_Stations")
        for key, value in stations[i].items():
            if key!="Email":
                ET.SubElement(TS, key).text = value
     
    tree = ET.ElementTree(root)
   
    # Writing the xml to output file
    tree.write("noEmail.xml")
