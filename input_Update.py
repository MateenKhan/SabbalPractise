from Sam import mydb
cs = mydb.cursor()

Madeoff = input("Enter The Madeoff : ")
Name = input("Enter The Name : ")
statement = "UPDATE items SET Madeoff = %s WHERE Name =%s "
data =(Name,Madeoff)
try :
  cs.execute(statement,data)
  mydb.commit()
  print("Data Updated.....")
except :
  print("Error....")











