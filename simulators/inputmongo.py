import pymongo
import sys

##Functions##
def connect():
 return pymongo.MongoClient("mongodb://127.0.0.1:27017")

def close():
 mongo.close()

def checkdb(mongo, dbname):
 if dbname not in mongo.list_database_names():
  sys.exit("Error: database doesn't exist")
 else:
  return mongo[dbname]
  
def checkcol(db, collection):
 if collection not in db.list_collection_names():
  sys.exit("Error: collection doesn't exist")
 else:
  return db[collection]
  
def delcontent():
 col.delete_many({})
 
def writedb(dbinput):
 col.insert_one(dbinput)
 
def listen():
 try:
  with mongo.watch([{'$match': {'operationType': 'insert'}}]) as stream:
   for insert_change in stream:
    return insert_change
 except pymongo.errors.PyMongoError:
  print("Error: Could not listen to stream")
 
def initialize(dbname, collection):
 global mongo
 global db
 global col
 
 mongo = connect()
 db = checkdb(mongo, dbname)
 col = checkcol(db, collection)
