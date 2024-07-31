from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .. import db
from ..models import User, Activity
from ..utils import CATEGORY_KEYS
from datetime import datetime
import json

post_bp = Blueprint(
    "post_bp",
    __name__,
    template_folder="templates",
)


@post_bp.route("/share", methods=["GET", "POST"])
@login_required
def share():
    if request.method == "POST":
        if current_user.current_activity:
            flash("Archive current activity to proceed.", category="error")
            return render_template(
                "share.html", user=current_user, categories=CATEGORY_KEYS
            )
        form_data = request.form.to_dict()
        for key in form_data:
            if not form_data[key]:
                form_data[key] = None

        new_entry = Activity(
            **form_data, user_id=current_user.id, timestamp=datetime.now()
        )
        current_user.current_activity = new_entry
        db.session.add(new_entry)
        db.session.commit()
        flash("Activity shared successfully.", category="success")
        return redirect(url_for("post_bp.review"))

    return render_template("share.html", user=current_user, categories=CATEGORY_KEYS)


@post_bp.route("/review", methods=["GET", "POST"])
@login_required
def review():
    return render_template(
        "review.html", user=current_user, activities=current_user.activities[::-1]
    )


@post_bp.route("/archive-activity", methods=["POST"])
@login_required
def archive_activity():
    archive_req = json.loads(request.data)
    activity_id = archive_req["activity_id"]
    archiving = Activity.query.get(activity_id)
    if archiving and archiving.user_id == current_user.id:
        archiving.archived = True
        current_user.current_activity_id = None
        db.session.commit()
        flash("Activity successfully archived.", category="success")
    return jsonify({})


@post_bp.route("/delete-activity", methods=["POST"])
@login_required
def delete_activity():
    delete_req = json.loads(request.data)
    activity_id = delete_req["activity_id"]
    activity = Activity.query.get(activity_id)
    if activity and activity.user_id == current_user.id:
        db.session.delete(activity)
        db.session.commit()
        flash("Activity successfully deleted.", category="success")
    return jsonify({})
