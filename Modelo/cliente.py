class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.facturas = []  # Lista para almacenar las facturas del cliente

    def agregar_factura(self, factura):
        """Agrega una factura al historial del cliente."""
        self.facturas.append(factura)

    def listar_facturas(self):
        """Retorna todas las facturas asociadas al cliente."""
        return self.facturas
