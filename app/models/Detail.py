from app import db

class Detail(db.Model):
    __tablename__ = 'Detail'

    detailId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productQuantity = db.Column(db.Integer, nullable=False)
    unitPrice = db.Column(db.Numeric(5, 2), nullable=False)
    subTotalDetail = db.Column(db.Numeric(5, 2), nullable=False)
    cartId = db.Column(db.Integer, db.ForeignKey('Cart.cartId'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('Product.productId'), nullable=False)

    # Relaciones
    cart = db.relationship('Cart', backref=db.backref('details', lazy=True))
    product = db.relationship('Product', backref=db.backref('details', lazy=True))

    def to_dict(self):
        return {
            'detailId': self.detailId,
            'productQuantity': self.productQuantity,
            'unitPrice': float(self.unitPrice),
            'subTotalDetail': float(self.subTotalDetail),
            'cartId': self.cartId,
            'productId': self.productId
        }