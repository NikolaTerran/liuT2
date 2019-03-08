# Team Raspberry pi - Tianrun Liu, Brian Lee, Damian Wasilewicz
# SoftDev2 pd6
# K08 -- Ay Mon, Go Git It From Yer Flask
# 2019-03-07

"""
dataset = list of current US senators
https://www.govtrack.us/api/v2/role?current=true&role_type=senator
"""

import os
import json

from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = os.urandom(32)

# mongodb constants
DEFAULTADDR = "178.128.157.14"
# DEFAULTADDR = "mud.ddns.net"
DBNAME = "gov"
COLNAME = "senators"

@app.route('/', methods=['GET','POST'])
def main():
	if request.method == 'POST':
		addr = request.form['ip']
		if len(addr) == 0:
			addr = DEFAULTADDR
		session['addr'] = addr
		return render_template("request.html")
	else:
		return render_template("home.html")

@app.route('/config', methods=['GET','POST'])
def config():
	if 'addr' not in session:
		session['addr'] = DEFAULTADDR
	if request.method == 'POST':
		destroy_db(session['addr'])

		addr = request.form['ip']
		if len(addr) == 0:
			addr = DEFAULTADDR
		client = MongoClient(addr)

		db = client[DBNAME]
		collection = db[COLNAME]
		session['addr'] = addr

		# Probably should handle errors
		create_db(addr)
	return render_template("config.html", ip=session['addr'])

@app.route('/connect',methods=['GET','POST'])
def connectdb():
	if request.method == 'POST':
		if request.form['first'] is not None:
			txt = request.values.get("first")
			#print(txt)
			list = []
			for senator in data.collection.find({"person.firstname":txt}):
				pprint.pprint(senator)
		return render_template("respond.html")

@app.route('/respond')
def respond():
	#if(request.method == "POST"):
		#addr = request.form[]
	return render_template("response.html")

def destroy_db(addr):
	print("Destroying database at " + addr)
	client = MongoClient(addr, serverSelectionTimeoutMS=3000)
	client.drop_database(DBNAME)

def create_db(addr):
	client = MongoClient(addr, serverSelectionTimeoutMS=3000)
	collection = client[DBNAME][COLNAME]
	print("Creating database at " + addr)
	with open('senator.json', 'r') as f:
		collection.insert_many(json.loads(f.read())['objects'])

if __name__ == "__main__":
	destroy_db(DEFAULTADDR)
	create_db(DEFAULTADDR)
	app.debug = True
	# use_reloader prevents create_db from executing twice
	app.run(use_reloader=False)
