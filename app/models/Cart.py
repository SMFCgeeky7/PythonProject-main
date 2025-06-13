from app import db

class Cart(db.Model):
    __tablename__ = 'Cart'

    cartId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subtotal = db.Column(db.Numeric(5, 2), nullable=False)
    total = db.Column(db.Numeric(5, 2), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('User.userId'), nullable=False)

    # Relación opcional (si tenés el modelo User)
    user = db.relationship('User', backref=db.backref('carts', lazy=True))

    def to_dict(self):
        return {
            'cartId': self.cartId,
            'subtotal': float(self.subtotal),
            'total': float(self.total),
            'userId': self.userId
        }