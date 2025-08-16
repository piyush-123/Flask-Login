
from flask import Flask
from .extensions import db,migrate,login_manager,bcrypt
from .auth.routes import  auth_bp
from .main.routes import main_bp
from .models import User


def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    return app