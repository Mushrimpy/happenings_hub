from flask import Blueprint, request, flash, redirect, flash, url_for, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User
from flask_login import login_user, logout_user, current_user, login_required
from . import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views_bp.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Username does not exist', category='error')

    return render_template('login.html', user=current_user)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out", category='success')
    return redirect(url_for('auth_bp.login'))

@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
          
        user = User.query.filter_by(username=username).first()
        
        if user:
            flash('Username already exists', category='error')
        else:
            if password1 != password2:
                flash('Passwords don\'t match', category='error')                
            else:
                new_user = User(username=username, password=generate_password_hash(password1, method='pbkdf2:sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created', category='success')
                return redirect(url_for('views_bp.home'))
            
    return render_template("sign_up.html", user=current_user)