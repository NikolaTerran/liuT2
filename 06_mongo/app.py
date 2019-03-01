import pymongo
import pprint
from pymongo import MongoClient
from bson import json_util

import signal
import sys

def signal_handler(sig, frame):
	print('bye\n')
	sys.exit(0)

#conf
addr = 'mud.ddns.net:27017'
db = 'test'
collection = 'restaurants'
json_file = 'primer-dataset.json'
#endconf

signal.signal(signal.SIGINT, signal_handler)

client = MongoClient(addr)
db = client[db]
collection = db[collection]

"""
fd = open(json_file,'r')
line = fd.readline()
counter = 1
while line:
	#print(line)
	line = fd.readline()
	data = json_util.loads(line)
	doc = db.doc
	doc_id = doc.insert_one(data).inserted_id
	counter += 1

fd.close()
"""

doc = db.doc
#pprint.pprint(doc.find_one())

def one():
	#print("ok\n")
	txt = raw_input("enter the zipcode\n")
	for post in doc.find({"address.zipcode":txt}):
		pprint.pprint(post)
	#{"address": {"zipcode": txt}}))

def two():
	txt = raw_input("enter the borough\n")
	for post in doc.find({"borough":txt}):
		pprint.pprint(post)

def three():
	txt = raw_input("enter the zipcode\n")
	xtx = raw_input("enter the grade\n")
	for post in doc.find({"$and":[{"address.zipcode":txt},{"grades.grade":xtx}]}):
		pprint.pprint(post)

def four():
	#txt = raw_input("enter the zipcode\n")
	#xtx = raw_input("enter the grade\n")
	#for post in doc.find({"$and":[{"address.zipcode":txt},{$where:"grades.grade < xtx"}]}):
	#	pprint.pprint(post)
	pprint("donno how to do it, need more time reading the pymongo doc\n")

def five():
	print("bye\n")
	sys.exit(0)

while True:
	print("Pymongo demo program")
	print("Using mongodb at " + addr)
	print("choose one")
	print("1. get all restaurants in a specified zip code")
	print("2. get all restaurants in a specified borough")
	print("3. get all restaurants in a specified zip code and with a specified grade")
	print("4. get all restaurants in a specified zip code with a score below a specified threshold")
	print("other: exit\n")
	txt = input("waiting for a numerical input\n")
	
	if(txt == 1):
		one()
	elif(txt == 2):
		two()
	elif(txt == 3):
		three()
	elif(txt == 4):
		four()
	else:
		five()
