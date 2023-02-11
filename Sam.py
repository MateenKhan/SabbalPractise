import mysql.connector

# Connecting to the Database
mydb = mysql.connector.connect(
    host='127.0.0.1',
    database='kitchen',
    user='root',
    password = "root",

)
cs = mydb.cursor()
