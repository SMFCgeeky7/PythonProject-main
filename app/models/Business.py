from app import db

class Business(db.Model):
    __tablename__ = 'Business'

    businessId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    businessName = db.Column(db.String(70), nullable=False)
    businessCategory = db.Column(db.String(50), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    userId = db.Column(db.Integer, db.ForeignKey('User.userId'), nullable=False)

    # Relación con User
    user = db.relationship('User', backref=db.backref('businesses', lazy=True))

    def to_dict(self):
        return {
            'businessId': self.businessId,
            'businessName': self.businessName,
            'businessCategory': self.businessCategory,
            'location': self.location,
            'phone': self.phone,
            'userId': self.userId
        }