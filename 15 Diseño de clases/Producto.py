class Producto:
    cont_productos = 0
    
    def __init__(self, nombre, precio) -> None:
        Producto.cont_productos += 1
        self._id_producto = Producto.cont_productos
        self._nombre = nombre
        self._precio = precio
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
        
    def __str__(self) -> str:
        return f'ID: {self._id_producto} - Nombre: {self._nombre} - Precio: {self._precio}'
    
if __name__ == '__main__':
    producto1 = Producto('Camisa', 100)
    print(producto1)
    producto2 = Producto('Pantalón', 300)
    print(producto2)
    