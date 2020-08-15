import mysql.connector
from mysql.connector import Error

#Create tge database
try:
    connection = mysql.connector.connect(host='localhost',
                                             user='YOUR_USER_HERE',         #Change this
                                             password='YOUR_PASSWORD')      #Change this

    mySql_Create_Database_Query = """CREATE DATABASE redditModLogs """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Database_Query)
    print("redditModLogss Database created successfully ")

except mysql.connector.Error as error:
    print("Failed to create Database in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

#Create the table
try:
    connection = mysql.connector.connect(host='localhost',
                                             database='redditModLogs',  
                                             user='YOUR_USER_HERE',         #Change this
                                             password='YOUR_PASSWORD')      #Change this

    mySql_Create_Table_Query = """CREATE TABLE modlogs ( 
                             actId varchar(767) NOT NULL,
                             actDate varchar(250) NOT NULL,
                             author varchar(250) NOT NULL,
                             action varchar(250) NOT NULL,
                             details varchar(767) NOT NULL,
                             PRIMARY KEY (actId)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("modlogs Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")