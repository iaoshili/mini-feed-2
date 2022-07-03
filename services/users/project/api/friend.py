# services/users/project/api/friend.py


from flask import request
from flask_restx import Namespace, Resource
from project.api.users.crud import follow, get_user_by_name

friend_namespace = Namespace("friend")


class Friend(Resource):
    def post(self):
        post_data = request.get_json()
        idol_name = post_data.get("idol_name")
        fan_name = post_data.get("fan_name")
        idol = get_user_by_name(idol_name)
        fan = get_user_by_name(fan_name)
        record = follow(idol_id=idol.id, fan_id=fan.id)
        # TODO, async construct timeline

        return record.id, 201


friend_namespace.add_resource(Friend, "")
