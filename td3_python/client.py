import webbrowser
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 260)
        x, y = 10, 10
        self.label1 = QLabel("Enter your host IP:", self)
        self.label1.move(x, y)
        y += 30
        self.text1 = QLineEdit(self)
        self.text1.move(x+30, y)
        y += 30
        self.label2 = QLabel("Enter your API Key:", self)
        self.label2.move(x, y)
        y += 30
        self.text2 = QLineEdit(self)
        self.text2.move(x+30, y)
        y += 30
        self.label3 = QLabel("Enter the hostname:", self)
        self.label3.move(x, y)
        y += 30
        self.text3 = QLineEdit(self)
        self.text3.move(x+30, y)
        y += 30
        self.label4 = QLabel("Answer:", self)
        self.label4.move(x, y)
        y += 30
        self.button = QPushButton("Send", self)
        self.button.move(x, y)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        ip = self.text1.text()
        api_key = self.text2.text()
        hostname = self.text3.text()

        if ip == "" or api_key == "" or hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(ip, api_key, hostname)
            if res:
                self.label4.setText("Answer: %s" % res)
                self.label4.adjustSize()
                self.show()
                if 'LAT' not in res.keys() or 'LONG' not in res.keys():
                    QMessageBox.about(self, "Error", "Position not found")
                else:
                    url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res['LAT'], res['LONG'])
                    webbrowser.open(url)

    def __query(self, ip, api_key, hostname):
        url = "http://%s/ip/%s?key=%s" % (hostname, ip, api_key)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()