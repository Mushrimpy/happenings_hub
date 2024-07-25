from flask import Blueprint, render_template, jsonify, request, flash
from flask_login import login_required, current_user
from .. import db
from ..models import User, Activity
from datetime import datetime


home_bp = Blueprint(
    "home_bp",
    __name__,
    template_folder="templates",
)


@home_bp.route("/", methods=["GET", "POST"])
@login_required
def hub():
    return render_template("hub.html", user=current_user)


@home_bp.route("/crew", methods=["GET", "POST"])
@login_required
def crew():
    return render_template("crew.html", user=current_user)
