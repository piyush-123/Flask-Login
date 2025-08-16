import os
from flask import Flask
from .extensions import db,migrate,login_manager,mail,limiter
from .auth import bp as auth_bp
from .main import bp as main_bp
from flask_talisman import Talisman


def create_app(config_path = None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')

    if config_path:
        app.config.from_pyfile(config_path)

    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    mail.init_app(app)
    limiter.init_app(app)

    csp = {
        'default-src':["self"],
        'img-src':["self","data:"],
        'script-src':["self"],
        'style-src':["self","unsafe-inline"]
    }

    Talisman(app,content_security_policy = csp,force_https=True,strict_transport_security=True)

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    app.config.update(
        
        SESSION_COOKIE_HTTPONLY = True,
        SESSION_COOKIE_SAMESITE = 'Lax',
        REMEMBER_COOKIE_HTTPONLY = True,

    )

    return app