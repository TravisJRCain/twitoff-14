# web_app/__init__.py

from flask import Flask

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.tweet_routes import tweet_routes

# DataBase File Path
DATABASE_URI = "sqlite:///twitter_flask_app_db.db" # using relative filepath


# Instiailizing the app inside of a function
def create_app():
    app = Flask(__name__)

    # Configures the DataBase
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    # Initializes the DataBase
    db.init_app(app)
    # Migrates the app and DataBase
    migrate.init_app(app, db)

    # Registering the blueprints for the different app routes
    app.register_blueprint(home_routes)
    app.register_blueprint(tweet_routes)
    
    return app





# Factory pattern; Flask best practice
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)