# services/users/project/tests/test_rest_feed.py


import json
from project.api.users.models import Feed


def test_feed(test_app):
    client = test_app.test_client()
    resp = client.post("/feed", json={"content": "random string"})
    feed_id = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert Feed.objects.get(id=feed_id).content == "random string"
