from Sam import mydb
cs = mydb.cursor()
cs.execute("CREATE DATABASE Kitchen")
print("Kitchen Database is created")