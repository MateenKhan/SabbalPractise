from Sam import mydb
cs = mydb.cursor()
i = int(input("Enter The item_no :"))
n = input("Enter The Name :")
m = input("Enter your MadeOff :")
s = "INSERT INTO items value(%s,%s,%s)"
t =(i,n,m)
cs.execute(s,t)

