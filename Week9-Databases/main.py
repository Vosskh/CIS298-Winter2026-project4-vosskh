# from https://www.py4e.com/html3/15-database

import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Track')
# cur.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')

cur.execute("INSERT INTO artist (name, eyes) VALUES ('Frank Sinatra', 'blue')")
conn.commit()
conn.close()