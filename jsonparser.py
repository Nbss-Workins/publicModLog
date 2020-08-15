import json
from urllib2 import urlopen
import datetime
import dbFowarder as dbf

jdata = json.loads(urlopen('YOUR REDDIT MOD LOG JSON URL HERE').read())			#Change this

for element in jdata['data']['children']:
	actId = element['data']['id']
	actDate =  datetime.datetime.fromtimestamp(element['data']['created_utc']).strftime('%c')
	author = element['data']['mod']
	if element['data']['action'] == "add_community_topics":
		action = element['data']['details']
		details = element['data']['description']
	else:
		details = element['data']['details']
	action = element['data']['action']
	
	if dbf.checkDupe(actId) != None:
		print("Dropping action:", actId, "(Already in database)")
	else:
		dbf.insertVariblesIntoTable(actId, actDate, author, action, details)
		print("Action with ID:", actId, "added to the database")

