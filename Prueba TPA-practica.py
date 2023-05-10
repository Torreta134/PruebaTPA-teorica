import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox, QGridLayout, QPushButton, QStackedLayout, QVBoxLayout, QHBoxLayout, QWidget

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1 Parte practica")
        self.setFixedSize(900, 600)

        # Crear los widgets que se van a usar
        nombre_usuario_label = QLabel("Nombre del usuario")
        imagen_label = QLabel("Icono")
        texto_descripcion_label = QLabel("Texto descriptivo del usuario")
        atributos_widgets = []
        valores_widgets = []
        for i in range(1, 7):
            atributo_label = QLabel(f"Atributo nro {i}")
            atributo_textbox = QLineEdit()
            valor_label = QLabel(f"Valor {i}")
            valor_textbox = QLineEdit()
            atributos_widgets.append((atributo_label, atributo_textbox))
            valores_widgets.append((valor_label, valor_textbox))
        ok_button = QPushButton("OK")

        # Crear los layouts que se van a usar
        atributos_layout = QGridLayout()
        for row, (atributo, valor) in enumerate(zip(atributos_widgets, valores_widgets)):
            atributos_layout.addWidget(atributo[0], row, 0)
            atributos_layout.addWidget(atributo[1], row, 1)
            atributos_layout.addWidget(valor[0], row, 2)
            atributos_layout.addWidget(valor[1], row, 3)

        formulario_layout = QVBoxLayout()
        formulario_layout.addWidget(nombre_usuario_label)
        formulario_layout.addWidget(imagen_label)
        formulario_layout.addWidget(texto_descripcion_label)
        formulario_layout.addLayout(atributos_layout)
        formulario_layout.addWidget(ok_button)

        contenedor_widget = QWidget()
        contenedor_widget.setLayout(formulario_layout)

        caja_superior_layout = QVBoxLayout()
        caja_superior_layout.addWidget(contenedor_widget)

        caja_inferior_layout = QStackedLayout()
        caja_superior_layout.addLayout(caja_inferior_layout)

        ventana_widget = QWidget()
        ventana_widget.setLayout(caja_superior_layout)
        self.setCentralWidget(ventana_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
