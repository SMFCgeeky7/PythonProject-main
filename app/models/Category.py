from app import db

class Category(db.Model):
    __tablename__ = 'Category'

    categoryId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoryName = db.Column(db.String(50), nullable=False)
    categoryImage = db.Column(db.String(255), nullable=True)

    # Relación con Product
    products = db.relationship('Product', backref='category', lazy=True)

    def to_dict(self):
        return {
            'categoryId': self.categoryId,
            'categoryName': self.categoryName,
            'categoryImage': self.categoryImage
        }