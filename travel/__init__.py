from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app=Flask(__name__)

    app.secret_key='whatever'

    Bootstrap(app)

    from . import views
    app.register_blueprint(views.mainbp)

    from . import destinations
    app.register_blueprint(destinations.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
