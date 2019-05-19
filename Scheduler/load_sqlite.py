import sqlite3
import pprint

db = sqlite3.connect('jobs.sqlite')
cur = db.cursor() 

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
table = tables[0][0]
print(tables)
print(table)

cur.execute("PRAGMA table_info({})".format(table))
pprint.pprint(cur.fetchall())

cur.execute("SELECT * FROM {}".format(table))
result = cur.fetchall()
s = result[-1][-1]
print(s.decode("utf-8", errors="ignore"))
print(type(s))
