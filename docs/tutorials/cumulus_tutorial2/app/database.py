import mysql.connector
import os
import time

def db_init():
  connected = False
  retries = 10
  mydb = None

  while not connected and retries > 0:
      try:
          mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password=os.environ['MYSQL_ROOT_PASSWORD']
          )
          connected = True
      except:
          retries = retries - 1
          time.sleep(1)

  assert mydb != None
  assert connected
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS socialmedia")
  cursor.execute("CREATE DATABASE socialmedia")
  cursor.close()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database="socialmedia"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS tweets")
  cursor.execute("CREATE TABLE tweets (username VARCHAR(255), tweet VARCHAR(800))")
  cursor.close()

  return 'init database'
