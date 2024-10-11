from flask import Flask
from app.routes import main  # Assuming your routes are defined in routes.py in the app folder
from app import db

def create_app():
    app = Flask(__name__)
    
    # Configure your app (e.g., database URI, etc.)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Register the blueprint
    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
