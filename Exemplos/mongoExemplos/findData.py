from pymongo import MongoClient

client = MongoClient()
db = client['twitterData']

cursor = db.checkins.find()

#cursor = db.checkins.find({"user.screen_name": "soldadonofront"})

#cursor = db.checkins.find({"user.followers_count": {"$gt": 5000}})

for document in cursor:
    print(document)
