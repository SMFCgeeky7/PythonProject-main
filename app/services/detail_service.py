from app.models.Detail import Detail
from app.services.base_service import BaseService

class DetalleService(BaseService):
    def __init__(self):
        super().__init__(Detail)