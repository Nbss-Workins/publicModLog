import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def checkDupe(actId):
	try:
		connection = mysql.connector.connect(host='localhost',
											database='redditModLogs',
											user='YOUR_USER_HERE',				#Change this
											password='YOUR_PASSWORD')			#Change this
		cursor = connection.cursor()
		cursor.execute("SELECT * from modlogs WHERE actId = %s", (actId,))
		rows = cursor.fetchone()

	except mysql.connector.Error as error:
	    print("Failed to check into table {}".format(error))

	finally:
		if (connection.is_connected()):
			cursor.close()
			connection.close()
			print("MySQL connection is closed")
			return(rows)

def insertVariblesIntoTable(actId, actDate, author, action, details):
	try:
		connection = mysql.connector.connect(host='localhost',
											database='redditModLogs',
											user='YOUR_USER_HERE',					#Change this
											password='YOUR_PASSWORD')				#Change this
		cursor = connection.cursor()
		mySql_insert_query = """INSERT INTO modlogs (actId, actDate, author, action, details) 
								VALUES 
								(%s, %s, %s, %s, %s) """

		recordTuple = (actId, actDate, author, action, details)
		cursor.execute(mySql_insert_query, recordTuple)
		connection.commit()
		print("Record inserted successfully into Laptop table")
	
	except mysql.connector.Error as error:
		print("Failed to insert into table {}".format(error))

	finally:
		if (connection.is_connected()):
			cursor.close()
			connection.close()
			print("MySQL connection is closed")