# Lets learn to add some widgets in the gui window created using PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
	app = QApplication(sys.argv)
	widget = QWidget()
	
	label = QLabel(widget)
	label.setText("Learnig to add label and button in PyQt5") 
	label.move(10,10)
	
	button1 = QPushButton(widget)
	button1.setText("Button 1")
	button1.move(10,50)
	button1.clicked.connect(button1_clicked)
	
	button2 = QPushButton(widget)
	button2.setText("Button 2")
	button2.move(10,100)
	button2.clicked.connect(button2_clicked)
	
	widget.setGeometry(50,50, 400,400)
	widget.setWindowTitle("Learing PyQt5")
	widget.show()
	sys.exit(app.exec_())
	

def button1_clicked():
	print("Button 1 is clicked")
	
def button2_clicked():
	print("Button 2 is clicked")
	
if __name__ == "__main__":
	window()
	
	
	
