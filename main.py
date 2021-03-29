# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
import compress
import encode
# import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 450, 811, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 510, 811, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 390, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 390, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 420, 171, 21))
        self.label_5.setText("")
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.originLabel = QtWidgets.QLabel(self.centralwidget)
        self.originLabel.setGeometry(QtCore.QRect(150, 0, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.originLabel.setFont(font)
        self.originLabel.setObjectName("originLabel")
        self.compressLabel = QtWidgets.QLabel(self.centralwidget)
        self.compressLabel.setGeometry(QtCore.QRect(540, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.compressLabel.setFont(font)
        self.compressLabel.setObjectName("compressLabel")
        self.origin_display = QtWidgets.QLabel(self.centralwidget)
        self.origin_display.setGeometry(QtCore.QRect(20, 50, 351, 321))
        self.origin_display.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.origin_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.origin_display.setText("")
        self.origin_display.setObjectName("origin_display")
        self.compress_display = QtWidgets.QLabel(self.centralwidget)
        self.compress_display.setGeometry(QtCore.QRect(440, 50, 351, 321))
        self.compress_display.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.compress_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.compress_display.setText("")
        self.compress_display.setObjectName("compress_display")
        self.originSize = QtWidgets.QLabel(self.centralwidget)
        self.originSize.setGeometry(QtCore.QRect(70, 390, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.originSize.setFont(font)
        self.originSize.setFrameShape(QtWidgets.QFrame.Box)
        self.originSize.setObjectName("originSize")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 390, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 390, 67, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 390, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.openImage)
        self.pushButton_2.clicked.connect(self.compressImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open Image "))
        self.pushButton_2.setText(_translate("MainWindow", "compress "))
        self.label_3.setText(_translate("MainWindow", "Size: "))
        self.label_4.setText(_translate("MainWindow", "Size: "))
        self.originLabel.setText(_translate("MainWindow", "Origin "))
        self.compressLabel.setText(_translate("MainWindow", "Compress"))
        self.originSize.setText(_translate("MainWindow", "0.0"))
        self.label.setText(_translate("MainWindow", "0.0"))
        self.label_2.setText(_translate("MainWindow", "Kb"))
        self.label_6.setText(_translate("MainWindow", "Kb"))

    def openImage(self):
        self.image = QFileDialog.getOpenFileName(None, 'open file', '', "Image files (*.bmp *.png *.jpg)")
        self.imagePath = self.image[0]
        self.pixmap = QPixmap(self.imagePath)
        self.origin_display.setPixmap(self.pixmap.scaled(351,321))
        self.origin_display.adjustSize()      
        # self.setCentralWidget(origin_display)
        # self.resize(pixmap.width(), pixmap.height())                
        self.size = self.pixmap.width()*self.pixmap.height()/1024
        self.originSize.setText(str(self.size))
        #print(ocr.resimden_yaziya(imagePath))
        print(self.imagePath)
        
    def compressImage(self):
        # self.image = cv2.imread("emma.png", cv2.IMREAD_GRAYSCALE)
        print(self.image)
        self.bitstream = encode(self.image)
        self.image_compress = compress(self.bitstream)
        self.image_compress = QtGui.QImage(self.image_compress, self.image_compress.shape[1], self.image_compress.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.compress_display.setPixmap(QtGui.QPixmap.fromImage(self.image_compress))


        
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
