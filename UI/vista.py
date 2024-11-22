from PyQt5 import QtWidgets, QtCore
from controlador.controlador import Controlador


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicialización del controlador
        self.controlador = Controlador()

        # Configuración de la ventana principal
        self.setWindowTitle("Tienda de Productos Agrícolas")
        self.resize(800, 600)

        # Widgets principales
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.layout_principal = QtWidgets.QVBoxLayout(self.central_widget)

        # Sección para registrar clientes
        self.seccion_registro_clientes = QtWidgets.QGroupBox("Registrar Cliente")
        self.layout_principal.addWidget(self.seccion_registro_clientes)
        self.layout_clientes = QtWidgets.QFormLayout(self.seccion_registro_clientes)

        self.nombre_cliente = QtWidgets.QLineEdit()
        self.layout_clientes.addRow("Nombre:", self.nombre_cliente)

        self.cedula_cliente = QtWidgets.QLineEdit()
        self.layout_clientes.addRow("Cédula:", self.cedula_cliente)

        self.boton_agregar_cliente = QtWidgets.QPushButton("Agregar Cliente")
        self.layout_clientes.addWidget(self.boton_agregar_cliente)

        # Conexión del botón "Agregar Cliente"
        self.boton_agregar_cliente.clicked.connect(self.agregar_cliente)

        # Sección para listar facturas
        self.seccion_facturas = QtWidgets.QGroupBox("Facturas del Cliente")
        self.layout_principal.addWidget(self.seccion_facturas)
        self.layout_facturas = QtWidgets.QVBoxLayout(self.seccion_facturas)

        self.selector_cliente = QtWidgets.QComboBox()
        self.layout_facturas.addWidget(self.selector_cliente)

        self.boton_ver_facturas = QtWidgets.QPushButton("Ver Facturas")
        self.layout_facturas.addWidget(self.boton_ver_facturas)

        self.tabla_facturas = QtWidgets.QTableWidget()
        self.tabla_facturas.setColumnCount(3)
        self.tabla_facturas.setHorizontalHeaderLabels(["Fecha", "Productos", "Valor Total"])
        self.layout_facturas.addWidget(self.tabla_facturas)

        # Conexión del botón "Ver Facturas"
        self.boton_ver_facturas.clicked.connect(self.ver_facturas)

    def agregar_cliente(self):
        """Agrega un cliente al sistema."""
        nombre = self.nombre_cliente.text()
        cedula = self.cedula_cliente.text()

        if not nombre or not cedula:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Debe llenar todos los campos.")
            return

        mensaje = self.controlador.agregar_cliente(nombre, cedula)
        QtWidgets.QMessageBox.information(self, "Información", mensaje)
        self.actualizar_lista_clientes()

    def actualizar_lista_clientes(self):
        """Actualiza el ComboBox con los clientes registrados."""
        self.selector_cliente.clear()
        for cedula in self.controlador.obtener_cedulas_clientes():
            self.selector_cliente.addItem(cedula)

    def ver_facturas(self):
        """Muestra las facturas del cliente seleccionado en la tabla."""
        cedula = self.selector_cliente.currentText()

        if not cedula:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay clientes registrados.")
            return

        cliente = self.controlador.obtener_cliente(cedula)
        if not cliente:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No se encontró el cliente.")
            return

        facturas = cliente.listar_facturas()
        self.tabla_facturas.setRowCount(len(facturas))  # Ajusta el número de filas según las facturas

        for fila, factura in enumerate(facturas):
            self.tabla_facturas.setItem(fila, 0, QtWidgets.QTableWidgetItem(factura.fecha))
            productos = ", ".join([p.nombre for p in factura.productos])
            self.tabla_facturas.setItem(fila, 1, QtWidgets.QTableWidgetItem(productos))
            self.tabla_facturas.setItem(fila, 2, QtWidgets.QTableWidgetItem(f"${factura.valor_total:.2f}"))

        QtWidgets.QMessageBox.information(self, "Facturas", f"Se encontraron {len(facturas)} facturas.")
