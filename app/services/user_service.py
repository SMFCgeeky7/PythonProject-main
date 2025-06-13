from app.models.usuario import User
from app.services.base_service import BaseService

class UserService(BaseService):
    def __init__(self):
        super().__init__(User)
