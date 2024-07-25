from flask import Blueprint, render_template, jsonify, request, flash
from flask_login import login_required, current_user
from .. import db
from ..models import User, Activity
from ..utils import CATEGORY_KEYS
from datetime import datetime


post_bp = Blueprint(
    "post_bp",
    __name__,
    template_folder="templates",
)


@post_bp.route("/share", methods=["GET", "POST"])
@login_required
def share():
    if request.method == "POST":
        form_data = request.form.to_dict()
        for key in form_data:
            if not form_data[key]:
                form_data[key] = None
            new_entry = Activity(
                **form_data, user_id=current_user.id, timestamp=datetime.now()
            )
        db.session.add(new_entry)
        db.session.commit()
        flash("Activity shared successfully", category="success")
        print(new_entry.longitude)
        print(new_entry.is_goal)

    return render_template("share.html", user=current_user, categories=CATEGORY_KEYS)


@post_bp.route("/review", methods=["GET", "POST"])
@login_required
def review():
    return render_template("review.html", user=current_user)
