# services/users/project/api/feed.py


from flask import request
from flask_restx import Namespace, Resource
from project.api.users.crud import get_user_by_name
from project.api.users.models import Feed
from project.mq.producer import enqueue

feed_namespace = Namespace("feed")


class FeedResource(Resource):
    def post(self):
        post_data = request.get_json()
        content = post_data.get("content")
        user_name = post_data.get("user_name")
        user_id = get_user_by_name(user_name).id
        feed = Feed(content=content, user_id=user_id)
        feed.save()
        enqueue(feed.id)
        return str(feed.id), 201


feed_namespace.add_resource(FeedResource, "")
