from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from . import db
from .models import User, Activity


views_bp = Blueprint("views_bp", __name__)


@views_bp.route("/", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views_bp.route("/follow/<int:user_id>", methods=["POST"])
@login_required
def follow(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    if current_user == user:
        return jsonify({"error": "You cannot follow yourself"}), 400
    if current_user.is_following(user):
        return jsonify({"message": f"You are already following {user.username}"}), 200

    current_user.followed.append(user)
    db.session.commit()
    return jsonify({"message": f"You are now following {user.username}"}), 200


@views_bp.route("/unfollow/<int:user_id>", methods=["POST"])
@login_required
def unfollow(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    if current_user == user:
        return jsonify({"error": "You cannot unfollow yourself"}), 400
    if not current_user.is_following(user):
        return jsonify({"message": f"You are not following {user.username}"}), 200

    current_user.followed.remove(user)
    db.session.commit()
    return jsonify({"message": f"You have unfollowed {user.username}"}), 200
