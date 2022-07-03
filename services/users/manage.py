# services/users/manage.py


import sys

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.users.models import User, Feed

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    Feed.objects.delete()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(username="michael", email="hermanmu@gmail.com"))
    db.session.add(User(username="michaelherman", email="michael@mherman.org"))
    db.session.add(User(username="roy", email="roy@gmail.com"))
    db.session.add(User(username="carina", email="carina@gmail.com"))
    db.session.add(User(username="ania", email="ania@gmail.com"))
    db.session.commit()


if __name__ == "__main__":
    cli()
