import sqlite3

# dont use ; using SQL in python
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Noah', 6505769609, 'ntkawasaki@gmail.com')")
db.execute("INSERT INTO contacts VALUES ('Cole', 6505752669, 'coleshaffer@email.com')")

cursor = db.cursor()  # generator: iterable that generates next value each time its used
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchone())  # fetch first
print(cursor.fetchone())  # fetch next
print(cursor.fetchone())  # no rows left

# for name, phone, email in cursor:
#     print(name, phone, email)

cursor.close()
db.commit()  # data committed to the table
db.close()

