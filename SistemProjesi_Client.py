import sys

from _thread import*
import socket
from PyQt4 import QtGui


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
k=gui()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
class baglanti():
	def __init__(self,host,port):
		self.host=host
		self.port=port
global baglan
baglan = baglanti('localhost',8001)
def dosya(dizin):
	file = open(dizin,'rb')
	oku = file.read(1024)
	while (oku):
		sock.send(oku)
		print(oku)
		print('gidiyor')
		oku= file.read(1024)
	print('gitti')
	file.close()
	k.message.clear()
	exit_thread()
def yolla(sender):
	if len(k.message.text())<=0:
		return
	buf = k.name.text() + " :"+k.message.text()
	if k.message.text()[0:2].__eq__('-f'):
		sock.send(str.encode('-f'))
		dizin=k.message.text().strip()
		start_new_thread(dosya,(dizin[2:],))
		return
	else:
		k.message.clear()
		sock.send(str.encode(buf))
		return
def baglanfonk(sender):
	global sock
	if k.send.isEnabled() == False:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((baglan.host,baglan.port))
			k.send.setDisabled(False)
			k.text.append("Bağlantı başarılı")
			k.conn.setText("Çıkış")
		except:
			k.text.append("Bağlantı sağlanamadı")
	else:
		k.send.setDisabled(True)
		sock.send("çıkış")
		sock.close()
		k.text.append("Bağlantı kapandı")
		k.conn.setText("bağlan")
def recv():
	while True:
		try:
			ss = sock.recv(1024)
			gelen= ss.decode('UTF-8')
			print(ss.decode('UTF-8'))
			if gelen.__eq__('%!%'):
				with open('gelendosya','w') as dosya:
					ss=sock.recv(1024)
					dosya.write(ss.decode('UTF-8'))
					dosya.close()
			k.text.append(ss.decode('UTF-8'))
		except:
			pass
	exit_thread()

k.send.mousePressEvent = yolla
k.conn.mousePressEvent = baglanfonk

k.widget.show()
start_new_thread(recv,())
k.app.exec_()
sys.exit(sock.close())