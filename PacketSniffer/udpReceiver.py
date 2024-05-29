from PyQt5.QtNetwork import QUdpSocket, QHostAddress
import struct
from PyQt5.QtCore import pyqtSignal, QObject

class UDPReceiver(QObject):
    datagramReceived = pyqtSignal(bytes)

    def __init__(self,ip,port):
        super().__init__()

        # Set up the UDP socket
        self.udp_socket = QUdpSocket()
        self.ip = ip
        self.port = int(port)
        self.udp_socket.bind(QHostAddress(self.ip), self.port)

    def startReceving(self):

        self.udp_socket.readyRead.connect(self.readPendingDatagrams)
    
    def stopReceving(self):
        try:
            self.udp_socket.readyRead.disconnect(self.readPendingDatagrams)
        except TypeError as e:
            print(f"Error disconnecting signal: {e}")
        self.udp_socket.close()
        print("UDP receiver stopped")

    def readPendingDatagrams(self):
        while self.udp_socket.hasPendingDatagrams():
            datagram, _, _ = self.udp_socket.readDatagram(self.udp_socket.pendingDatagramSize())
            self.datagramReceived.emit(datagram)
            print("Inside Received message: ", datagram)
            # unpacked_data = struct.unpack('=HBH', datagram)
            # print("Unpacked Data:", unpacked_data)

