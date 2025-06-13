from app import db

class Product(db.Model):
    __tablename__ = 'Product'

    productId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productName = db.Column(db.String(255), nullable=False)
    productDescription = db.Column(db.Text)
    price = db.Column(db.Numeric(5, 2), nullable=False)
    availability = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Numeric(5, 2))
    productImage = db.Column(db.String(255))
    additionalImages = db.Column(db.String(255))
    timesAddedToCart = db.Column(db.Integer, default=0)
    categoryId = db.Column(db.Integer, db.ForeignKey('Category.categoryId'))

    # Relación con Detail
    details = db.relationship('Detail', backref='product', lazy=True)

    def to_dict(self):
        return {
            'productId': self.productId,
            'productName': self.productName,
            'productDescription': self.productDescription,
            'price': float(self.price),
            'availability': self.availability,
            'discount': float(self.discount) if self.discount else None,
            'productImage': self.productImage,
            'additionalImages': self.additionalImages,
            'timesAddedToCart': self.timesAddedToCart,
            'categoryId': self.categoryId
        }