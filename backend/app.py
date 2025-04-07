from flask import Flask
from flask_cors import CORS
from models.db.exercise1 import db, Exercise1
from models.db.exercise2 import db, Exercise2
from models.db import db, create_exercise1_table
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        create_exercise1_table()

    from routes.exercise1 import exercise1_bp
    from routes.exercise2 import exercise2_bp

    app.register_blueprint(exercise1_bp, url_prefix='/exercise1')
    app.register_blueprint(exercise2_bp, url_prefix='/exercise2')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)