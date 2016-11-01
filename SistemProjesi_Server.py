import socket
from _thread import *

#host = 'localhost'
#port = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
import random
class baglanti():
    adrlistesi = []
    def __init__(self,host,port):
        self.host=host
        self.port=port
host = baglanti('localhost',8001)
try:
    s.bind((host.host, host.port))
except socket.error as e:
    print(str(e))
#a=[]
s.listen(5)
global c
c=[]
print('Baglanti bekleniyor')
def yolla(veri,adrsayisi):
    for i in range(0,adrsayisi):
        if veri is not None:
            host.adrlistesi[i].send(str.encode(veri))
def dosyayolla(veri,adrsayisi):
    for i in range(0,adrsayisi):
        if veri is not None:
            host.adrlistesi[i].send(str.encode(veri))

def thread(conn):
    while True:
        sayi=host.adrlistesi.__len__()
        print("dinlendi")
        data = conn.recv(2048)
        reply = data.decode('UTF-8')
        if reply.__eq__('-f'):
            yolla('%!%',sayi)
            while True:
                dosyaisim = random.randint(0,100)
                if dosyaisim not in c:
                    c.append(dosyaisim)
                    break
            with open(str(dosyaisim),'w') as alinan:
                print('geliyor')
                data=conn.recv(1024)
                alinan.write(data.decode('UTF-8'))
                dosyayolla(data.decode('UTF-8'),sayi)
                alinan.close()
        else:
            yolla(reply,sayi)
            print(reply)
            print("yollandi")

while True:
    conn, addr = s.accept()
    host.adrlistesi.append(conn)
    print('connected to: '+addr[0]+':'+str(addr[1]))
    isim=conn.recv(1024)
    conn.send(str.encode('Hoşgeldin'+'  '+isim.decode('UTF-8')))
    start_new_thread(thread,(conn,))