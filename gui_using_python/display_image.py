import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QLineEdit, QGridLayout,QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

class user_input(QMainWindow):
	def __init__(self):
		super().__init__()

		self.line = QLineEdit(self)
		self.line.move(10,50)
		self.line.resize(200,40)

		self.label = QLabel(self)
		self.label.move(10,80)
		
		self.line.textChanged.connect(self.onChange)

		self.image = QLabel(self)

		self.button = QPushButton(self)
		self.button.move(10,120)
		self.button.setText("Get image")
		self.button.clicked.connect(self.display_image)

		self.setGeometry(50,50,600,600)
		self.setWindowTitle("this is line edit")
		self.show()

	def onChange(self, text):
		self.label.setText(text)
		self.label.adjustSize()

	def display_image(self,image):
		self.img = QPixmap("359.jpg")
		self.image.setPixmap(self.img)
		self.image.move(10,150)
		self.image.adjustSize()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = user_input()
	sys.exit(app.exec_())
