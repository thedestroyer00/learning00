import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 

class Window(QWidget):
	def __init__(self):
		super().__init__()

		self.button = QPushButton("show dialog",self)
		self.button.move(0,0)
		self.adjustSize()
		self.button.clicked.connect(self.showdialog)

		self.label = QLabel(self)
		self.label.move(50,100)
		

		self.setGeometry(50,50,600,600)
		self.setWindowTitle("This is dialog box")
		self.show()

	def showdialog(self):
		text, ok = QInputDialog.getText(self, "Input Dialog", "Enter Text: ")
		if ok : 
			self.label.setText(str(text))
			self.label.adjustSize()


if __name__ == "__main__":
	app=QApplication(sys.argv)
	win = Window()
	sys.exit(app.exec_())



