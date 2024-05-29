from PyQt5.QtNetwork import QUdpSocket, QHostAddress
import struct


class UDPSender():
    def __init__(self):
        super().__init__()
                # Set up the UDP socket
        self.udp_socket = QUdpSocket()

        # Define IP and port to send messages to
        self.target_ip = "192.168.29.252"  # Change this to the receiver's IP address
        self.target_port = 2021

    def send_message(self, data):
            if data:
                datagram = data
                self.udp_socket.writeDatagram(datagram, QHostAddress(self.target_ip), self.target_port)
                print(f"Message sent: {data}, Dataframe: {datagram}")
            else:
                print("Please enter a message to send")