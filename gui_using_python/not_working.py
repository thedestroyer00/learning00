#This code is not working please help....
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QLineEdit, QGridLayout,QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

class user_input(QMainWindow):
	def __init__(self):
		super().__init__()

		self.line = QLineEdit(self)
		self.line.move(50,50)
		self.line.resize(200,40)

		self.label = QLabel(self)
		self.label.move(100,100)
		
		self.line.textChanged.connect(self.onChange)


		self.button = QPushButton(self)
		self.button.setText("Get image")
		self.button.move(100,200)
		self.button.clicked.connect(self.display_image)

		self.setGeometry(50,50,200,200)
		self.setWindowTitle("this is line edit")
		self.show()

	def onChange(self, text):
		self.label.setText(text)
		self.label.adjustSize()



	class display_image(QWidget):
		def __init__(self):
			super().__init__()

			self.img = QPixmap("./359.jpg")
			self.label = QLabel()
			self.label.setPixmap(self.img)

			self.grid = QGridLayout()
			self.grid.addWidget(self.label, 1,1)
			self.setLayout(self.grid)

			self.setGeometry(50,50,200,200)
			self.setWindowTitle("this is image")
			self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = user_input()
	sys.exit(app.exec_())
