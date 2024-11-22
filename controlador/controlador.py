from Modelo.cliente import Cliente
from Modelo.factura import Factura

class Controlador:
    def __init__(self):
        self.clientes = {} 

    def agregar_cliente(self, nombre, cedula):
        if cedula in self.clientes:
            return f"El cliente con cédula {cedula} ya existe."
        cliente = Cliente(nombre, cedula)
        self.clientes[cedula] = cliente
        return f"Cliente {nombre} agregado exitosamente."

    def obtener_cliente(self, cedula):
        return self.clientes.get(cedula, None)

    def agregar_factura(self, cedula, factura):
        cliente = self.obtener_cliente(cedula)
        if cliente:
            cliente.agregar_factura(factura)
            return f"Factura agregada al cliente {cliente.nombre}."
        return f"No se encontró un cliente con cédula {cedula}."
