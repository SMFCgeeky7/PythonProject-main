from app.models.Cart import Cart
from app.services.base_service import BaseService

class CartService(BaseService):
    def __init__(self):
        super().__init__(Cart)
