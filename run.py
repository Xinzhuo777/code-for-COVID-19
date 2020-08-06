import sys
import kv
from PyQt5.QtWidgets import *
from main_ui import *
from predict_ui import *
# import the_tk as win2
import a_project
palette1 = QtGui.QPalette()
palette1.setColor(palette1.Background, QtGui.QColor(255, 255, 255))

class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setPalette(palette1)
        self.pushButton.clicked.connect(self.open_win1)
        self.pushButton_2.clicked.connect(self.open_win2)

    def open_win1(self):
        self.close()
        self.win1 = MyPreWindow()
        self.win1.show()
    def open_win2(self):
        import the_tk as win2
        win2.main_tk()
        pass
class MyPreWindow(QMainWindow, Pre_MainWindow):

    def __init__(self, parent=None):
        super(MyPreWindow, self).__init__(parent)
        self.setupUi(self)
        self.setPalette(palette1)
        self.label.setScaledContents(True)
        self.label_para.setScaledContents(True)
        self.label_para.setPixmap(QtGui.QPixmap('para.png'))
        self.pushButton.clicked.connect(self.predict_btn)
        self.pushButton_2.clicked.connect(self.back_btn)

    def predict_btn(self):
        print()
        if self.lineEdit.text() == '':
            QMessageBox.warning(self, 'waining', '请输入对应参数后查看！', QMessageBox.Ok)
        else:
            num = self.lineEdit.text()
            a_project.fucc(num)
            print(kv.get_name(int(num)))
            self.label_tips.setText('你当前查看的是'+kv.get_name(int(num))+'的疫情情况')
            self.label.setPixmap(QtGui.QPixmap('pre.png'))

    def back_btn(self):
        self.close()
        self.win = MyMainWindow()
        self.win.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
