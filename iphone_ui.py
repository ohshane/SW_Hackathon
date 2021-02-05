import os, sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.setObjectName("Iphone_Instagram")
        self.resize(448, 875)
        self.setFixedSize(448, 875)
        self.setStyleSheet("background-color: rgb(225, 225, 225);")

        # ********** ********** label_2 ********** **********
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 461, 881))
        self.label_2.setStyleSheet("image: url(iphone_instagram2.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")


        # ********** ********** label ********** **********
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 230, 361, 361))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")


        # ********** ********** pushButton ********** **********
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(420, 860, 21, 20))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "image: url(Button.JPG);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.NextImage)


        # ********** ********** Execute ********** **********
        self.center()  # ** 창을 화면의 정 가운데에 위치 **
        self.show()


        self.number = 0
        self.filename = str(self.number) + ".jpg"
        image = QtGui.QImage(self.filename)
        if image.width() > 361:
            image = image.scaledToWidth(361)
        if image.height() > 361:
            image = image.scaledToHeight(361)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        self.time = QTime.currentTime()
        self.start = self.time.toString('hh.mm.ss.zzz')



    def TimeCheck(self):
        json_data[filename]['time'] = total
        # if 좋아요 버튼을 눌렀을때
        if (json_data[filename]['likes'] == 1):
            # 이미 한번 누른경우, 초기화 (0)
            json_data[filename]['likes'] = 0
        else:  # 좋아요가 처음인 경우에 좋아요 수 갱신
            json_data[filename]['likes'] = 1
            tag_name = json_data[filename]['tag']
            tag_json[tag_name]['likes'] += 1


    def NextImage(self):

        self.time = QTime.currentTime()
        self.end = self.time.toString('hh.mm.ss.zzz')

        start_hour = int(self.start[:2])
        end_hour = int(self.end[:2])
        start_min = int(self.start[3:5])
        end_min = int(self.end[3:5])
        start_sec = int(self.start[6:8])
        end_sec = int(self.end[6:8])
        start_zz = int(self.start[9:11])
        end_zz = int(self.end[9:11])

        total_sec = 0
        total_zz = 0

        if start_zz > end_zz:
            end_sec -= 1
            end_zz += 100
        total_zz += (end_zz - start_zz)

        if (end_sec == -1):
            end_sec += 1
        if start_sec > end_sec:
            end_min -= 1
            end_sec += 60
        total_sec += (end_sec - start_sec)

        if (end_min == -1):
            end_min += 1
        if start_min > end_min:
            end_hour -= 1
            end_min += 60
        total_sec += (end_min - start_min) * 60
        total_sec += (end_hour - start_hour) * 3600

        total = str(total_sec) + "." + str(total_zz)
        print(self.filename, "/", total)


        self.time = QTime.currentTime()
        self.start = self.time.toString('hh.mm.ss.zzz')


        if self.number < 40:
            self.number = self.number + 10
        else:
            self.number = self.number - 39

        self.filename = str(self.number) + ".jpg"
        image = QtGui.QImage(self.filename)
        if image.width() > 361:
            image = image.scaledToWidth(361)
        if image.height() > 361:
            image = image.scaledToHeight(361)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))



    def center(self):
        ct = self.frameGeometry()
        ct2 = QtWidgets.QDesktopWidget().availableGeometry().center()
        ct.moveCenter(ct2)
        self.move(ct.topLeft())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

