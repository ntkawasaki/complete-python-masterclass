import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "new_email@update.com"
phone = input("Please enter your phone number: ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)  # store SQL
# parameter substitution, sqlite library sanitizes input
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} row updates".format(update_cursor.rowcount))

print()
print("Are cursors the same? {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()  # use cursors connection property for commits
update_cursor.close()

# unpacked
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("=" * 40)

db.close()
