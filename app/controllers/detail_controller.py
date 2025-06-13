from flask import Blueprint
from app.services.detail_service import DetailService
from app.controllers.base_controller import BaseController

detail_bp = Blueprint('details', __name__)
detail_service = DetailService()

class DetailController(BaseController):
    def __init__(self):
        super().__init__(detail_service)

    @staticmethod
    @detail_bp.route('', methods=['GET'])
    def get_all():
        try:
            details = DetailService.get_all()
            return DetailController.success_response(
                data=[d.to_dict() for d in details],
                message=f'Se encontraron {len(details)} detalles'
            )
        except Exception as e:
            return DetailController.error_response(f'Error: {str(e)}', 500)

    @staticmethod
    @detail_bp.route('/<int:detail_id>', methods=['GET'])
    def get_by_id(detail_id):
        try:
            detail = DetailService.get_by_id(detail_id)
            if not detail:
                return DetailController.error_response('Detalle no encontrado', 404)
            return DetailController.success_response(
                data=detail.to_dict(),
                message='Detalle encontrado'
            )
        except Exception as e:
            return DetailController.error_response(f'Error: {str(e)}', 500)

detail_controller = DetailController()