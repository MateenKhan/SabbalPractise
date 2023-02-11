from Sam import mydb

cs = mydb.cursor()


statement = "UPDATE items SET Madeoff = 'Steel' WHERE Name ='Spoons'"
print("Data Updated..!!!")
cs.execute(statement)
mydb.commit()


mydb.close()