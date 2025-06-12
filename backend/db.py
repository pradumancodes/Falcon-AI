import csv
import sqlite3

conn = sqlite3.connect("falcon.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(100))"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(100))"
cursor.execute(query)






# query = "INSERT INTO sys_command VALUES (null, 'paint', 'explorer shell:AppsFolder\\Microsoft.Paint_8wekyb3d8bbwe!App')"
# cursor.execute(query)
# conn.commit()



# query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()



# query = "DELETE FROM sys_command WHERE name='paint'"
# cursor.execute(query)
# conn.commit()



# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name VARCHAR(200), Phone VARCHAR(255), email VARCHAR(255) NULL)''')




