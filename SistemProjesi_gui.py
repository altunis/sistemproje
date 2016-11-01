from PyQt4 import QtGui
import sys


class gui():
	app = QtGui.QApplication(sys.argv)
	widget = QtGui.QWidget()
	widget.resize(500, 400)
	widget.setWindowTitle('Sistem Odevi')
	layout = QtGui.QGridLayout(widget)
	text = QtGui.QTextBrowser()
	lmessage = QtGui.QLabel("Mesaj:")
	message = QtGui.QLineEdit()
	lname = QtGui.QLabel("isim:")
	name = QtGui.QLineEdit()
	name.setText("isim:")
	send = QtGui.QPushButton("yolla")
	conn = QtGui.QPushButton("Bağlan")
	send.setDisabled(True)
	layout.addWidget(text,0,0,6,5)
	layout.addWidget(lname,6,0)
	layout.addWidget(name,6,1,1,2)
	layout.addWidget(send,6,5,1,1)
	layout.addWidget(conn,6,4,1,1)
	layout.addWidget(lmessage,7,0,1,1)
	layout.addWidget(message,7,1,1,4)