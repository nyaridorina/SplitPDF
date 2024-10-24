import os
from flask import Flask

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')

# Check if the folder exists before creating it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from .routes import main
    app.register_blueprint(main)

    return app
