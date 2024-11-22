class Factura:
    def __init__(self, fecha: str):
        self.fecha = fecha
        self.productos = []  # Lista de productos en la factura
        self.valor_total = 0.0

    def agregar_producto(self, producto):
        """Agrega un producto a la factura."""
        self.productos.append(producto)
        self.valor_total += producto.precio

    def calcular_total(self):
        """Calcula el valor total de la factura."""
        self.valor_total = sum(producto.precio for producto in self.productos)
        return self.valor_total
