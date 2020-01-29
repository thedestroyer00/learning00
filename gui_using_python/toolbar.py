import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		grid = QGridLayout()
		self.setLayout(grid)

		toolbar = QToolBar()
		grid.addWidget(toolbar)

		toolbutton = QToolButton()
		toolbutton.setText("Button1")
		toolbutton.setCheckable(True)
		toolbutton.setAutoExclusive(True)
		toolbar.addWidget(toolbutton)

		toolbutton = QToolButton()
		toolbutton.setText("Button2")
		toolbutton.setCheckable(True)
		toolbutton.setAutoExclusive(True)
		toolbar.addWidget(toolbutton)

		textfield = QPlainTextEdit()
		grid.addWidget(textfield)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

