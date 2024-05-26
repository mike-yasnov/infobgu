from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    jwt = JWTManager(app)
    jwt.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    with app.app_context():
        # Импортируйте и зарегистрируйте Blueprint
        from .auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/api/auth')

        from .schedule import schedule_bp
        app.register_blueprint(schedule_bp, url_prefix='/api/schedule')
        # Создайте все таблицы
        db.create_all()

    return app
