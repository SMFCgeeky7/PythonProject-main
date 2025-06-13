from app.models.Product import Product
from app.services.base_service import BaseService

class ProductoService(BaseService):
    def __init__(self):
        super().__init__(Product)