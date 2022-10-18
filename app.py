from sys import exit, argv
from time import sleep
from threading import Condition, Thread

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QImage, QPixmap
import PySide6.QtCore as QtCore
from matplotlib import use


from celestialBody import CelestialBody
from drawer import drawframe
from vector2d import Vector2D
from ui_mainwindow import Ui_MainWindow
from logger import LogEntry
from graph_plotter import draw_x_y_graph, draw_speed_graph

selectedRow = 0
bodies = {}


def get_min_free_index():
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
        # self.log = None
        self.log = None
        self.frame_counter = None
        self.simThread = None
        self.timerThread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnNew.clicked.connect(self.create_body)
        self.ui.btnDelete.clicked.connect(self.delete_body)
        self.ui.btnCopy.clicked.connect(self.copy_body)
        self.ui.btnSimStep.clicked.connect(self.sim_step)
        self.ui.btnSimStart.clicked.connect(self.sim_start)
        self.ui.btnSimStop.clicked.connect(self.sim_stop)

        self.doSimCycle = False
        self.drawReady = Condition()
        self.drawDelay = 0.01

    def create_body(self):
        name = f"Тело {get_min_free_index()}"
        bodies[name] = CelestialBody(
            position=Vector2D(
                x=self.ui.spbPosX.value() + 305,
                y=self.ui.spbPosY.value() + 305
            ),
            speed=Vector2D(
                x=self.ui.spbSpdX.value(),
                y=self.ui.spbSpdY.value()
            ),
            mass=self.ui.spbMass.value(),
            radius=self.ui.spbRadius.value()
        )
        self.ui.lstBodies.addItem(name)

    def delete_body(self):
        global selectedRow
        name = self.ui.lstBodies.currentItem().text()
        del bodies[name]
        self.ui.lstBodies.takeItem(selectedRow)

    def copy_body(self):
        original = bodies[self.ui.lstBodies.currentItem().text()]
        name = f"Тело {get_min_free_index()}"
        bodies[name] = CelestialBody(
            position=original.position,
            speed=original.speed,
            mass=original.mass,
            radius=original.radius
        )
        self.ui.lstBodies.addItem(name)

    def sim_step(self):
        indexes = []

        for key in list(bodies.keys()):
            indexes.append(key.split()[1])

        drawframe(bodies=list(bodies.values()),
                  indexes=indexes,
                  drawvectors=self.ui.cbxDrawSpdVects.isChecked(),
                  drawtrails=self.ui.cbxDrawTrails.isChecked(),
                  frame_number=self.frame_counter,
                  log=self.log)

        frame = QImage('frame.jpg')
        pixmap = QPixmap(frame)
        self.ui.lblSimulationDisplay.setPixmap(pixmap)

        self.frame_counter += 1

    def timer_cycle(self):
        try:
            self.drawDelay = 1 / 30
        except ZeroDivisionError:
            self.drawDelay = 1

        while self.doSimCycle:
            with self.drawReady:
                self.drawReady.notify()
                sleep(self.drawDelay)

    def sim_cycle(self):
        while self.doSimCycle:
            with self.drawReady:
                self.drawReady.wait()
                self.sim_step()

    def sim_start(self):
        self.log = LogEntry(frame_size=(610, 610),
                            body_count=len(bodies),
                            initial_pos=[x.position.getxy() for x in list(bodies.values())],
                            initial_vel=[x.speed.getxy() for x in list(bodies.values())])
        self.timerThread = Thread(target=self.timer_cycle, args=())
        self.simThread = Thread(target=self.sim_cycle, args=())

        self.ui.gpbBodies.setEnabled(False)
        self.ui.gpbEdit.setEnabled(False)
        self.ui.verticalLayout_2.setEnabled(False)
        self.ui.btnSimStart.setEnabled(False)
        self.ui.btnSimStep.setEnabled(False)
        self.ui.btnSimStop.setEnabled(True)

        self.frame_counter = 0
        self.doSimCycle = True
        self.simThread.start()
        self.timerThread.start()

    def sim_stop(self):

        self.ui.gpbBodies.setEnabled(True)
        self.ui.gpbEdit.setEnabled(True)
        self.ui.verticalLayout_2.setEnabled(True)
        self.ui.btnSimStart.setEnabled(True)
        self.ui.btnSimStep.setEnabled(True)
        self.ui.btnSimStop.setEnabled(False)

        self.doSimCycle = False
        self.simThread.join()
        self.timerThread.join()
        self.log.dump()
        self.create_graphs()

    def create_graphs(self):

        draw_x_y_graph()
        draw_speed_graph()
        try:
            self.ui.lbl_position_graph.setPixmap(QPixmap(QImage("xyplot.jpg")).scaled(
                self.ui.lbl_position_graph.width(),
                self.ui.lbl_position_graph.height(),
                QtCore.Qt.KeepAspectRatio))
            self.ui.lbl_speed_graph.setPixmap(QPixmap(QImage("speed_plot.jpg")).scaled(
                self.ui.lbl_speed_graph.width(),
                self.ui.lbl_speed_graph.height(),
                QtCore.Qt.KeepAspectRatio
            ))
        except FileNotFoundError:
            pass


def setup():
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    exit(app.exec())


if __name__ == "__main__":
    use('TkAgg')
    mainThread = Thread(target=setup(), args=())
    mainThread.start()
