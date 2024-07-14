from . import db
from flask_login import UserMixin

followers = db.Table(
    "followers",
    db.Column("follower_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("following_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    active_activity = db.relationship(
        "Activity",
        uselist=False,
        backref="author",
        lazy=True,
        foreign_keys="Activity.user_id",
    )
    following = db.relationship(
        "User",
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.following_id == id),
        backref=db.backref("followers", lazy="dynamic"),
        lazy="dynamic",
    )

    def is_following(self, user):
        return self.following.filter(followers.c.following_id == user.id).count() > 0

    def is_followed_by(self, user):
        return self.followers.filter(followers.c.follower_id == user.id).count() > 0


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    active = db.Column(
        db.Boolean, default=False
    )  # Added field to indicate if activity is active
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
