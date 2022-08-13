import sys
from turtle import position
import celestialBody
from vector2d import vector2d
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

pos = vector2d(0, 0)
spd = vector2d(0, 0)
mass = 1,0
radius = 10

bodies = []

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.spbMass.valueChanged.connect(self.mass_changed)
        self.ui.spbRadius.valueChanged.connect(self.radius_changed)
        self.ui.spbPosX.valueChanged.connect(self.pos_x_changed)
        self.ui.spbPosY.valueChanged.connect(self.pos_y_changed)
        self.ui.spbSpdX.valueChanged.connect(self.spd_x_changed)
        self.ui.spbSpdY.valueChanged.connect(self.spd_y_changed)

        self.ui.btnNew.clicked.connect(
            lambda: bodies.append(
                celestialBody(
                    position=pos,
                    speed=spd,
                    mass=mass,
                    radius=radius
                )
            )
        )

    def pos_x_changed(self, value):
        global pos
        pos.x = float(value)
        pos.updateLen()

    def pos_y_changed(self, value):
        global pos
        pos.y = float(value)
        pos.updateLen()

    def spd_x_changed(self, value):
        global spd
        spd.x = float(value)
        spd.updateLen()

    def spd_y_changed(self, value):
        global spd
        pos.x = float(value)
        pos.updateLen()

    def mass_changed(self, value):
        global mass
        mass = float(value)

    def radius_changed(self, value):
        global radius
        radius = value

    def createBody(self, pos, spd, mas, rad):
        pass
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())