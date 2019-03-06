"""
dataset = list of current US senators
https://www.govtrack.us/api/v2/role?current=true&role_type=senator
I just edited it use text editor to format it in the format I want 
then I just used mongoimport with --jsonArray attached to it
"""
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
db = 'gov'
collection = 'senators'
json_file = 'senator.json'
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

#pprint.pprint(doc.find_one())

def one():
	#print("ok\n")
	print("first letter of your response should be capitalized")
	txt = raw_input("enter the firstname\n")
	for post in collection.find({"person.firstname":txt}):
		pprint.pprint(post)
	#{"address": {"zipcode": txt}}))

def two():
	print("first letter of your response should be capitalized")
	txt = raw_input("enter the lastname\n")
	for post in collection.find({"person.lastname":txt}):
		pprint.pprint(post)

def three():
	#txt = raw_input("enter the cspnid\n")
	xtx = input("enter the cspanid\n")
	for post in collection.find({"person.cspanid":xtx}):
		pprint.pprint(post)

def four():
	print("first letter of your response should be capitalized, and don't append \"party\" to it")
	txt = raw_input("enter the party name\n")
	#xtx = input("enter the score\n")
	for post in collection.find({"party":txt}):
		pprint.pprint(post)
	#	pprint.pprint(post)
	#print("donno how to do it, need more time reading the pymongo doc\n")


def five():
	print("bye\n")
	sys.exit(0)

while True:
	print("Pymongo demo program")
	print("Using mongodb at " + addr)
	print("choose one")
	print("1. find senator/s by firstname")
	print("2. find senator/s by lastname")
	print("3. find senator by cspanid")
	print("4. find senator by party")
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
