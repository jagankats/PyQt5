from PyQt5 import QtCore, QtWidgets
from PyQt5 import uic
import sys, time, random

class DataClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(float, float, float, float)

    def __init__(self, parent=None):
        super(DataClass, self).__init__(parent)

    def run(self):
        print('Starting thread...')
        while True:
            lat, long = self.dummy_gps()
            temp = self.temp_sensor()
            humidity = self.humidity_sensor()
            self.any_signal.emit(lat, long, temp, humidity)
            time.sleep(1)

    def dummy_gps(self):
        lat = random.randint(3086340228, 3086405821)
        lat = lat / 100000000
        long = random.randint(7585707193, 7585898276)
        long = long / 100000000
        return lat, long

    def temp_sensor(self):
        return random.randint(15, 46)

    def humidity_sensor(self):
        return random.randint(50, 91)

    def stop(self):
        print('Stopping thread...')
        self.terminate()

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('main.ui', self)

        self.pushButton_2.setEnabled(False)
        self.pushButton.clicked.connect(self.start_worker)
        self.pushButton_2.clicked.connect(self.stop_worker)

    def start_worker(self):
        self.thread = DataClass(parent=None)
        self.thread.start()
        self.thread.any_signal.connect(self.my_function)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)

    def stop_worker(self):
        self.thread.stop()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)

    def my_function(self, lat, long, temp, humidity):
        temp = str(temp) + " Degree"
        humidity = str(humidity) + " %"
        self.ui.lineEdit.setText(str(lat))
        self.ui.lineEdit_2.setText(str(long))
        self.ui.lineEdit_3.setText(temp)
        self.ui.lineEdit_4.setText(humidity)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyApp()
    mainWindow.show()
    sys.exit(app.exec_())