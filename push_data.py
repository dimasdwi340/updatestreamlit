import pymongo
import json
from list_data import data
client = pymongo.MongoClient("mongodb+srv://dimasdwi340:mypassword@cobaclusterku.osdwh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.influcheck

for data in data:
    with open(f'new_dataset/{data}') as f:
        file_data = json.load(f)
        #print (file_data)
        push = db.datatesting.insert_one(file_data)
        if push:
            print (data, '... ok')
        else:
            print (data, '... failed')
    # push
