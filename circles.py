import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.create_circle_btn.clicked.connect(self.update)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Git и желтые окружности')

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(252, 227, 3))
        r = randint(1, 100)
        x = randint(0, 640)
        y = randint(0, 480)
        self.qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleWindow()
    ex.show()
    sys.exit(app.exec())