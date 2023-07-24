import mysql.connector
conn = mysql.connector.connect (host='localhost', password='hesoyam21', user='root')

if conn.is_connected():
   print("connection established :)")
