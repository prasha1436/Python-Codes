import sqlite3

conn= sqlite3.connect('emaildb.sqlite3')
cur= conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts(email TEXT, count INTEGER)')
fname= input('Enter the file name:')
if len(fname)<1:
    fname= 'mbox-short.txt'
fh= open(fname)
for l in fh:
    if not l.startswith('From:'):
        continue
    words= l.split()
    email= words[1]
    cur.execute('SELECT count FROM Counts WHERE email=?', (email,))
    row= cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(email, count) VALUES (?,1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count= count+1 WHERE email=?', (email,))

    conn.commit()

sqlstr= 'SELECT email, Count FROM Counts ORDER BY count DESC LIMIT 10'
for entry in cur.execute(sqlstr):
    print(entry[0], entry[1])
