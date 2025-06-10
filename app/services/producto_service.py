from app.models.Producto import Producto
from app.services.base_service import BaseService
from app import db

class ProductoService(BaseService):
    """Servicio para operaciones específicas de Producto"""

    def __init__(self):
        super().__init__(Producto)

    @staticmethod
    def get_all():
        """Obtener todos los productos"""
        return Producto.query.all()

    @staticmethod
    def get_by_id(producto_id):
        """Obtener producto por ID"""
        return Producto.query.get(producto_id)

    @staticmethod
    def delete(producto_id):
        """Eliminar producto"""
        try:
            producto = Producto.query.get(producto_id)
            if not producto:
                return False

            db.session.delete(producto)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def create(data):
        """Crear nuevo producto con validaciones"""
        # Validar campos requeridos
        required_fields = ['nombreProducto', 'precio', 'disponibilidad']
        for field in required_fields:
            if not data.get(field):
                raise ValueError(f'El campo {field} es requerido')

        # Validar precio
        try:
            precio = float(data.get('precio'))
            if precio <= 0:
                raise ValueError('El precio debe ser mayor a 0')
        except ValueError:
            raise ValueError('El precio debe ser un número válido')

        # Validar disponibilidad
        try:
            disponibilidad = int(data.get('disponibilidad'))
            if disponibilidad < 0:
                raise ValueError('La disponibilidad no puede ser negativa')
        except ValueError:
            raise ValueError('La disponibilidad debe ser un número entero')

        # Crear producto
        producto = Producto(
            nombreProducto=data.get('nombreProducto').strip(),
            descripcionProducto=data.get('descripcionProducto'),
            precio=precio,
            disponibilidad=disponibilidad,
            descuento=data.get('descuento'),
            imagenProductoPrincipal=data.get('imagenProductoPrincipal'),
            imagenProductoAdicionales=data.get('imagenProductoAdicionales'),
            vecesGuardadoEnCarrito=0,
            idCategoria=data.get('idCategoria')
        )

        db.session.add(producto)
        db.session.commit()

        return producto

    @staticmethod
    def update(producto_id, data):
        """Actualizar producto"""
        producto = Producto.query.get(producto_id)
        if not producto:
            return None

        # Campos que se pueden actualizar
        updatable_fields = [
            'nombreProducto', 'descripcionProducto', 'precio', 
            'disponibilidad', 'descuento', 'imagenProductoPrincipal',
            'imagenProductoAdicionales', 'idCategoria'
        ]

        for field in updatable_fields:
            if field in data:
                if field == 'precio':
                    try:
                        precio = float(data[field])
                        if precio <= 0:
                            raise ValueError('El precio debe ser mayor a 0')
                        setattr(producto, field, precio)
                    except ValueError:
                        raise ValueError('El precio debe ser un número válido')

                elif field == 'disponibilidad':
                    try:
                        disponibilidad = int(data[field])
                        if disponibilidad < 0:
                            raise ValueError('La disponibilidad no puede ser negativa')
                        setattr(producto, field, disponibilidad)
                    except ValueError:
                        raise ValueError('La disponibilidad debe ser un número entero')

                elif field == 'descuento':
                    if data[field] is not None:
                        try:
                            descuento = float(data[field])
                            if descuento < 0 or descuento > 100:
                                raise ValueError('El descuento debe estar entre 0 y 100')
                            setattr(producto, field, descuento)
                        except ValueError:
                            raise ValueError('El descuento debe ser un número válido')

                else:
                    setattr(producto, field, data[field])

        db.session.commit()
        return producto

    @staticmethod
    def get_by_categoria(categoria_id):
        """Obtener productos por categoría"""
        return Producto.query.filter_by(idCategoria=categoria_id).all()

    @staticmethod
    def get_productos_disponibles():
        """Obtener solo productos con disponibilidad > 0"""
        return Producto.query.filter(Producto.disponibilidad > 0).all()

    @staticmethod
    def get_productos_con_descuento():
        """Obtener productos con descuento"""
        return Producto.query.filter(Producto.descuento > 0).all()

    def validate_producto_data(self, data, is_update=False):
        """Validar datos del producto"""
        errors = []

        if not is_update or 'nombreProducto' in data:
            if not data.get('nombreProducto'):
                errors.append("El nombre del producto es requerido")

        if not is_update or 'precio' in data:
            try:
                precio = float(data.get('precio', 0))
                if precio <= 0:
                    errors.append("El precio debe ser mayor a 0")
            except ValueError:
                errors.append("El precio debe ser un número válido")

        return errors