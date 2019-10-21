from PySide2 import QtCore, QtGui, QtWidgets
from mainui import Ui_MainWindow

class UIPracticeWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(UIPracticeWindow, self).__init__(parent)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# User functions
		self.ui.pushButton.clicked.connect(self.printDennts)
		self.ui.clear.clicked.connect(self.cleartext)
		self.ui.pushButton.clicked.connect(self.printMessage)

	def printDennts(self):
		self.ui.textEdit.setText(" Dennts")
	
	def cleartext(self):
		self.ui.textEdit.setText("")

	def printMessage(self):
		print("Hello World")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UIPracticeWindow()
    MainWindow.show()
    #sys.exit(app.exec_())
