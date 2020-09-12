from PyQt5 import Qt, QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QCheckBox
import mainform
from firebase import Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage


class MainForm(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        cred = credentials.Certificate('wear-by-weather.json')
        firebase_admin.initialize_app(cred)
        self.items = ["jacket", "sneakers", "shirt", "jeans", "t-shirts"]
        self.styles = ["Casual", "Sport", "Official"]
        self.shops = {}
        self.url = {}
        self.read_data()
        self.add_values()
        self.pushButton.pressed.connect(self.write_data)
        # self.firebase_check()

    def add_values(self):
        for shop in self.shops.values():
            self.comboBoxShop.addItem(shop)
        for item in self.items:
            self.comboBoxItem.addItem(item)
        for style in self.styles:
            self.comboBoxStyle.addItem(style)

    def firebase_check(self):
        config = {
            "apiKey": "AIzaSyAl0sJD8bl30gnWH9juh6pywzOzsuzSdso",
            "authDomain": "wear-by-weather.firebaseapp.com",
            "databaseURL": "https://wear-by-weather.firebaseio.com",
            "storageBucket": "wear-by-weather.appspot.com"
        }
        fir = Firebase(config)
        lis = fir.storage().child("Men/NormalBodyWeight/Casual/1/details")

    def write_data(self):
        db = firestore.client()
        self.shops[str(len(self.shops) + 1)] = self.lineEditPath.text()
        doc_ref = db.collection('shops').document('shops')
        doc_ref.set(self.shops)
        self.comboBoxShop.clear()
        doc_ref = db.collection("Links").document("links")
        doc_ref.set(self.url)
        self.add_values()

    def read_data(self):
        db = firestore.client()
        shops = db.collection("shops")
        docs = shops.stream()
        for doc in docs:
            self.shops = doc.to_dict()
        urls = db.collection("Links")
        docs = urls.stream()
        for doc in docs:
            self.url = doc.to_dict()

        doc_ref = db.collection('Casual').document('2')
        doc = doc_ref.get()
        if doc.exists:
            print(doc.to_dict())


if __name__ == "__main__":
    app = Qt.QApplication([])
    si = MainForm()
    si.show()
    app.exec()
