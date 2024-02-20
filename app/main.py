import sqlite3

conn = sqlite3.connect('test_new.db')

cur = conn.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")

# cur.execute('SELECT * FROM posts')
# 
# print(cur.fetchone())
# # (1, 'Post 1', 'Content for post 1')
#
# print(cur.fetchone()[2])
# # Content for post 2
#
# for row in cur.execute('SELECT * FROM posts'):
#     print(dict(zip(['id', 'title', 'content'], row)))
