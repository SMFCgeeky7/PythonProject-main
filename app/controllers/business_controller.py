from flask import Blueprint
from app.services.business_service import BusinessService
from app.controllers.base_controller import BaseController

business_bp = Blueprint('businesses', __name__)
business_service = BusinessService()

class BusinessController(BaseController):
    def __init__(self):
        super().__init__(business_service)

    @staticmethod
@business_bp.route('', methods=['GET'])
def get_all():
    try:
        # Usa la instancia del servicio, no la clase directa
        businesses = business_service.get_all()  # business_service está inicializado arriba
        return BusinessController.success_response(
            data=[b.to_dict() for b in businesses],
            message=f'Se encontraron {len(businesses)} negocios'
        )
    except Exception as e:
        return BusinessController.error_response(f'Error: {str(e)}', 500)

    @staticmethod
    @business_bp.route('/<int:business_id>', methods=['GET'])
    def get_by_id(business_id):
        try:
            business = BusinessService.get_by_id(business_id)
            if not business:
                return BusinessController.error_response('Negocio no encontrado', 404)
            return BusinessController.success_response(
                data=business.to_dict(),
                message='Negocio encontrado'
            )
        except Exception as e:
            return BusinessController.error_response(f'Error: {str(e)}', 500)

business_controller = BusinessController()