import pymongo
client = pymongo.MongoClient("mongodb+srv://dimasdwi340:mypassword@cobaclusterku.osdwh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def get_data():
    db = client.influcheck
    items = db.data_user.find()
    items = list(items)
    return items

items = get_data()


