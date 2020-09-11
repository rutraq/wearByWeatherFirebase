from PyQt5 import Qt, QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QCheckBox
import mainform
from firebase import Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class MainForm(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        cred = credentials.Certificate('wear-by-weather.json')
        firebase_admin.initialize_app(cred)
        self.items = ["jacket", "sneakers", "shirt", "jeans", "t-shirts"]
        self.shops = {}
        self.read_data()
        self.add_values()
        self.pushButton.pressed.connect(self.write_data)

    def add_values(self):
        for shop in self.shops.values():
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
        firebase = Firebase(config)
        db = firebase.database()
        data = {"1": "nike",
                "2": "залупа жени",
                "3": "Гулькин хуй"}
        db.child("shops").set(data)
        print(db.child("shops").get().val())

    def write_data(self):
        db = firestore.client()
        self.shops[str(len(self.shops) + 1)] = self.lineEditPath.text()
        doc_ref = db.collection('shops').document('shops')
        doc_ref.set(self.shops)
        self.comboBoxShop.clear()
        self.add_values()

    def read_data(self):
        db = firestore.client()
        emp_ref = db.collection('shops')
        docs = emp_ref.stream()
        for doc in docs:
            self.shops = doc.to_dict()


if __name__ == "__main__":
    app = Qt.QApplication([])
    si = MainForm()
    si.show()
    app.exec()
