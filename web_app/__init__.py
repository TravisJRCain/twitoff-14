# web_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

from .routes.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.stats_routes import stats_routes

load_dotenv()

# DataBase File Path
DATABASE_URL = os.getenv("DATABASE_URL") # using absolute filepath
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")


# Instiailizing the app inside of a function
def create_app():
    app = Flask(__name__)

    # Configures the DataBase
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initializes the DataBase
    db.init_app(app)
    print(db)
    # Migrates the app and DataBase
    migrate.init_app(app, db)

    # Registering the blueprints for the different app routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(stats_routes)
    return app



if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)