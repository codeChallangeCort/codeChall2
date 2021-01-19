import pandas as pd
import json
import sys


# waiting for an input from user and should be file_name.csv"

try:
    print("Please provide the input files: ")
    filenames = sys.argv[1]
except Exception as e:
    sys.exit()

# Empty Dictionary for JSON dumps

json_data = {}

# List of customers information including first_name, last_name and email.

json_data["user_list"] = []

# list_id will start from 0

list_id = 1

# user_list_size is the count of customer 

json_data["user_list_size"] = 0


def getInfo(row):
    """
    This FUncation will split the full name in firstname and lastname, with list_id, and will dump that information in temporary dict
    and temp dict into a list of
    json_data
    """ 

    # json_temp is to get the info for a individual customer for temporary time.
    
    json_temp = {}
    global list_id
    json_temp["list_id"] = list_id
    
    if (row["full_name"].find(" ") != -1):
        full_name = row["full_name"].split(" ")
        json_temp["first_name"] = full_name[0]
        json_temp["last_name"] = full_name[1]
    else:
        json_temp["first_name"] = row["full_name"]
        json_temp["last_name"] = ""
    json_temp["email"] = row["email"]

    # json_temp will be appended into the list of json_data.

    json_data["user_list"].append(json_temp)
    list_id += 1
    
# If more than one filesname has been passed with "," then for each file data would be readed and stored into json_data.
    
for filename in filenames.split(","):
    df = pd.read_csv(filename)
    json_data["user_list_size"] += len(df)
    df.apply(lambda x: getInfo(x),axis=1)

# To dump the json_data into outfile.

with open('results.json', 'w') as outfile:
    json.dump(json_data, outfile, indent=4)
