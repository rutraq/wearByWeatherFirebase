from PyQt5 import Qt, QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QCheckBox
import mainform
from firebase import Firebase
from Crypto.PyblicKey import RSA

class MainForm(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.shops = ["nike", "хуяйк", "женина залупа", "бабкин хуй"]
        self.items = ["jacket", "sneakers", "shirt", "jeans", "t-shirts"]
        self.add_values()
        self.firebase_check()

    def add_values(self):
        for shop in self.shops:
            self.comboBoxShop.addItem(shop)
        for item in self.items:
            self.comboBoxItem.addItem(item)

    def firebase_check(self):
        config = {
            "apiKey": "AIzaSyAl0sJD8bl30gnWH9juh6pywzOzsuzSdso",
            "authDomain": "wear-by-weather.firebaseapp.com",
            "databaseURL": "https://wear-by-weather.firebaseio.com",
            "storageBucket": "wear-by-weather.appspot.com",
        }
        firebase2 = Firebase(config)


if __name__ == "__main__":
    app = Qt.QApplication([])
    si = MainForm()
    si.show()
    app.exec()
