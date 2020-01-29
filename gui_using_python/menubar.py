import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		grid = QGridLayout()
		self.setLayout(grid)

		menubar = QMenuBar()
		grid.addWidget(menubar,0,0)

		actionfile = menubar.addMenu("File")
		actionfile.addAction("New")
		actionfile.addAction("Save")
		actionfile.addAction("Save As")
		actionfile.addSeparator()
		actionfile.addAction("Quit")

		menubar.addMenu("View")
		menubar.addMenu("Store")

		text = QPlainTextEdit()
		grid.addWidget(text,1,0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
