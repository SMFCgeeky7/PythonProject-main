from app.models.User import User
from app.services.base_service import BaseService
from app import db

class NoteService(BaseService):
    """Servicio para operaciones específicas de User"""

    def __init__(self):
        super().__init__(User)

    @staticmethod
    def get_all():
        """Obtener todas las notas"""
        return Note.query.all()

    @staticmethod
    def get_by_id(user_id):
        """Obtener nota por ID"""
        return Note.query.get(user_id)