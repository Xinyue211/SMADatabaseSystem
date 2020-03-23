from flask import Flask
from flask_pymongo import PyMongo
from flask import request
from flask import render_template

from dao import tweet

from helper import gzip_parser

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/smaDB"
mongo = PyMongo(app)


@app.route('/data_list')
def show_data_list():
    return render_template('tweet_list.html', data_list=tweet.get_all(mongo.db))


@app.route('/upload_gzip')
def upload_gzip():
    if request.method == 'POST':
        jsons = gzip_parser.to_json(request.form['path'])
        for tweet_json in jsons:
            tweet.add_tweet(mongo.db, tweet_json)
        return render_template('upload_gzip.html', uploaded='true')
    else:
        return render_template('upload_gzip.html', uploaded='false')


if __name__ == '__main__':
    app.run()
