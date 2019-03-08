# Team Raspberry pi - Tianrun Liu, Brian Lee, Damian Wasilewicz
# SoftDev2 pd6
# K08 -- Ay Mon, Go Git It From Yer Flask
# 2019-03-07

"""
dataset = list of current US senators
https://www.govtrack.us/api/v2/role?current=true&role_type=senator
I just edited it use text editor to format it in the format I want 
then I just used mongoimport with --jsonArray attached to it
"""

import os
import pprint

from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)
app.secret_key = os.urandom(32)

# mongodb constants
DEFAULTADDR = "mud.ddns.net"
DBNAME = "gov"
COLNAME = "senators"

@app.route('/', methods=['GET','POST'])
def main():
	if request.method == 'POST':
		addr = request.form['ip']
		if len(addr) == 0:
			addr = DEFAULTADDR
		client = MongoClient(addr)

		db = client[DBNAME]
		collection = db[COLNAME]
		session['addr'] = addr
		return render_template("request.html")
	else:
		return render_template("home.html")

@app.route('/config', methods=['GET','POST'])
def config():
	if request.method == 'POST':
		addr = request.form['ip']
		if len(addr) == 0:
			addr = DEFAULTADDR
		client = MongoClient(addr)

		db = client[DBNAME]
		collection = db[COLNAME]
		session['addr'] = addr
		return render_template("config.html", ip=addr)
	else:
		if 'addr' not in session:
			session['addr'] = DEFAULTADDR
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

def destroy_db():
	# TODO: helper function to drop a mongodb db at a given IP
	pass

def create_db():
	# TODO: helper function to create a mongodb db at a given IP
	pass

if __name__ == "__main__":
	app.debug = True
	app.run()
