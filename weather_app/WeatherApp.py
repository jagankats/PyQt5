from PyQt5.QtWidgets import QApplication, QMainWindow
from main import Ui_MainWindow
from owm import OpenWeatherMap


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showdata)

    def showdata(self):
        obj = OpenWeatherMap()
        weather_data = obj.weather_condition()
        soil_data = obj.soil_report()
        self.leDT.setText(weather_data[0])
        self.leWC.setText(weather_data[1])
        self.leWS.setText(weather_data[2])
        self.leH.setText(weather_data[3])
        self.leT.setText(weather_data[4])
        self.leC.setText(weather_data[5])
        self.leSTS.setText(soil_data[0])
        self.leST10.setText(soil_data[1])
        self.leSM.setText(soil_data[2])


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())