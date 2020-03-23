def add_user(db, user_json):
    db.user.insert(user_json)