
import json
from project.api.users.models import Feed, User, Follow
from project import db


def test_feed(test_app, test_database, add_user, add_feed, add_timeline):
    client = test_app.test_client()
    roy = add_user("roy", "roy@mherman.org")
    carina = add_user("carina", "carina@notreal.com")
    ania = add_user("ania", "ania@notreal.com")
    feed = add_feed(content="fried chicken", user_id=ania.id)
    add_timeline(user_id=roy.id, feed=feed)

    resp = client.get("/timeline/roy")
    results = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert results == ["fried chicken"]
