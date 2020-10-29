import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully"
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,;''')
conn.commit()
conn.close()