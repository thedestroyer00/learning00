# Let's add message box in our GUI 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
	app = QApplication(sys.argv)
	widget = QWidget()

	label = QLabel(widget)
	label.setText("Hello World")
	label.move(10,10)

	button1 = QPushButton(widget)
	button1.setText("Button1")
	button1.move(10,50)
	button1.clicked.connect(button1_clicked)

	button2 = QPushButton(widget)
	button2.setText("Button2")
	button2.move(10,100)
	button2.clicked.connect(button2_clicked)

	button3 = QPushButton(widget)
	button3.setText("enter")
	button3.move(10,150)
	button3.clicked.connect(messagebox)

	widget.setGeometry(50,50,400,400)
	widget.setWindowTitle("This is the PyQt5")
	widget.show()
	sys.exit(app.exec_())

def messagebox():
	message = QMessageBox()
	message.setIcon(QMessageBox.Information)
	message.setText("Would you like to continue")
	message.setWindowTitle("Confirm")
	message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	message.buttonClicked.connect(messagebutton)

	buttonmessage = message.exec()
	if buttonmessage == QMessageBox.Ok:
		print("Ok button is pushed")
	elif buttonmessage == QMessageBox.Cancel:
		print("Cancel is pushed")


def button1_clicked():
	print("Button 1 is clicked")

def button2_clicked():
	print("Button 2 is clicked")

def messagebutton(i):
	print(i.text(),"button is clicked")

if __name__ == "__main__":
	window()
