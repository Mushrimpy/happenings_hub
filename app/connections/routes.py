from flask import Blueprint, render_template, jsonify, request, flash
from flask_login import login_required, current_user
from .. import db
from ..models import User, FriendRequest
import json

connections_bp = Blueprint(
    "connections_bp",
    __name__,
    template_folder="templates",
)


@connections_bp.route("/followers")
@login_required
def followers():
    return render_template(
        "followers.html",
        user=current_user,
        followers=current_user.followers[::-1],
        follow_requests=current_user.received_requests[::-1],
    )


@connections_bp.route("/following", methods=["GET", "POST"])
@login_required
def following():
    if request.method == "POST":
        requested_user = User.query.filter_by(
            username=request.form.get("follow_req_username")
        ).first()

        if requested_user:
            if requested_user == current_user:
                flash("You cannot follow yourself", category="error")
            elif any(
                req.receiver_id == requested_user.id
                for req in current_user.sent_requests
            ):
                flash(
                    f"Already sent a friend request to {requested_user.username}",
                    category="error",
                )
            else:
                new_request = FriendRequest(
                    sender_id=current_user.id, receiver_id=requested_user.id
                )
                db.session.add(new_request)
                db.session.commit()
                flash(
                    f"Friend request sent to {requested_user.username}",
                    category="success",
                )
        else:
            flash("User not found", category="error")

    return render_template(
        "following.html", user=current_user, following=current_user.following[::-1]
    )


@connections_bp.route("/accept-request", methods=["POST"])
@login_required
def accept_request():
    follow_req = json.loads(request.data)
    request_id = follow_req["request_id"]
    friend_request = FriendRequest.query.get(request_id)
    if friend_request and friend_request.receiver_id == current_user.id:
        sender = User.query.get(friend_request.sender_id)
        current_user.followers.append(sender)
        db.session.delete(friend_request)
        db.session.commit()
        flash(f"Friend request from {sender.username} accepted", category="success")
    return jsonify({})


@connections_bp.route("/decline-request", methods=["POST"])
@login_required
def decline_request():
    follow_req = json.loads(request.data)
    request_id = follow_req["request_id"]
    friend_request = FriendRequest.query.get(request_id)
    if friend_request and friend_request.receiver_id == current_user.id:
        sender = User.query.get(friend_request.sender_id)
        db.session.delete(friend_request)
        db.session.commit()
        flash(f"Friend request from {sender.username} declined", category="success")
    return jsonify({})


@connections_bp.route("/remove-follower", methods=["POST"])
@login_required
def remove_follower():
    remove_follower_req = json.loads(request.data)
    follower_id = remove_follower_req["follower_id"]
    follower = User.query.get(follower_id)
    if follower and follower in current_user.followers:
        current_user.followers.remove(follower)
        db.session.commit()
        flash(f"No longer followed by {follower.username}", category="success")
    return jsonify({})


@connections_bp.route("/unfollow", methods=["POST"])
@login_required
def unfollow():
    unfollow_req = json.loads(request.data)
    followed_id = unfollow_req["followed_id"]
    followed = User.query.get(followed_id)
    if followed and followed in current_user.following:
        current_user.following.remove(followed)
        db.session.commit()
        flash(f"No longer following {followed.username}", category="success")
    return jsonify({})
