from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox, QApplication
from main import Ui_MainWindow
from sub import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pbSum.clicked.connect(self.close)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pbSubWin.clicked.connect(self.onClicked)

    def onClicked(self):
        updateDialog = Dialog()
        updateDialog.exec_()
        try:
            self.a = float(updateDialog.lineEdit.text())
            self.b = float(updateDialog.lineEdit_2.text())
            self.sum = self.a+self.b
            self.label_2.setText(str(self.sum))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please Enter valid integer Numbers')
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec_()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
