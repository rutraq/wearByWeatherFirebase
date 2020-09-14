from PyQt5 import Qt, QtGui, QtCore
from PyQt5 import QtWidgets
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
        self.items = ["jacket", "sneakers", "shirt", "jeans", "t-shirt"]
        self.styles = ["Casual", "Sport", "Official"]
        self.shops = {}
        self.url = {}
        self.unique_number = int
        self.read_data()
        self.add_values()

        self.pushButton.setEnabled(False)

        self.pushButton.pressed.connect(self.write_data)
        self.lineEditStyleNumber.textChanged.connect(self.switch_button_enabled)
        self.lineEditUrl.textChanged.connect(self.switch_button_enabled)

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

    def switch_button_enabled(self):
        if self.lineEditUrl.text() != "" and self.lineEditStyleNumber.text() != "":
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

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
        items = self.document_read(collection, self.lineEditStyleNumber.text())
        items[str(self.unique_number)] = "{0}{1}{2}".format(self.unique_number, self.comboBoxItem.currentText(),
                                                            shop_number)
        doc_ref = db.collection(collection).document(self.lineEditStyleNumber.text())
        doc_ref.set(items)

        self.unique_number += 1

        doc_ref = db.collection("UniqueNumber").document("UniqueNumber")
        doc_ref.set({"1": self.unique_number})

    def read_data(self):
        self.shops = self.standard_read("shops")
        self.url = self.standard_read("Links")
        self.unique_number = int(self.standard_read("UniqueNumber")['1'])

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
        print(number)
        doc_ref = db.collection(collection).document(str(number))
        doc = doc_ref.get()
        if doc.exists:
            print(doc.to_dict())
            return doc.to_dict()
        else:
            doc_ref = db.collection(collection).document(str(number))
            doc_ref.set({})
            return {}


if __name__ == "__main__":
    app = Qt.QApplication([])
    si = MainForm()
    si.show()
    app.exec()
