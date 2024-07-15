from flask import Blueprint, render_template, jsonify, request, flash
from flask_login import login_required, current_user
from . import db
from .models import User
import json

contacts_bp = Blueprint("contacts_bp", __name__)


@contacts_bp.route("/followers")
@login_required
def followers():
    return render_template("followers.html", user=current_user)


@contacts_bp.route("/following", methods=["GET", "POST"])
@login_required
def following():
    if request.method == "POST":
        requested_user = User.query.filter_by(
            username=request.form.get("follow_req_username")
        ).first()

        if requested_user:
            if requested_user == current_user:
                flash("Cannot follow yourself", category="error")
            elif current_user.is_following(requested_user):
                flash(
                    f"Already following {requested_user.username}",
                    category="error",
                )
            else:
                current_user.following.append(requested_user)
                db.session.commit()
                flash(
                    f"Now following {requested_user.username}",
                    category="success",
                )
        else:
            flash("User not found", category="error")

    return render_template("following.html", user=current_user)


@contacts_bp.route("/unfollow", methods=["POST"])
@login_required
def unfollow():
    unfollow_req = json.loads(request.data)
    follower_id = unfollow_req["follower_id"]
    follower = User.query.get(follower_id)
    if follower and follower in current_user.followers:
        current_user.followers.remove(follower)
        db.session.commit()
        flash("Follower removed", category="success")
    return jsonify({})
