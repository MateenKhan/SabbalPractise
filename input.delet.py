from Sam import mydb
cs = mydb.cursor()
id = input("enter id to delete:: ")
s = "DELETE FROM items WHERE item_no = "+id
cs.execute(s)
mydb.commit()
mydb.close()

