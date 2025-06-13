from flask import Blueprint
from app.services.category_service import CategoryService
from app.controllers.base_controller import BaseController

category_bp = Blueprint('categories', __name__)
category_service = CategoryService()

class CategoryController(BaseController):
    def __init__(self):
        super().__init__(category_service)

    @staticmethod
    @category_bp.route('', methods=['GET'])
    def get_all():
        try:
            categories = CategoryService.get_all()
            return CategoryController.success_response(
                data=[c.to_dict() for c in categories],
                message=f'Se encontraron {len(categories)} categorías'
            )
        except Exception as e:
            return CategoryController.error_response(f'Error: {str(e)}', 500)

    @staticmethod
    @category_bp.route('/<int:category_id>', methods=['GET'])
    def get_by_id(category_id):
        try:
            category = CategoryService.get_by_id(category_id)
            if not category:
                return CategoryController.error_response('Categoría no encontrada', 404)
            return CategoryController.success_response(
                data=category.to_dict(),
                message='Categoría encontrada'
            )
        except Exception as e:
            return CategoryController.error_response(f'Error: {str(e)}', 500)

category_controller = CategoryController()