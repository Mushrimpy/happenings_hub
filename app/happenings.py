from flask import Blueprint, render_template, jsonify, request, flash
from flask_login import login_required, current_user
from . import db
from .models import User, Activity
from .utils import CATEGORY_KEYS
from datetime import datetime


happenings_bp = Blueprint("happenings_bp", __name__)


@happenings_bp.route("/", methods=["GET", "POST"])
@login_required
def hub():
    return render_template("hub.html", user=current_user)


@happenings_bp.route("/share", methods=["GET", "POST"])
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


@happenings_bp.route("/crew", methods=["GET", "POST"])
@login_required
def crew():
    return render_template("crew.html", user=current_user)
