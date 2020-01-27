import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

class window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.label = QLabel(self)
		self.label.setText("This is all I have so far in python graphics ")
		self.label.move(0,0)
		self.label.adjustSize()


		self.button = QPushButton(self)
		self.button.move(0,50)
		self.button.setText("Get Image")
		self.button.clicked.connect(self.display_image)

		self.image = QLabel(self)
		self.image.move(20,150)
	
		self.checkbox = QCheckBox("This is a car",self)
		self.checkbox.setChecked(True)
		self.checkbox.move(0,800)
		self.checkbox.adjustSize()
		self.checkbox.toggled.connect(self.change)

		self.checkboxx = QCheckBox("This is not a car", self)
		if str(self.checkbox.isChecked()) == "True":
			self.checkboxx.setChecked(False)
		else:
			self.checkboxx.setChecked(True)
		self.checkboxx.move(0,820)
		self.checkboxx.adjustSize()
		self.checkboxx.toggled.connect(self.change)
		
		self.setWindowTitle("This is power of python")
		self.setGeometry(50,50,1400,900)
		self.show()


	def change(self):
		self.value = self.sender()
		print("Your choice is " + str(self.checkbox.isChecked()))

	def display_image(self,image):
		self.img = QPixmap("359.jpg")
		self.image.setPixmap(self.img)
		self.image.adjustSize()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = window()
	sys.exit(app.exec_())





