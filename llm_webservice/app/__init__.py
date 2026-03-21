# app/__init__.py
from flask import Flask
from flask_cors import CORS
from .setup_db import init_db
from .routes import main_routes
from .qwen import Qwen

# Initialize shared objects here so they aren't recreated per request
qwen_instance = Qwen()

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"])

    # register routes
    app.register_blueprint(main_routes)

    # store shared objects in app context if needed
    app.qwen = qwen_instance
    try:
        app.db_manager = init_db()
    except Exception as e:
        print(f"DB initialization failed: {e}")
        app.db_manager = None

    return app