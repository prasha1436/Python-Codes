import json
import sqlite3

conn= sqlite3.connect('rosterdb.sqlite3')
cur= conn.cursor()

cur.executescript('''

drop table if exists User;
drop table if exists Course;
drop table if exists Member;

create table User(
    id integer not null primary key autoincrement UNIQUE,
    name text UNIQUE,
    email text
);

create table Course(
    id integer not null primary key autoincrement UNIQUE,
    title text UNIQUE
);

create table Member(
    course_id integer,
    user_id integer,
    role integer,
    primary key (user_id, course_id)
)
''')

fname= input('Enter the file name:')
if len(fname)<1:
    fname= 'roster_data_assign.json'

cont= open(fname).read()
lst= json.loads(cont)
print(lst)
for item in lst:
    print('Name:', item[0], 'Course:', item[1], 'Role:', item[2])

    cur.execute('insert or ignore into User (name) values (?)', (item[0],))
    cur.execute('select id from User where name=?', (item[0], ))
    user_id= cur.fetchone()[0]

    cur.execute('insert or ignore into Course (title) values (?)', (item[1],))
    cur.execute('select id from Course where title=?', (item[1], ))
    course_id= cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role)
        VALUES ( ?, ?, ? )''',
        ( user_id, course_id, item[2]))

    conn.commit()
