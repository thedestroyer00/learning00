import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.setWindowTitle("This is PyQt5")
		grid = QGridLayout()
		self.setLayout(grid)

		group = QGroupBox("This is group layout")
		group.setCheckable(True)
		grid.addWidget(group)

		vbox = QVBoxLayout()
		group.setLayout(vbox)

		radion = QRadioButton("Radiobutton 1")
		vbox.addWidget(radion)

		radion = QRadioButton("Radiobutton 2")
		vbox.addWidget(radion)

		radion = QRadioButton("Radiobutton 3")
		vbox.addWidget(radion)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
