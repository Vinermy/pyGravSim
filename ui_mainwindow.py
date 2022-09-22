# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 630)
        MainWindow.setMaximumSize(QSize(900, 630))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 261, 611))
        self.vloToolbar = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vloToolbar.setObjectName(u"vloToolbar")
        self.vloToolbar.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.vloToolbar.setContentsMargins(0, 0, 0, 0)
        self.gpbBodies = QGroupBox(self.verticalLayoutWidget_2)
        self.gpbBodies.setObjectName(u"gpbBodies")
        self.gpbBodies.setMaximumSize(QSize(255, 150))
        self.lstBodies = QListWidget(self.gpbBodies)
        self.lstBodies.setObjectName(u"lstBodies")
        self.lstBodies.setGeometry(QRect(5, 21, 241, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstBodies.sizePolicy().hasHeightForWidth())
        self.lstBodies.setSizePolicy(sizePolicy)

        self.vloToolbar.addWidget(self.gpbBodies)

        self.gpbEdit = QGroupBox(self.verticalLayoutWidget_2)
        self.gpbEdit.setObjectName(u"gpbEdit")
        self.gpbEdit.setMaximumSize(QSize(255, 250))
        self.verticalLayoutWidget = QWidget(self.gpbEdit)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 243, 221))
        self.vloEdit = QVBoxLayout(self.verticalLayoutWidget)
        self.vloEdit.setObjectName(u"vloEdit")
        self.vloEdit.setContentsMargins(0, 0, 0, 0)
        self.gloPosSpd = QGridLayout()
        self.gloPosSpd.setObjectName(u"gloPosSpd")
        self.lblPos = QLabel(self.verticalLayoutWidget)
        self.lblPos.setObjectName(u"lblPos")

        self.gloPosSpd.addWidget(self.lblPos, 0, 0, 1, 1)

        self.lblSpdX = QLabel(self.verticalLayoutWidget)
        self.lblSpdX.setObjectName(u"lblSpdX")

        self.gloPosSpd.addWidget(self.lblSpdX, 1, 1, 1, 1)

        self.lblSpdY = QLabel(self.verticalLayoutWidget)
        self.lblSpdY.setObjectName(u"lblSpdY")

        self.gloPosSpd.addWidget(self.lblSpdY, 1, 3, 1, 1)

        self.lblPosY = QLabel(self.verticalLayoutWidget)
        self.lblPosY.setObjectName(u"lblPosY")

        self.gloPosSpd.addWidget(self.lblPosY, 0, 3, 1, 1)

        self.lblPosX = QLabel(self.verticalLayoutWidget)
        self.lblPosX.setObjectName(u"lblPosX")

        self.gloPosSpd.addWidget(self.lblPosX, 0, 1, 1, 1)

        self.lblSpd = QLabel(self.verticalLayoutWidget)
        self.lblSpd.setObjectName(u"lblSpd")

        self.gloPosSpd.addWidget(self.lblSpd, 1, 0, 1, 1)

        self.spbPosX = QSpinBox(self.verticalLayoutWidget)
        self.spbPosX.setObjectName(u"spbPosX")
        self.spbPosX.setEnabled(True)
        self.spbPosX.setMinimum(-310)
        self.spbPosX.setMaximum(310)

        self.gloPosSpd.addWidget(self.spbPosX, 0, 2, 1, 1)

        self.spbPosY = QSpinBox(self.verticalLayoutWidget)
        self.spbPosY.setObjectName(u"spbPosY")
        self.spbPosY.setEnabled(True)
        self.spbPosY.setMinimum(-310)
        self.spbPosY.setMaximum(310)

        self.gloPosSpd.addWidget(self.spbPosY, 0, 4, 1, 1)

        self.spbSpdX = QSpinBox(self.verticalLayoutWidget)
        self.spbSpdX.setObjectName(u"spbSpdX")
        self.spbSpdX.setEnabled(True)
        self.spbSpdX.setMinimum(-500)
        self.spbSpdX.setMaximum(500)

        self.gloPosSpd.addWidget(self.spbSpdX, 1, 2, 1, 1)

        self.spbSpdY = QSpinBox(self.verticalLayoutWidget)
        self.spbSpdY.setObjectName(u"spbSpdY")
        self.spbSpdY.setEnabled(True)
        self.spbSpdY.setMinimum(-500)
        self.spbSpdY.setMaximum(500)

        self.gloPosSpd.addWidget(self.spbSpdY, 1, 4, 1, 1)


        self.vloEdit.addLayout(self.gloPosSpd)

        self.hloMass = QHBoxLayout()
        self.hloMass.setObjectName(u"hloMass")
        self.lblMass = QLabel(self.verticalLayoutWidget)
        self.lblMass.setObjectName(u"lblMass")

        self.hloMass.addWidget(self.lblMass)

        self.spbMass = QSpinBox(self.verticalLayoutWidget)
        self.spbMass.setObjectName(u"spbMass")
        self.spbMass.setEnabled(True)
        self.spbMass.setMinimum(1)
        self.spbMass.setMaximum(1000000)
        self.spbMass.setValue(1)

        self.hloMass.addWidget(self.spbMass)


        self.vloEdit.addLayout(self.hloMass)

        self.hloRadius = QHBoxLayout()
        self.hloRadius.setObjectName(u"hloRadius")
        self.lblRadius = QLabel(self.verticalLayoutWidget)
        self.lblRadius.setObjectName(u"lblRadius")

        self.hloRadius.addWidget(self.lblRadius)

        self.spbRadius = QSpinBox(self.verticalLayoutWidget)
        self.spbRadius.setObjectName(u"spbRadius")
        self.spbRadius.setEnabled(True)
        self.spbRadius.setMinimum(1)
        self.spbRadius.setMaximum(100)
        self.spbRadius.setValue(10)

        self.hloRadius.addWidget(self.spbRadius)


        self.vloEdit.addLayout(self.hloRadius)

        self.vloButtons = QVBoxLayout()
        self.vloButtons.setObjectName(u"vloButtons")
        self.btnNew = QPushButton(self.verticalLayoutWidget)
        self.btnNew.setObjectName(u"btnNew")

        self.vloButtons.addWidget(self.btnNew)

        self.hloButtons = QHBoxLayout()
        self.hloButtons.setObjectName(u"hloButtons")
        self.btnDelete = QPushButton(self.verticalLayoutWidget)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setEnabled(True)

        self.hloButtons.addWidget(self.btnDelete)

        self.btnCopy = QPushButton(self.verticalLayoutWidget)
        self.btnCopy.setObjectName(u"btnCopy")
        self.btnCopy.setEnabled(True)

        self.hloButtons.addWidget(self.btnCopy)


        self.vloButtons.addLayout(self.hloButtons)


        self.vloEdit.addLayout(self.vloButtons)


        self.vloToolbar.addWidget(self.gpbEdit)

        self.gpbSettings = QGroupBox(self.verticalLayoutWidget_2)
        self.gpbSettings.setObjectName(u"gpbSettings")
        self.gpbSettings.setMaximumSize(QSize(255, 150))
        self.verticalLayoutWidget_3 = QWidget(self.gpbSettings)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 19, 231, 127))
        self.vloSimSettings = QVBoxLayout(self.verticalLayoutWidget_3)
        self.vloSimSettings.setObjectName(u"vloSimSettings")
        self.vloSimSettings.setContentsMargins(0, 0, 0, 0)
        self.cbxDrawTrails = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxDrawTrails.setObjectName(u"cbxDrawTrails")

        self.vloSimSettings.addWidget(self.cbxDrawTrails)

        self.cbxDrawSpdVects = QCheckBox(self.verticalLayoutWidget_3)
        self.cbxDrawSpdVects.setObjectName(u"cbxDrawSpdVects")

        self.vloSimSettings.addWidget(self.cbxDrawSpdVects)

        self.vloSimSpd = QVBoxLayout()
        self.vloSimSpd.setObjectName(u"vloSimSpd")
        self.lblSimSpd = QLabel(self.verticalLayoutWidget_3)
        self.lblSimSpd.setObjectName(u"lblSimSpd")

        self.vloSimSpd.addWidget(self.lblSimSpd)

        self.hrsSimSpd = QSlider(self.verticalLayoutWidget_3)
        self.hrsSimSpd.setObjectName(u"hrsSimSpd")
        self.hrsSimSpd.setMinimum(1)
        self.hrsSimSpd.setMaximum(61)
        self.hrsSimSpd.setValue(31)
        self.hrsSimSpd.setOrientation(Qt.Horizontal)
        self.hrsSimSpd.setInvertedAppearance(False)
        self.hrsSimSpd.setInvertedControls(False)
        self.hrsSimSpd.setTickPosition(QSlider.TicksAbove)
        self.hrsSimSpd.setTickInterval(15)

        self.vloSimSpd.addWidget(self.hrsSimSpd)


        self.vloSimSettings.addLayout(self.vloSimSpd)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnSimStart = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStart.setObjectName(u"btnSimStart")
        self.btnSimStart.setMaximumSize(QSize(23, 23))
        icon = QIcon()
        icon.addFile(u":/icon/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStart.setIcon(icon)
        self.btnSimStart.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStart)

        self.btnSimStep = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStep.setObjectName(u"btnSimStep")
        self.btnSimStep.setMaximumSize(QSize(23, 23))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/step.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStep.setIcon(icon1)
        self.btnSimStep.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStep)

        self.btnSimStop = QPushButton(self.verticalLayoutWidget_3)
        self.btnSimStop.setObjectName(u"btnSimStop")
        self.btnSimStop.setMaximumSize(QSize(23, 23))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSimStop.setIcon(icon2)
        self.btnSimStop.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btnSimStop)


        self.vloSimSettings.addLayout(self.horizontalLayout_2)


        self.vloToolbar.addWidget(self.gpbSettings)

        self.lblCreator = QLabel(self.verticalLayoutWidget_2)
        self.lblCreator.setObjectName(u"lblCreator")
        self.lblCreator.setMaximumSize(QSize(16777215, 20))
        self.lblCreator.setAlignment(Qt.AlignCenter)

        self.vloToolbar.addWidget(self.lblCreator)

        self.lblSimulationDisplay = QLabel(self.centralwidget)
        self.lblSimulationDisplay.setObjectName(u"lblSimulationDisplay")
        self.lblSimulationDisplay.setGeometry(QRect(280, 10, 610, 610))
        self.lblSimulationDisplay.setMaximumSize(QSize(610, 610))
        self.lblSimulationDisplay.setFrameShape(QFrame.Panel)
        self.lblSimulationDisplay.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyGravSim", None))
        self.gpbBodies.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0430", None))
        self.gpbEdit.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.lblPos.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435:", None))
        self.lblSpdX.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.lblSpdY.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.lblPosY.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.lblPosX.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.lblSpd.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c:", None))
        self.lblMass.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0441\u0430:", None))
        self.lblRadius.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441:", None))
        self.btnNew.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnCopy.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.gpbSettings.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.cbxDrawTrails.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0441\u043b\u0435\u0434", None))
        self.cbxDrawSpdVects.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0432\u0435\u043a\u0442\u043e\u0440\u044b \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0435\u0439", None))
        self.lblSimSpd.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.btnSimStart.setText("")
        self.btnSimStep.setText("")
        self.btnSimStop.setText("")
        self.lblCreator.setText(QCoreApplication.translate("MainWindow", u"by Egor Kosachev | Distributed via MIT Liscence", None))
        self.lblSimulationDisplay.setText("")
    # retranslateUi

