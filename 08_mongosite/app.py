#Team Raspberry pi
#Tianrun Liu
#
#

"""
dataset = list of current US senators
https://www.govtrack.us/api/v2/role?current=true&role_type=senator
I just edited it use text editor to format it in the format I want 
then I just used mongoimport with --jsonArray attached to it
"""

import os
from collections import OrderedDict
from flask import Flask, render_template, request, redirect, url_for, session
#from flask_pymongo import PyMongo
import pprint
from pymongo import MongoClient
from bson import json_util

import signal
import sys

#addr = "google.com"

#conf
#addr = 'mud.ddns.net:27017'
#db = 'gov'
#collection = 'senators'
#json_file = 'senator.json'
#endconf

app = Flask(__name__)
app.secret_key = os.urandom(32)

class DataStore():
	collection = None

data = DataStore()

@app.route('/', methods=['GET','POST'])
def main():
	if request.method == 'POST':
		addr = request.form['ip']
		db = request.form['db']
		collection = request.form['collection']
		client = MongoClient(addr,document_class=OrderedDict)


		#my db and collection name
		db = client[db]
		collection = db[collection]
		data.collection = collection 
		print(collection)
		session['addr'] = addr
		#print(type(collection))
		#json_util.dumps(collection)
		#print(type(collection))
		#session['collection'] = json_util.dumps(collection,default=json_util.default)
		##########################
		return render_template("request.html")
	else:
		return render_template("home.html")

@app.route('/connect',methods=['GET','POST'])
def connectdb():
	if request.method == 'POST':
		if request.form['first'] is not None:
			txt = request.values.get("first")
			#print(txt)
			list = []
			for senator in data.collection.find({"person.firstname":txt}):
				pprint.pprint(senator)
	#json_util.dups(collection)
	#session['collection'] = collection
			#print(result)
			#	pprint.pprint(post)
		#print(list)	
		return render_template("respond.html")
	#else:
	#	return redirect(url_for('connectdb'))

@app.route('/respond')
def respond():
	#if(request.method == "POST"):
		#addr = request.form[]
	return render_template("response.html")




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
	print("Please make sure your pymongo version <= 3.4.0")
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
"""

#if necessary, comment out the code below and uncomment
#code above to test db functionality
if __name__ == "__main__":
	app.debug = True
	app.run()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
