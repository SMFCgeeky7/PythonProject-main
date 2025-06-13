from flask import Blueprint, request, g
from app.services.producto_service import ProductoService
from app.controllers.base_controller import BaseController
from app.utils.auth_decorators import token_required, admin_required

producto_bp = Blueprint('productos', __name__)
producto_service = ProductoService()

class ProductoController(BaseController):
    """Controlador para operaciones de Producto"""

    def __init__(self):
        super().__init__(producto_service)

    @staticmethod
    @producto_bp.route('', methods=['GET'])
    def get_all():
        """Obtener todos los productos"""
        try:
            productos = ProductoService.get_all()
            return ProductoController.success_response(
                data=[producto.to_dict() for producto in productos],
                message=f'Se encontraron {len(productos)} productos'
            )
        except Exception as e:
            return ProductoController.error_response(f'Error al obtener productos: {str(e)}', 500)

    @staticmethod
    @producto_bp.route('/<int:producto_id>', methods=['GET'])
    def get_by_id(producto_id):
        """Obtener producto por ID"""
        try:
            producto = ProductoService.get_by_id(producto_id)
            if not producto:
                return ProductoController.error_response('Producto no encontrado', 404)

            return ProductoController.success_response(
                data=producto.to_dict(),
                message='Producto encontrado'
            )
        except Exception as e:
            return ProductoController.error_response(f'Error al obtener producto: {str(e)}', 500)

    @staticmethod
    @producto_bp.route('', methods=['POST'])
    @token_required
    @admin_required
    def create():
        """Crear nuevo producto (solo admin)"""
        try:
            data = request.get_json()

            if not data:
                return ProductoController.error_response('Datos JSON requeridos', 400)

            # Validar campos requeridos
            required_fields = ['nombreProducto', 'precio', 'disponibilidad']
            missing_fields = [field for field in required_fields if not data.get(field)]

            if missing_fields:
                return ProductoController.error_response(
                    f'Campos requeridos: {", ".join(missing_fields)}', 400
                )

            producto = ProductoService.create(data)
            return ProductoController.success_response(
                data=producto.to_dict(),
                message='Producto creado exitosamente',
                status_code=201
            )
        except ValueError as e:
            return ProductoController.error_response(str(e), 400)
        except Exception as e:
            return ProductoController.error_response(f'Error al crear producto: {str(e)}', 500)

    @staticmethod
    @producto_bp.route('/<int:producto_id>', methods=['PUT'])
    @token_required
    @admin_required
    def update(producto_id):
        """Actualizar producto (solo admin)"""
        try:
            data = request.get_json()

            if not data:
                return ProductoController.error_response('Datos JSON requeridos', 400)

            producto = ProductoService.update(producto_id, data)
            if not producto:
                return ProductoController.error_response('Producto no encontrado', 404)

            return ProductoController.success_response(
                data=producto.to_dict(),
                message='Producto actualizado exitosamente'
            )
        except ValueError as e:
            return ProductoController.error_response(str(e), 400)
        except Exception as e:
            return ProductoController.error_response(f'Error al actualizar producto: {str(e)}', 500)

    @staticmethod
    @producto_bp.route('/<int:producto_id>', methods=['DELETE'])
    @token_required
    @admin_required
    def delete(producto_id):
        """Eliminar producto (solo admin)"""
        try:
            success = ProductoService.delete(producto_id)
            if not success:
                return ProductoController.error_response('Producto no encontrado', 404)

            return ProductoController.success_response(
                message='Producto eliminado exitosamente'
            )
        except Exception as e:
            return ProductoController.error_response(f'Error al eliminar producto: {str(e)}', 500)

producto_controller = ProductoController()