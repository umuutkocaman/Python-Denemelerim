import sys
from PyQt5 import QtWidgets
from tasarım_code import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCevir.clicked.connect(self.onClicked)
    def onClicked(self):
        items = self.ui.groupBox.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                metin = self.ui.input.text()
                if rb.text() == "BÜYÜT":
                    self.ui.output.setText(metin.upper())
                elif rb.text() == "KÜÇÜLT":
                    self.ui.output.setText(metin.lower())
                elif rb.text() == "CÜMLE BAŞ HARFİİNİ BÜYÜT":
                    self.ui.output.setText(metin.capitalize())
                elif rb.text() == "HER KELİMENİN BAŞ HARFİNİ BÜYÜT":
                    self.ui.output.setText(metin.title())
                else:
                    self.ui.output.setText(rb.text())
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()
