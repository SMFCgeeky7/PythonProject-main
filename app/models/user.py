from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db
from config import Config

class User(db.Model):
    __tablename__ = 'User'

    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(70), nullable=True)
    lastName = db.Column(db.String(70), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    address = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(13), nullable=True)
    department = db.Column(db.String(12), nullable=True)  # departamento -> state (por ser Bolivia)
    profilePhoto = db.Column(db.String(200), nullable=True)

    # Relación con Carrito (un usuario puede tener un carrito)
    carts = db.relationship('Cart', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.firstName} {self.lastName}>'

    def set_password(self, password):
        """Establecer contraseña hasheada"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verificar contraseña"""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Convertir a diccionario"""
        return {
            'userId': self.userId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'country': self.country,
            'state': self.state,
            'profilePhoto': self.profilePhoto
        }