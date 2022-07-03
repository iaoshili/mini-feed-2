# services/users/project/api/__init__.py


from flask_restx import Api
from project.api.ping import ping_namespace
from project.api.feed import feed_namespace
from project.api.friend import friend_namespace
from project.api.timeline import timeline_namespace 
from project.api.users.views import users_namespace

api = Api(version="1.0", title="Users API", doc="/doc/")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(feed_namespace, path="/feed")
api.add_namespace(friend_namespace, path="/friend")
api.add_namespace(users_namespace, path="/users")
api.add_namespace(timeline_namespace, path="/timeline")
