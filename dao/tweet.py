import user


def add_tweet(db, tweet_json):
    user_list = db.user.find({'id': tweet_json['user']['id']})
    if len(user_list) > 0:
        tweet_user = user_list[0]
    else:
        user.add_user(db, tweet_json['user'])
        tweet_user = db.user.find({'id': tweet_json['user']['id']})[0]
    tweet_json['user'] = tweet_user['_id']

    if tweet_json['quoted_status']:
        q_list = db.tweet.find({'id': tweet_json['quoted_status']['id']})
        if len(q_list) > 0:
            quote = q_list[0]
        else:
            add_tweet(db, tweet_json['quoted_status'])
            quote = db.tweet.find({'id': tweet_json['quoted_status']['id']})[0]
        tweet_json['quoted_status'] = quote['_id']

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
