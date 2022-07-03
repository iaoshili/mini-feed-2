# services/users/project/api/timeline.py


from flask_restx import Namespace, Resource
from flask import request
from project.api.users.crud import get_user_by_name, follow, get_timeline
from project.cache.global_cache import cached

timeline_namespace = Namespace("timeline")


@timeline_namespace.route('/<username>')
@timeline_namespace.param('username')
class TimelineResource(Resource):
    def get(self, username):
        return _get_timeline(username)


@cached
def _get_timeline(username):
    user = get_user_by_name(username)

    feeds = get_timeline(user_id=user.id)

    return [feed.content for feed in feeds], 201


timeline_namespace.add_resource(TimelineResource, "")
