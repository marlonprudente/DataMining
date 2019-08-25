#Import MongoClient from pymongo.

from pymongo import MongoClient
import json

#Use MongoClient to create a connection:
client = MongoClient()


#To assign the database named primer to the local variable db
db = client['twitterData']

#You can access collection objects directly using dictionary-style
db['checkins']

listaCheckins = open('saidaColetaStream.txt','r')

for jsonData in listaCheckins:
  
  result = db.checkins.insert_one(json.loads(jsonData))
  
  