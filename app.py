import sys
import configparser as cp
from time import sleep
from celestialBody import CelestialBody
from drawer import drawFrame
from vector2d import Vector2D
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from ui_mainwindow import Ui_MainWindow
from threading import Condition, Thread

config = cp.ConfigParser()
config.read('config.ini')
selectedRow = 0
bodies = {}

def getMinFreeIndex():
    global bodies
    keys = list(bodies.keys())

    if len(list(bodies.keys())) == 0:
        return 1

    for i in range(len(keys)):
        keys[i] = int(keys[i].split(' ')[1])

    max_key = max(keys)

    for i in range(1, max_key):
        if i not in keys:
            return i
    return max_key + 1

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnNew.clicked.connect(self.createBody)
        self.ui.btnDelete.clicked.connect(self.deleteBody)
        self.ui.btnCopy.clicked.connect(self.copyBody)
        self.ui.btnSimStep.clicked.connect(self.simStep)
        self.ui.btnSimStart.clicked.connect(self.simStart)
        self.ui.btnSimStop.clicked.connect(self.simStop)

        self.timerThread = Thread(target=self.timerCycle(), args=())
        self.simThread = Thread(target=self.simCycle(), args=())

        self.doSimCycle = False
        self.drawReady = Condition()
        self.drawDelay = 1/30

    def createBody(self):
        name = f"Тело {getMinFreeIndex()}"
        bodies[name] = CelestialBody(
            position=Vector2D(
                x=self.ui.spbPosX.value() + 305,
                y=self.ui.spbPosY.value()+ 305
            ),
            speed=Vector2D(
                x=self.ui.spbSpdX.value(),
                y=self.ui.spbSpdY.value()
            ),
            mass=self.ui.spbMass.value() * int(config['CONSTANTS']['mass_mult']),
            radius=self.ui.spbRadius.value()
        )
        self.ui.lstBodies.addItem(name)

        

    def deleteBody(self):
        global selectedRow
        name = self.ui.lstBodies.currentItem().text()
        del bodies[name]
        self.ui.lstBodies.takeItem(selectedRow)

    def copyBody(self):
        original = bodies[self.ui.lstBodies.currentItem().text()]
        name = f"Тело {getMinFreeIndex()}"
        bodies[name] = CelestialBody(
            position=original.position,
            speed=original.speed,
            mass=original.mass,
            radius=original.radius
        )
        self.ui.lstBodies.addItem(name)

    def simStep(self):
        indexes = []

        for key in list(bodies.keys()):
            indexes.append(key.split()[1])

        drawFrame(
            bodies=list(bodies.values()),
            indexes=indexes,
            drawTrails=self.ui.cbxDrawTrails.isChecked(),
            drawVectors=self.ui.cbxDrawSpdVects.isChecked()
        )

        frame = QImage('frame.jpg')
        pixmap = QPixmap(frame)
        self.ui.lblSimulationDisplay.setPixmap(pixmap)

    

    def timerCycle(self):
        try:
            self.drawDelay = 1 / 30
        except ZeroDivisionError:
            self.drawDelay = 1
        
        while self.doSimCycle:
            self.drawReady.notify()
            sleep(self.drawDelay)

    def simCycle(self):
        while self.doSimCycle:
            self.drawReady.wait()
            self.simStep()



    def simStart(self):

        self.ui.gpbBodies.setEnabled(False)
        self.ui.gpbEdit.setEnabled(False)
        self.ui.gpbSettings.setEnabled(False)
        self.ui.btnSimStop.setEnabled(True)

        self.doSimCycle = True
        self.simThread.start()
        self.timerThread.start()

    def simStop(self):

        self.ui.gpbBodies.setEnabled(True)
        self.ui.gpbEdit.setEnabled(True)
        self.ui.gpbSettings.setEnabled(True)

        self.doSimCycle = False
        self.simThread.join()
        self.timerThread.join()


def setup():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    mainThread = Thread(target=setup(), args=())
    mainThread.start()