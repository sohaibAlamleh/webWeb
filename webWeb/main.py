import sqlite3

connect = sqlite3.connect(r"C:\Users\ahmad ghazawi\Desktop\webWeb\db.sqlite3")
cursor = connect.cursor()
e = cursor.execute("SELECT * FROM test")

for i in e:
    print(i)
import os
print(os.getcwd())#show where directory
# saved
