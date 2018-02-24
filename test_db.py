import sqlite3

conn = sqlite3.connect('D:/Coding/database/seloger.db')
c = conn.cursor()

# t = ('RHAT',)
c.execute('SELECT count(id) FROM ids')
nb = c.fetchone()
print(nb)

for id in c.execute('SELECT * FROM ids limit 10'):
	print(id[0])

#c.execute("INSERT INTO data values ('1','2','3')")
c.execute('SELECT * FROM data')
print(c.fetchall())


conn.commit()
conn.close()
