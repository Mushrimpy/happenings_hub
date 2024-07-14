from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
import os

load_dotenv()
db = SQLAlchemy()
DB_NAME = os.getenv("DB_NAME")


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{DB_NAME}",
        UPLOAD_FOLDER=os.path.join(app.instance_path, os.getenv("UPLOAD_FOLDER")),
    )
    db.init_app(app)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    from .views import views_bp
    from .auth import auth_bp

    app.register_blueprint(views_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/auth/")

    from .errors import page_not_found

    app.register_error_handler(404, page_not_found)

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth_bp.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    from .models import User

    db_path = os.path.join(app.instance_path, DB_NAME)
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print("Database created")
            admin_user = User(
                username="admin", password=generate_password_hash(os.getenv("ADMIN_PW"))
            )
            db.session.add(admin_user)
            db.session.commit()
