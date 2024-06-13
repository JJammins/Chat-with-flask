from pathlib import Path
from apps.config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app(config_key) :
    app = Flask(__name__)
    app.config.from_object(config[config_key])
    app.config.from_mapping(
        SECRET_KEY="wlqrktj0613wkrhtlvek",
        SQLALCHEMY_DATABASE_URI=
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY="sjanwhfflsepdpdpd189"
    )

    db.init_app(app)
    Migrate(app, db)
    csrf.init_app(app)

    from apps.chat import views as crud_views
    app.register_blueprint(crud_views.chat, url_prefix="/chat")

    return app