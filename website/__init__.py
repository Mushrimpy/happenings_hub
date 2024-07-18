from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
import os

db = SQLAlchemy()

def create_app(config_class="config.Config"):

    app = Flask(__name__)
    app.config.from_object(config_class)  # Load configuration

    # Configure upload folder
    app.config["UPLOAD_FOLDER"] = os.path.join(
        app.instance_path, app.config["UPLOAD_FOLDER"]
    )
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register blueprints
    from .views import views_bp
    from .auth import auth_bp
    from .friends import friends_bp

    app.register_blueprint(views_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/auth/")
    app.register_blueprint(friends_bp, url_prefix="/friends/")

    # Register error handlers
    from .errors import page_not_found

    app.register_error_handler(404, page_not_found)

    # Initialize database
    from .models import User, Activity, FriendRequest

    create_database(app)

    # Initialize LoginManager
    login_manager = LoginManager()
    login_manager.login_view = "auth_bp.login"
    login_manager.init_app(app)

    # User loader function
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    from .models import User

    db_path = os.path.join(app.instance_path, app.config["DB_NAME"])
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print("Database created")
            admin_user = User(
                username="admin",
                password=generate_password_hash(app.config["ADMIN_PW"]),
            )
            print(f"ADMIN_PW loaded from config: {app.config["ADMIN_PW"]}")
            db.session.add(admin_user)
            db.session.commit()
