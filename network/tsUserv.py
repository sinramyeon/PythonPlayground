# udp timestamp
# 연결 지향 통신이 아닌 udp

from socket import *
from time import time


HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True :
  print ' waiting for message .... '
  data, addr = udpSerSock.recvfrom(BUFSIZ)
  udpSerSock.sendto('[%s] %s' %(ctime(), data), addr)
  print ' ... received from and returned to : ', addr


udpSerSock.close()
