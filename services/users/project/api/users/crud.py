# services/users/project/api/users/crud.py


from project import db
from project.api.users.models import Feed, Follow, Timeline, User


def get_all_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_by_name(username):
    return User.query.filter_by(username=username).first()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def update_user(user, username, email):
    user.username = username
    user.email = email
    db.session.commit()
    return user


def delete_user(user):
    db.session.delete(user)
    db.session.commit()
    return user


def follow(fan_id, idol_id):
    record = Follow(idol_id=idol_id, fan_id=fan_id)
    db.session.add(record)
    db.session.commit()
    return record


def get_feed_by_id(id):
    return Feed.objects.get(id=id)


def get_fans(idol_id):
    follow_records = Follow.query.filter_by(idol_id=idol_id).all()
    return [get_user_by_id(r.fan_id) for r in follow_records]


def add_to_timeline(user_id, feed):
    timeline = Timeline(user_id=user_id, feed_id=str(feed.id), created_at=feed.created_at)
    db.session.add(timeline)
    db.session.commit()
    return timeline 


def get_timeline(user_id):
    timelines = Timeline.query.filter_by(user_id=user_id).order_by(Timeline.created_at.desc()).limit(5)
    feed_ids = [timeline.feed_id for timeline in timelines]
    feeds = Feed.objects(id__in=feed_ids)
    return feeds
