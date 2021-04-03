# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton, QMessageBox, QCheckBox, QSpinBox
from PyQt5.QtGui import QIcon, QPixmap
from huffman import *
from compress import *
# import encode
import cv2
import math
import numpy as np
import zigzag
from encode import *
import time 
import compress_RLE
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UET Image Compressor")
        MainWindow.resize(1041, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 281, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 130, 281, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 410, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 410, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.originLabel = QtWidgets.QLabel(self.centralwidget)
        self.originLabel.setGeometry(QtCore.QRect(430, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.originLabel.setFont(font)
        self.originLabel.setObjectName("originLabel")
        self.compressLabel = QtWidgets.QLabel(self.centralwidget)
        self.compressLabel.setGeometry(QtCore.QRect(790, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.compressLabel.setFont(font)
        self.compressLabel.setObjectName("compressLabel")
        self.origin_display = QtWidgets.QLabel(self.centralwidget)
        self.origin_display.setGeometry(QtCore.QRect(300, 60, 351, 331))
        self.origin_display.setAutoFillBackground(True)
        self.origin_display.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.origin_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.origin_display.setText("")
        self.origin_display.setObjectName("origin_display")
        self.compress_display = QtWidgets.QLabel(self.centralwidget)
        self.compress_display.setGeometry(QtCore.QRect(680, 60, 351, 331))
        self.compress_display.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.compress_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.compress_display.setText("")
        self.compress_display.setObjectName("compress_display")
        self.originSize = QtWidgets.QLabel(self.centralwidget)
        self.originSize.setGeometry(QtCore.QRect(370, 410, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.originSize.setFont(font)
        self.originSize.setFrameShape(QtWidgets.QFrame.Box)
        self.originSize.setObjectName("originSize")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(740, 410, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 410, 67, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(860, 410, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 200, 281, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 300, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 300, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 340, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 340, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 370, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(90, 370, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 450, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(150, 470, 48, 26))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.show_result)
        # self.label_13 = QtWidgets.QLabel(self.centralwidget)
        # self.label_13.setGeometry(QtCore.QRect(400, 460, 101, 17))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_13.setFont(font)
        # self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        # self.label_13.setText("")
        # self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(680, 450, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        # self.label_15 = QtWidgets.QLabel(self.centralwidget)
        # self.label_15.setGeometry(QtCore.QRect(770, 460, 101, 17))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_15.setFont(font)
        # self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        # self.label_15.setText("")
        # self.label_15.setObjectName("label_15")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 410, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 440, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1041, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.openImage)
        self.pushButton_2.clicked.connect(self.compressImage)
        self.pushButton_3.clicked.connect(self.saveImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open Image "))
        self.pushButton_2.setText(_translate("MainWindow", "Compress "))
        self.label_3.setText(_translate("MainWindow", "Size: "))
        self.label_4.setText(_translate("MainWindow", "Size: "))
        self.originLabel.setText(_translate("MainWindow", "Origin "))
        self.compressLabel.setText(_translate("MainWindow", "Compress"))
        self.originSize.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Kb"))
        self.label_6.setText(_translate("MainWindow", "Kb"))
        self.pushButton_3.setText(_translate("MainWindow", "Save Image Compress "))
        self.label_7.setText(_translate("MainWindow", "Time: "))
        self.label_9.setText(_translate("MainWindow", "PSNR:"))
        self.label_11.setText(_translate("MainWindow", "Rate:"))
        # self.label_5.setText(_translate("MainWindow", "Entropy:"))
        # self.label_14.setText(_translate("MainWindow", "Entropy: "))
        self.checkBox.setText(_translate("MainWindow", "RLE"))
        self.checkBox_2.setText(_translate("MainWindow", "Huffman"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.label_16.setText(_translate("MainWindow", "Quatization: "))
        


    def openImage(self):
        self.image = QFileDialog.getOpenFileName(None, 'open file', '', "Image files (*.bmp *.png *.jpg)")
        self.imagePath = self.image[0]
        org_img = cv2.imread(self.imagePath, 0)
        self.pixmap = QPixmap(self.imagePath)
        self.origin_display.setPixmap(self.pixmap.scaled(351,331))
        self.origin_display.adjustSize()      
        # self.setCentralWidget(origin_display)
        # self.resize(pixmap.width(), pixmap.height())                
        self.size = self.pixmap.width()*self.pixmap.height()/1024
        self.originSize.setText(str(self.size))
        #print(ocr.resimden_yaziya(imagePath))
        print(self.imagePath)
        #caculator entopy
        # self.entropy = self.caculator_Entropy(org_img)
        # self.entropy = round(self.entropy, 5)
        # self.label_13.setText(str(self.entropy))

    def compressImage(self):
        start = time.time()
        quantization = self.spinBox.value()
        print(quantization)
        # self.image = cv2.imread("emma.png", cv2.IMREAD_GRAYSCALE)
        self.image = cv2.imread(self.imagePath, 0)
        self.image = cv2.resize(self.image,(351, 331))
        
        encoded_text1, bitstream = encode(self.image, quantization)
        if (self.checkBox_2.isChecked()):
            encoded_text = encoded_text1
            self.image_compress = compress(encoded_text, quantization)
        else:
            encoded_text = bitstream
            self.image_compress = compress_RLE.compress_RLE(bitstream, quantization)
        # cv2.imwrite("test.png", image_compress)
        # cv2.imwrite("test1.png", padd_image)


        image_compress_display = QtGui.QImage(self.image_compress, self.image_compress.shape[1], self.image_compress.shape[0], self.image_compress.shape[1], QtGui.QImage.Format_Indexed8)
        self.compress_display.setPixmap(QtGui.QPixmap.fromImage(image_compress_display))
       
        size_compress = (len(encoded_text)-5)*8/8/1024
        #lam tron den 5 so sau thap phan 
        size_compress = round(size_compress, 5)
        self.label.setText(str(size_compress))
        self.image_compress = cv2.resize(self.image_compress, (self.image.shape[1], self.image.shape[0]))
        self.image_compress = cv2.bilateralFilter(self.image_compress, 9,75,75)
        #caculator mse
        mse = np.square(self.image-self.image_compress).mean()
        mse = round(mse, 5)
        psnr = 10*(np.log10((255*255)/mse))
        psnr = round(psnr, 5)
        self.label_10.setText(str(psnr))

        # #caculator entropy for image compressed 
        # self.entropy_new = self.caculator_Entropy(self.image_compress)
        # self.entropy_new = round(self.entropy_new, 5)
        # self.label_15.setText(str(self.entropy_new))

        #caculator rate commpress 
        rate = 1 - (len(encoded_text)-5)*8/(512*512*8)
        rate = round(rate, 5)
        self.label_12.setText(str(rate))
        #caculator time compress
        _time = round(time.time()-start, 5)
        self.label_8.setText(str(_time)+ 's')

        

        # cv2.imshow("hah", image_compress)
        # cv2.waitKey()

    def saveImage(self):
        #self.image_compress = cv2.resize(self.image_compress, (512, 512))
        cv2.imwrite("image_compress_15.png", self.image_compress)
        msg = QMessageBox()
        msg.setWindowTitle("Image Compress")
        msg.setText("Image Saved!!!")
        
        x = msg.exec_()

    def caculator_Entropy(self, img):
        marg = np.histogramdd(np.ravel(img), bins=256)[0] / img.size
        marg = list(filter(lambda p: p > 0, np.ravel(marg)))
        entropy = -np.sum(np.multiply(marg, np.log2(marg)))
        return entropy

    def show_result(self):
        quantization = self.spinBox.value()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

