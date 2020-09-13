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
        self.unique_number = int
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
        self.url[str(self.unique_number)] = self.lineEditUrl.text()
        doc_ref = db.collection('Links').document('links')
        doc_ref.set(self.url)
        shop_number = int
        for k, v in self.shops.items():
            if v == self.comboBoxShop.currentText():
                shop_number = k
        collection = "{0}-{1}-{2}".format(self.comboBoxGender.currentText(), self.comboBoxWeight.currentText(),
                                          self.comboBoxStyle.currentText())
        items = self.document_read(collection, shop_number)
        items[str(self.unique_number)] = "{0}{1}{2}".format(self.unique_number, self.comboBoxItem.currentText(),
                                                            shop_number)
        doc_ref = db.collection(collection).document(self.lineEditStyleNumber.text())
        doc_ref.set(items)

        self.unique_number += 1

    def read_data(self):
        db = firestore.client()
        self.shops = self.standard_read("shops")
        self.url = self.standard_read("Links")
        self.unique_number = int(self.standard_read("UniqueNumber")['1'])

        doc_ref = db.collection('Men-NormalBodyWeight-Casual').document('1')
        doc = doc_ref.get()
        if doc.exists:
            print(doc.to_dict())

    @staticmethod
    def standard_read(collection):
        db = firestore.client()
        info = db.collection(collection)
        docs = info.stream()
        for doc in docs:
            info = doc.to_dict()
        return info

    @staticmethod
    def document_read(collection, number):
        db = firestore.client()
        doc_ref = db.collection(collection).document(str(number))
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()


if __name__ == "__main__":
    app = Qt.QApplication([])
    si = MainForm()
    si.show()
    app.exec()
