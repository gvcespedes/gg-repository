import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.init_GUI()

    def init_GUI(self):
        """
        Este método configura todos los widgets de la ventana.
        """
        self.setGeometry(100, 100, 400, 400)
        self.label1 = QLabel('Nombre jugador:', self) #mensajito antes de barrita blanca
        self.label1.move(10, 15)
        self.label2 = QLabel('Bando con el que desea jugar:', self)
        self.label2.move(10, 15)
        self.label3 = QLabel('Puntaje histórico:', self)
        self.label3.move(10, 15)
        self.edit1 = QLineEdit('', self) #barrita blanca para escribir
        self.edit1.setGeometry(45, 15, 100, 20)
        self.boton1 = QPushButton('Gatos', self)
        self.boton1.setGeometry(45, 15, 100, 20)
        self.boton2 = QPushButton('Pinguinos', self)
        self.boton2.setGeometry(45, 15, 100, 20)
        self.boton3 = QPushButton('Empezar', self) #botón que dice empezar
        self.boton3.resize(self.boton3.sizeHint())

        """
        Creamos el layout horizontal y agregamos los widgets mediante el
        método addWidget(). El método addStretch() nos permite incluir
        opcionalmente espaciadores.
        """
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.edit1)
        hbox.addStretch(1)

        h2box = QHBoxLayout()
        h2box.addStretch(1)
        h2box.addWidget(self.label2)
        h2box.addWidget(self.boton1)
        h2box.addWidget(self.boton2)
        h2box.addStretch(1)

        h3box = QHBoxLayout()
        h3box.addStretch(1)
        h3box.addWidget(self.label3)
        h3box.addStretch(1)

        h4box = QHBoxLayout()
        h4box.addStretch(1)
        h4box.addWidget(self.boton3)
        h4box.addStretch(1)


        """
        Creamos el layout vertical y le agregamos el layout horizontal.
        Opcionalmente agregamos espaciadores para distribuir los widgets.
        Notar el juego entre el valor recibido por los espaciadores.
        """
        vbox = QVBoxLayout()
        vbox.addStretch(5)
        vbox.addLayout(hbox)
        vbox.addLayout(h2box)
        vbox.addLayout(h3box)
        vbox.addLayout(h4box)
        vbox.addStretch(1)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_())
