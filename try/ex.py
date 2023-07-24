import mysql.connector
conn = mysql.connector.connect (host='localhost', ', user='root')

if conn.is_connected():
   print("connection established :)")
