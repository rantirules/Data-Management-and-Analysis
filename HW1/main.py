import csv
from datetime import datetime
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
print(dates_new_cases_average)

# CSV QUESTION 3

# JSON QUUESTION 1
# import json
# with open("movies.json", "r") as json_file:
#     json_to_dict = json.load(json_file) #json.load() converts from json to dictionary
#     print(type(json_to_dict))
#     average = 0
#     for key in json_to_dict:
#         average = sum(key["ratings"])/len(key["ratings"])
#         # print(average)
#         if key == "averageRating":
#             key["averageRating"] = average
#         # print(key["ratings"])
# output = open("averageUpdated.json", "w")
# json.dump(json_to_dict, output, indent=4)
# output.close()

# import json
# with open("movies.json", "r") as json_file:
#     output = open("averageUpdated1.json", "w")
#     # json.dump(json_file, output, indent=4)
#     data = json.load(json_file)
#     for i in data:
#         # print(type(i))
#         # average = 0
#         for key, value in i.items():
#             # print(key)
#             # print(value)
#             if key == "ratings":
#                 # average = sum(key["ratings"])/len(key["ratings"])
#                 average = sum(value)/len(value)
#             elif key == "averageRating":
#                 value = average
#                 average = 0
#     json.dump(data, output, index=6)
#     output.close()                
    # print(type(data))
    # print(type(data[0]))


# import json
# movie_file = open('movies.json', 'r')
# movie_file_string = json.dump(movie_file)
# # json_string_to_dict = json.loads(movie_file_string)
# print(type(movie_file_string ))
# movie_file.close()
# import json
# json_file = open('movies.json', 'r') # read the movies.json file
# output = open("averageUpdated.json", "w")
# # with open("averageUpdated.json", "w") as output: # create the new file where we want to store the data
# json_to_list = json.load(json_file) #json.loads() converts from json to dictionary
# # json_to_dict = dict.fromkeys(json_to_list)
# # print(type(json_to_dict))
# average = 0

# for key in json_file:
#     # print(key[2])
#     int_list = [int(i) for i in key["ratings"]]
#     average = sum(int_list)/len(int_list)
#     #         # print(average)
#     if key == "averageRating":
#          key["averageRating"] = average
#                 # print(key["ratings"])
#             #output = open("averageUpdated.json", "w")
# json.dump(json_file, output, indent=4)
# json_file.close()
# output.close()
