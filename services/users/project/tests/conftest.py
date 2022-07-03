# services/users/project/tests/conftest.py


import pytest
from project import create_app, db
from project.api.users.models import Feed, Timeline, User, Follow


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("project.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="module")
def add_user():
    def _add_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user


@pytest.fixture(scope="module")
def add_feed():
    def _add_feed(content, user_id):
        feed = Feed(content=content, user_id=user_id)
        feed.save()
        return feed 

    return _add_feed


@pytest.fixture(scope="module")
def add_follow():
    def _add_follow(idol_id, fan_id):
        follow = Follow(idol_id=idol_id, fan_id=fan_id)
        db.session.add(follow)
        db.session.commit()
        return follow

    return _add_follow


@pytest.fixture(scope="module")
def add_timeline():
    def _add_timeline(user_id, feed):
        timeline = Timeline(user_id=user_id, feed_id=str(feed.id), created_at=feed.created_at)
        db.session.add(timeline)
        db.session.commit()
        return timeline

    return _add_timeline 
