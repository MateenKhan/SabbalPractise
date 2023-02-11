from Sam import mydb

cs = mydb.cursor()
i = input("Enter The item_no :")
query = "SELECT item_no,Name,madeoff FROM items"
cs.execute(query)

myresult = cs.fetchone()
for row in myresult:
    print(row)
