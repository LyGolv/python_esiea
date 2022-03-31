import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QGroupBox,
    QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
    QHBoxLayout, QSpacerItem, QGridLayout
)
from PyQt5.QtGui import (
    QIcon,
)
from PyQt5.QtCore import (
    Qt, QFile, QTextStream,
)
import requests

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.updateUI()

    
    def initUI(self):
        self.setObjectName("app")
        self.setWindowTitle("IP_Mapper")
        self.setWindowIcon(QIcon("workout_tp3/icon.png"))
        self.resize(320, 150)
        file = QFile("workout_tp3/client.qss")
        if not file.open(QFile.ReadOnly|QFile.Text):
            exit(-1)
        qss = QTextStream(file)
        self.setStyleSheet(qss.readAll())


    def updateUI(self):
        self.v_layout = QVBoxLayout(self)
        # Element of Vertical Layout
        # ----
        self.h1 = QLabel()
        self.h1.setText("Main Informations")
        self.h1.setAlignment(Qt.AlignHCenter)
        self.h1.setObjectName("H1")
        self.groupbox = QGroupBox()
        self.grid_layout = QGridLayout()
        self.send = QPushButton()
        self.send.setText("Envoyer")
        self.grid_layout.addWidget(QLabel(), 0, 1, 0, 2, Qt.AlignLeft)
        self.grid_layout.addWidget(self.send, 0, 4)
        self.v_layout.addWidget(self.h1)
        self.v_layout.addWidget(self.groupbox)
        self.v_layout.addLayout(self.grid_layout)
        # -----
        self.form_layout = QFormLayout()
        self.groupbox.setLayout(self.form_layout)
        # Element of form layout
        # ----
        self.ip = QLineEdit()
        self.api_key = QLineEdit()
        self.hostname = QLineEdit()   
        self.hostname.setText("127.0.0.1:8000")     
        self.form_layout.addRow(QLabel("Enter your Host IP:"), self.ip)
        self.form_layout.addRow(QLabel("Enter your API Key:"), self.api_key)
        self.form_layout.addRow(QLabel("Enter your Hostname:"), self.hostname)
        self.form_layout.addRow(QLabel("Answer:"), QLabel())  
        # ----     
        self.send.clicked.connect(self.on_click)
    

    def on_click(self):
        hostname = self.hostname.text()
        api_key  = self.api_key.text()
        ip = self.ip.text()
        print(hostname, api_key, ip)

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()