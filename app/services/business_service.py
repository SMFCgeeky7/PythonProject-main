from app.models.Business import Business
from app.services.base_service import BaseService

class BusinessService(BaseService):
    def __init__(self):
        super().__init__(Business)