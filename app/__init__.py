from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Registrar blueprints existentes
    from app.controllers.user_controller import user_bp
    from app.controllers.note_controller import note_bp
    from app.controllers.auth_controller import auth_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(note_bp, url_prefix='/api/notes')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # Registrar blueprints NUEVOS (solo GET)
    from app.controllers.cart_controller import cart_bp
    from app.controllers.category_controller import category_bp
    from app.controllers.detail_controller import detail_bp
    from app.controllers.business_controller import business_controller_bp
    from app.controllers.product_controller import product_bp
    from app.controllers.user_controller import user_bp

    app.register_blueprint(cart_bp, url_prefix='/api/cart')
    app.register_blueprint(category_bp, url_prefix='/api/category')
    app.register_blueprint(detail_bp, url_prefix='/api/detail')
    app.register_blueprint(business_bp, url_prefix='/api/business')
    app.register_blueprint(product_bp, url_prefix='/api/product')
    app.register_blueprint(user_bp, url_prefix='/api/user')

    return app
