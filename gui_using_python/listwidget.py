import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		grid = QGridLayout()
		self.setLayout(grid)

		self.listwidget = QListWidget()
		self.listwidget.insertItem(0,'Music')
		self.listwidget.insertItem(1,'Game')
		self.listwidget.insertItem(2,'Software')
		self.listwidget.insertItem(3,'Car')
		self.listwidget.clicked.connect(self.itemclicked)

		grid.addWidget(self.listwidget)

	def itemclicked(self):
		self.value = self.listwidget.currentItem()
		print(self.value.text())



if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = Window()
	screen.show()
	sys.exit(app.exec_())
