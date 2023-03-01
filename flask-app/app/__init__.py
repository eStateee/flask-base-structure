from flask import Flask
from config import Config
from app.extensions import db


def create_app(config_class=Config):
    # Initialize flask app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    # Test route (delete after testing)
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    # Return app
    return app
