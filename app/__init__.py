import os
from flask import Flask

DOWNLOADS_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = DOWNLOADS_FOLDER

    from .routes import main
    app.register_blueprint(main)

    return app
