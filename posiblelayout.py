import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)

from PyQt5.QtGui import QPixmap
class MiVentana(QWidget):
    def __init__(self, n, lista, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.numero = n
        self.lista = lista
        self.init_GUI()
        # self.label = QLabel(self)
        # self.label.setMinimumSize(1,1)
        # self.label.setMaximumSize(50,50)

        self.mis_labels = [QLabel(self) for _ in range(self.numero[0]*self.numero[1])]
        for l in range(self.numero[1]):
            for k in range(self.numero[0]):
                #self.mis_labels[k+self.numero[0]*l].scaled(50,50)
                self.mis_labels[k+self.numero[0]*l].move(50*k,50*l) # el primero mueve por columnas
                if self.lista[k+self.numero[0]*l]=='X':
                    self.mis_labels[k + self.numero[0] * l].setPixmap(QPixmap("sprites/mapa/towerDefense_tile029.png").scaled(50,50))
                elif self.lista[k+self.numero[0]*l]=='O':
                    self.mis_labels[k+self.numero[0]*l].setPixmap(QPixmap("sprites/mapa/towerDefense_tile024.png").scaled(50,50))
                elif self.lista[k+self.numero[0]*l]=='C':
                    self.mis_labels[k + self.numero[0] * l].setPixmap(QPixmap("sprites/mapa/towerDefense_tile055.png").scaled(50, 50))
                #elif k<(self.numero[0]-1) and self.lista[k + self.numero[0] * (l+1)] == 'O' and self.lista[k+self.numero[0]*l]=='C':
                #    self.mis_labels[k + self.numero[0] * l].setPixmap(QPixmap("sprites/mapa/towerDefense_tile001.png").scaled(50,50))
                #elif l>=1 and self.lista[k-1 + self.numero[0] * l] == 'O' and self.lista[k+self.numero[0]*l]=='C':
                #    self.mis_labels[k + self.numero[0] * l].setPixmap(QPixmap("sprites/mapa/towerDefense_tile025.png").scaled(50,50))
                #elif l<(self.numero[1]-1) and self.lista[k+1 + self.numero[0] * l] == 'O' and self.lista[k+self.numero[0]*l]=='C':
                #    self.mis_labels[k + self.numero[0] * l].setPixmap(QPixmap("sprites/mapa/towerDefense_tile023.png").scaled(50,50))

        for l in range(self.numero[1]):
            for k in range(self.numero[0]):
                if self.lista[k+self.numero[0]*l]=='B':
                    #self.mis_labels[k + self.numero[0] * l].setMaximumSize(100, 100)
                    self.mis_labels[k + self.numero[0] * l].move(50 * k, 50 * l)
                    self.mis_labels[k + self.numero[0] * l].setPixmap(QPixmap("sprites/pinguino/base.png").scaled(100,100))
                    break
            else:
                continue
            break
        self.mis_labels[k + self.numero[0] * l].show()
        #self.label.setPixmap(QPixmap("sprites/mapa/towerDefense_tile024.png"))
        #self.label.show()



    def init_GUI(self):
        """
        Este método configura todos los widgets de la ventana.
        """
        self.setGeometry(100, 100, 50*self.numero[0], 50*self.numero[1]) #[0] es el ancho, [1] es el largo
        #self.setGeometry(100, 100, 1000, 500)  # [0] es el ancho, [1] es el largo


if __name__ == '__main__':
    lista = []
    with open("./mapas/mapa_1.txt", encoding="utf-8") as archivo:
        j = 0
        for line in archivo:
            j += 1
            i = 0
            for character in line.strip("\n").split(" "):
                lista.append(character)
                i += 1
    app = QApplication([])
    n = (i,j)
    form = MiVentana(n, lista)
    form.show()
    sys.exit(app.exec_())