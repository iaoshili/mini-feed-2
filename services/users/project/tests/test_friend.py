
import json
from project.api.users.models import Feed, User, Follow
from project import db


def test_feed(test_app, test_database, add_user):
    client = test_app.test_client()
    roy = add_user("roy", "roy@mherman.org")
    add_user("carina", "carina@notreal.com")
    add_user("ania", "ania@notreal.com")
    resp = client.post("/friend", json={"fan_name": "roy", "idol_name": "ania"})
    id = json.loads(resp.data.decode())
    assert resp.status_code == 201
    fan_id = Follow.query.filter_by(id=id).first().fan_id 
    assert fan_id == roy.id
