import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class CirclesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.qp = QPainter()
        self.create_circle_btn.clicked.connect(self.update)

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.create_circle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_circle_btn.setGeometry(QtCore.QRect(230, 200, 171, 41))
        self.create_circle_btn.setObjectName("create_circle_btn")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и случайные окружности"))
        self.create_circle_btn.setText(_translate("MainWindow", "Создать окружность"))

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(randint(1, 255), randint(1, 100), randint(1, 100)))
        r = randint(1, 100)
        x = randint(0, 640)
        y = randint(0, 480)
        self.qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CirclesWindow()
    ex.show()
    sys.exit(app.exec())
