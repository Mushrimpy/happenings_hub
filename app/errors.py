from flask import render_template
from flask_login import current_user


def page_not_found(error):
    return render_template("404.html", user=current_user), 404
