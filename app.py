import os

from flask import Flask
from flask_migrate import Migrate

from extensions import db
from source.views.battle import BATTLE_BLUEPRINT
from source.views.health import API_BLUEPRINT
from source.views.player import PLAYER_BLUEPRINT


def create_app(db_url: str = None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url or os.getenv("DATABASE_URL")

    db.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    app.register_blueprint(API_BLUEPRINT)
    app.register_blueprint(BATTLE_BLUEPRINT)
    app.register_blueprint(PLAYER_BLUEPRINT)
    return app


if __name__ == '__main__':
    application = create_app()
    application.run(debug=True)
