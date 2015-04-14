import shelve
import sqlite3

db1 = shelve.open('ng.db')
conn = sqlite3.connect('linggle.db')
cursor = conn.cursor()

for k in db1.keys():
    for v in db1[k]:
        result = v[0].encode('utf-8')
        pos = v[1].encode('utf-8')
        count = int(v[2].encode('utf-8'))
        cursor.execute("INSERT INTO pair VALUES ('{}', '{}', '{}', '{}')".format(k, result, pos, count))

conn.commit()
conn.close()
