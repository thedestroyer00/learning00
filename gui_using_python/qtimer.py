import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,Qt,QTimer

class window(QMainWindow):
	def __init__(self):
		QWidget.__init__(self)

		self.checkbox = QCheckBox("This is a checkbox",self)
		self.checkbox.move(50,50)
		self.checkbox.setChecked(True)
		self.checkbox.adjustSize()
		self.checkbox.toggled.connect(self.onchange)

		self.checkboxx = QCheckBox("This is't a checkbox",self)
		self.checkboxx.move(50,70)
		self.checkboxx.adjustSize()

		self.timer = QTimer()
		self.timer.timeout.connect(self.handletime)
		self.timer.start(400)

	def handletime(self):
		if str(self.checkbox.isChecked()) == "True":
			self.checkboxx.setChecked(False)
		else:
			self.checkboxx.setChecked(True)

		self.setGeometry(50,50,300,300)
		self.setWindowTitle('This is window title ')
		self.show()

	def onchange(self):
		self.checkvalue = self.sender()
		print("The value is changed to " + str(self.checkvalue.isChecked()))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = window()
	sys.exit(app.exec_())

