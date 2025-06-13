from app.models.Category import Category
from app.services.base_service import BaseService

class CategoryService(BaseService):
    def __init__(self):
        super().__init__(Category)