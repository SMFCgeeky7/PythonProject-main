from flask import Blueprint
from app.services.cart_service import CartService
from app.controllers.base_controller import BaseController

cart_bp = Blueprint('carts', __name__)
cart_service = CartService()

class CartController(BaseController):
    def __init__(self):
        super().__init__(cart_service)

    @staticmethod
    @cart_bp.route('', methods=['GET'])
    def get_all():
        try:
            carts = CartService.get_all()
            return CartController.success_response(
                data=[c.to_dict() for c in carts],
                message=f'Se encontraron {len(carts)} carritos'
            )
        except Exception as e:
            return CartController.error_response(f'Error: {str(e)}', 500)

    @staticmethod
    @cart_bp.route('/<int:cart_id>', methods=['GET'])
    def get_by_id(cart_id):
        try:
            cart = CartService.get_by_id(cart_id)
            if not cart:
                return CartController.error_response('Carrito no encontrado', 404)
            return CartController.success_response(
                data=cart.to_dict(),
                message='Carrito encontrado'
            )
        except Exception as e:
            return CartController.error_response(f'Error: {str(e)}', 500)

cart_controller = CartController()