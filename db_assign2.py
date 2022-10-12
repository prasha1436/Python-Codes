import sqlite3

conn= sqlite3.connect('db_assign2.sqlite')
cur= conn.cursor()

cur.execute('drop table if exists Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

fname= input('Enter the mail box txt file name:')
if len(fname)<1:
    fname= 'mbox.txt'
fh= open(fname)
i= 0
for l in fh:
    l= l.rstrip()
    if not l.startswith('From '):
        continue
    words= l.split()
    email= words[1]
    lst1= email.split('@')
    org= lst1[1]
#    print(org)
    i= i+1
    cur.execute('SELECT count FROM Counts WHERE org=?', (org,))
    row= cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org, count) VALUES (?,1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count= count+1 WHERE org=?', (org,))

    if (i%10 == 0):
        conn.commit()

conn.commit()
