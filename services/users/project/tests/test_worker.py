from project.mq.worker import fan_out
from project.api.users.models import Timeline

def test_fan_out(test_app, test_database, add_user, add_feed, add_follow):
    roy = add_user("roy", "roy@mherman.org")
    carina = add_user("carina", "carina@notreal.com")
    ania = add_user("ania", "ania@notreal.com")
    feed = add_feed(content="I love fried chicken", user_id=ania.id)
    add_follow(idol_id=ania.id, fan_id=roy.id)
    add_follow(idol_id=ania.id, fan_id=carina.id)
    assert Timeline.query.count() == 0

    fan_out(feed.id)

    assert Timeline.query.count() == 2