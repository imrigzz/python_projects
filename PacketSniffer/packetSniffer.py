# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PacketSniffer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from udpReceiver import UDPReceiver
from udpSender import UDPSender
import struct
import json
from datetime import datetime



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setObjectName("mainWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mainWidget)

        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.topWidget = QtWidgets.QWidget(self.mainWidget)
        self.topWidget.setObjectName("topWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.topWidget)

        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.ipLineEdit = QtWidgets.QLineEdit(self.topWidget)
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.horizontalLayout.addWidget(self.ipLineEdit)

        self.portLineEdit = QtWidgets.QLineEdit(self.topWidget)
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout.addWidget(self.portLineEdit)

        self.receivePushButton = QtWidgets.QPushButton(self.topWidget)
        self.receivePushButton.setObjectName("receivePushButton")
        self.receivePushButton.setCheckable(True)
        self.horizontalLayout.addWidget(self.receivePushButton)
        
        self.sendPushButton = QtWidgets.QPushButton(self.topWidget)
        self.sendPushButton.setObjectName("sendPushButton")
        self.horizontalLayout.addWidget(self.sendPushButton)
        
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.topWidget)


        # splitter
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        

        # Text browser widget
        self.textBrowserWidget = QtWidgets.QWidget(self.mainWidget)
        self.textBrowserWidget.setObjectName("textBrowserWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.textBrowserWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.textBrowserWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.splitter.addWidget(self.textBrowserWidget)
        # self.verticalLayout.addWidget(self.textBrowserWidget)
        


        
        # messageFormatterWidget
        self.messageFormatterWidget = QtWidgets.QWidget(self.mainWidget)
        self.messageFormatterWidget.setObjectName("messageFormatterWidget")
        # self.messageFormatterWidget.setStyleSheet("border-top: 1px solid black;")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.messageFormatterWidget)
        self.gridLayout_21.setObjectName("gridLayout_2")

        self.verticalLayoutFormatter = QtWidgets.QVBoxLayout()
        self.verticalLayoutFormatter.setObjectName("verticalLayoutFormatter")

        self.Label = QtWidgets.QLabel(self.messageFormatterWidget)
        self.Label.setObjectName("Label")
        self.Label.setText("B:1    H:2    I:4    L:4     Q:8")
        self.verticalLayoutFormatter.addWidget(self.Label)

        self.formatLineEdit = QtWidgets.QLineEdit(self.messageFormatterWidget)
        self.formatLineEdit.setObjectName("formatLineEdit")
        self.verticalLayoutFormatter.addWidget(self.formatLineEdit)

        self.HexLineEdit = QtWidgets.QLineEdit(self.messageFormatterWidget)
        self.HexLineEdit.setObjectName("HexLineEdit")
        self.verticalLayoutFormatter.addWidget(self.HexLineEdit)

        self.textBrowserHexList = QtWidgets.QTextEdit(self.messageFormatterWidget)
        self.textBrowserHexList.setObjectName("textBrowserHexList")
        self.verticalLayoutFormatter.addWidget(self.textBrowserHexList) 

        self.formatPushButton = QtWidgets.QPushButton(self.messageFormatterWidget)
        self.formatPushButton.setObjectName("formatPushButton")
        self.verticalLayoutFormatter.addWidget(self.formatPushButton) 
         

        self.gridLayout_21.addLayout(self.verticalLayoutFormatter, 0, 0, 1, 1)
        self.splitter.addWidget(self.messageFormatterWidget)
        # self.verticalLayout.addWidget(self.messageFormatterWidget)

        self.splitter.setSizes([1,0])

        self.verticalLayout.addWidget(self.splitter)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.mainWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ip,port = self.readConfigFileIP()
        self.ipLineEdit.setText(ip)
        self.portLineEdit.setText(str(port))
  
        self.sendPushButton.clicked.connect(self.send_message)
        
        self.receivePushButton.clicked.connect(self.receive_message)
        self.formatPushButton.clicked.connect(self.arrange_message)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ipLineEdit.setPlaceholderText(_translate("MainWindow", "Enter IP Address"))
        self.portLineEdit.setPlaceholderText(_translate("MainWindow", "Port"))
        self.formatLineEdit.setPlaceholderText(_translate("MainWindow", "Enter message format (format.json)"))
        self.HexLineEdit.setPlaceholderText(_translate("MainWindow", "Copy and paste clean HEx here"))
        self.receivePushButton.setText(_translate("MainWindow", "start Receive"))
        self.formatPushButton.setText(_translate("MainWindow", "Format"))
        self.sendPushButton.setText(_translate("MainWindow", "Send"))

    def readConfigFileIP(self):
        json_file_path = "config.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data['ip'], data['port']
    
    def readConfigFileDataTypes(self):
        json_file_path = "config.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data
    
    def receive_message(self):
        ip = self.ipLineEdit.text()
        port = self.portLineEdit.text()
        print(ip,port)
        self.receiverInstance = UDPReceiver(ip,port)
        self.receiverInstance.datagramReceived.connect(self.displayReceivedData)

        if self.receivePushButton.isChecked():
            self.receivePushButton.setText("stop receiving")
            self.receiverInstance.startReceving()
        else:
            self.receivePushButton.setText("start receiving")
            self.receiverInstance.stopReceving()

    def displayReceivedData(self,datagram):
        print("Received message: ", datagram)
        current_time = self.currentTime()
        self.textBrowser.append(f"{current_time} Raw Hex Format >> {str(datagram)}")
        print(datagram)
        HexList = self.formatDatagramToCleanList(datagram)
        self.displayHexList(HexList)
        self.textBrowser.append(f"{current_time} Total Message Length >> {len(HexList)}")
        self.textBrowser.append('--------------------------------------------------------------')
   

    def send_message(self):
        senderInstance = UDPSender()
        values = [21,6,8082864118]
        packed_data = struct.pack(f'=BBQ', *values)
        senderInstance.send_message(packed_data)

    def formatDatagramToCleanList(self,datagram):
        hex_list = [format(byte, '02x') for byte in datagram]
        return hex_list
    
    def displayHexList(self,HexList):
        currentTime = self.currentTime()
        hex_string = ' '.join(HexList)
        self.textBrowser.append(f"{currentTime} Clean Hex Data >> {hex_string}")
        

    def arrange_message(self):
        format = self.formatLineEdit.text()
        HexValues = self.HexLineEdit.text()
        HList = HexValues.split(' ')
        Hstr = ''.join(HList)
        HexBytearray = bytearray.fromhex(Hstr)
        print(HexValues, HexBytearray)
        format_length = self.calculate_format_length(format)
        self.textBrowserHexList.append(f"Expected message length: {format_length} \nEntered Message Length: {len(HList)} ")
        
        format_little_endian  = '='+format

        unpacked_data = struct.unpack(format_little_endian, HexBytearray)
        for i in range(len(unpacked_data)):
            self.textBrowserHexList.append(f"{i} {format[i]} : {unpacked_data[i]}")
        self.textBrowserHexList.append("-------------------------------------------------")

    def calculate_format_length(self,format):
        length = 0
        data = self.readConfigFileDataTypes()
        for item in format:
            length = length + data[item]
        return length
    
    def currentTime(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        return formatted_time
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())