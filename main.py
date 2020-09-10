from PyQt5 import Qt, QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QCheckBox
import mainform


class MainForm(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.shops = ["nike", "хуяйк", "женина залупа", "бабкин хуй"]
        self.items = ["jacket", "sneakers", "shirt", "jeans", "t-shirts"]
        self.add_values()

    def add_values(self):
        for shop in self.shops:
            self.comboBoxShop.addItem(shop)
        for item in self.items:
            self.comboBoxItem.addItem(item)


if __name__ == "__main__":
    app = Qt.QApplication([])
    si = MainForm()
    si.show()
    app.exec()
