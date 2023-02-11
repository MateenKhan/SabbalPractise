from Sam import mydb
cs = mydb.cursor()
sql = "INSERT INTO kitchen.items (item_no,Name,Madeoff) VALUES (%s,%s,%s)"
val = [("01","Tea VesselL","Steel"),
       ("02","Milk Vessels","Steel"),
       ("03", "Bowls","Steel"),
       ("04", "Bowls","Plastic"),
       ("05", "Spoons","Steel"),
       ("06", "Folks","Steel"),
       ("07", "Frying Pan","aluminum")]
cs.executemany(sql, val)
mydb.commit()
print(cs.rowcount, "details inserted")


