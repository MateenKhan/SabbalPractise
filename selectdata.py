from Sam import mydb

cs = mydb.cursor()

query = "SELECT * FROM kitchen.items"
cs.execute(query)

myresult = cs.fetchall()

for x in myresult:
    print(x)

# disconnecting from server
