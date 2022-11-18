import mysql.connector
import json
import search
import database
import os
from flask import Flask, render_template, request

app = Flask(__name__)

database.db_init()

def add_tweets(tweets):
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database="socialmedia"
  )
  cursor = mydb.cursor()
  
  for tweet in tweets:
      add_tweet = ("INSERT INTO tweets "
                   "(username, tweet)"
                   "VALUES (%s, %s)")

      data_tweet = (tweet["username"], tweet["text"])

      cursor.execute(add_tweet, data_tweet)
      mydb.commit()

  cursor.close()


@app.route('/', methods=["GET", "POST"])
def index():

    query = 'Project Management lang:en -is:retweet'

    if request.method == 'POST':
        query = '{} lang:en -is:retweet'.format(request.form['query'])

    max_results = 10 
    tweets = search.returnSearchTweetList(query, max_results)
    add_tweets(tweets)

    return render_template('index.html', **locals())

@app.route('/tweets')
def get_tweets():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database="socialmedia"
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM tweets")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)


if __name__ == "__main__":
  app.run(host ='0.0.0.0')

