import pymongo
from pymongo import MongoClient
from bson import json_util

client = MongoClient('mud.ddns.net:27017')

db = client['test']
collection = db['restaurants']

fd = open('primer-dataset.json','r')
line = fd.readline()
counter = 1
while line:
	print(line)
	#line = fd.readline()
	data = json_util.loads(line)
	doc = db.doc
	doc_id = doc.insert_one(data).inserted_id
	counter += 1

fd.close()
