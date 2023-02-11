import mysql.connector

dataBase = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root"
)
cursorObject = dataBase.cursor()
cursorObject.execute("use kitchen")
TableName = "CREATE TABLE items (" \
            "item_no int(255)," \
            "Name VARCHAR(255)," \
            "Madeoff VARCHAR(255) " \
            ");"
cursorObject.execute(TableName)
print("Items Table is Created in the Kitchen Database")