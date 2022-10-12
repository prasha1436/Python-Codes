import xml.etree.ElementTree as ET
import sqlite3

conn= sqlite3.connect('tracksdb.sqlite3')
cur= conn.cursor()

cur.executescript('''

drop table if exists Artist;
drop table if exists Album;
drop table if exists Track;

create table Artist(
    id integer not null primary key autoincrement UNIQUE,
    name text UNIQUE
);

create table Album(
    id integer not null primary key autoincrement UNIQUE,
    title text UNIQUE,
    artist_id integer
);

create table Track(
    id integer not null primary key autoincrement UNIQUE,
    title text UNIQUE,
    album_id integer,
    len integer, rating integer, count integer
)
''')

fname= input('Enter the file name:')
if len(fname)<1:
    fname= 'Library.xml'

def lookup(d, key):
    found= False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found= True
    return None

fhand= ET.parse(fname)
alls= fhand.findall('dict/dict/dict')

for entry in alls:
    if(lookup(entry, 'Track ID') is None):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None :
        continue

    print(name, artist, album, count, rating, length)

    cur.execute('insert or ignore into Artist (name) values (?)', (artist,))
    cur.execute('select id from Artist where name=?', (artist, ))
    artist_id= cur.fetchone()[0]

    cur.execute('insert or ignore into Album (title, artist_id) values (?,?)', (album, artist_id))
    cur.execute('select id from Album where title=?', (album, ))
    album_id= cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count ) )

    conn.commit()
