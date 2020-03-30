
def add_tweet(db, tweet_json):
    # Add quote reference if there is nonempty 'quoted_status' in the tweet's json
    if tweet_json['quoted_status']:
        q_list = db.tweet.find({'id': tweet_json['quoted_status']['id']})
        if len(q_list) > 0:
            quote = q_list[0]
        else:
            add_tweet(db, tweet_json['quoted_status'])
            quote = db.tweet.find({'id': tweet_json['quoted_status']['id']})[0]
        tweet_json['quoted_status'] = quote['_id']

    # Add retweet reference if there is nonempty 'retweeted_status' in the tweet's json
    if tweet_json['retweeted_status']:
        t_list = db.tweet.find({'id': tweet_json['retweeted_status']['id']})
        if len(t_list) > 0:
            quote = t_list[0]
        else:
            add_tweet(db, tweet_json['retweeted_status'])
            quote = db.tweet.find({'id': tweet_json['retweeted_status']['id']})[0]
        tweet_json['retweeted_status'] = quote['_id']

    db.tweet.insert(tweet_json)


def get_all(db):
    return db.tweet.find()
