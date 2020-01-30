import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		grid = QGridLayout()
		self.setLayout(grid)

		label1 = QLabel("This is label 1")
		label2 = QLabel("This is label 2")

		tabwidget = QTabWidget()
		tabwidget.addTab(label1,"Tab 1")
		tabwidget.addTab(label2, "Tab 2")

		grid.addWidget(tabwidget)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = Window()
	screen.show()
	sys.exit(app.exec_())
