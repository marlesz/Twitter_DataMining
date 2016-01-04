# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wtyczka.ui'
#
# Created: Thu Dec 24 00:42:01 2015
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(850, 604)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        Form.setFont(font)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 460, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 120, 161, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 90, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 580, 581, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 560, 46, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 431, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 150, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 10, 161, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        #self.graphicsView = QtGui.QGraphicsView(Form)
        #self.graphicsView.setGeometry(QtCore.QRect(270, 110, 561, 441))
        #self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(460, 80, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 410, 131, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setValidator(QRegExpValidator(QtCore.QRegExp("\d*\.\d*")))




        self.comboBox2 = QtGui.QComboBox(Form)
        self.comboBox2.setGeometry(QtCore.QRect(20, 200, 161, 21))
        self.comboBox2.setObjectName(_fromUtf8("comboBox2"))
        self.comboBox2.addItem(_fromUtf8(""))
        self.comboBox2.addItem(_fromUtf8(""))
        self.label7 = QtGui.QLabel(Form)
        self.label7.setGeometry(QtCore.QRect(20, 170, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label7.setFont(font)
        self.label7.setObjectName(_fromUtf8("label7"))
        self.pushButton2 = QtGui.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(20, 250, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))

        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget.setGeometry(QtCore.QRect(270, 110, 561, 431))
        # self.widget.setAutoFillBackground(True)
        # p = self.widget.palette()
        # p.setColor(self.widget.backgroundRole(), QtCore.Qt.white)
        # self.widget.setPalette(p)
        self.widget.setStyleSheet("""
        .QWidget {
            border: 1px solid grey;
            background-color: rgb(255, 255, 255);
            }
        """)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Wykonaj", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "Metoda centroidów", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "Pojedyńcze wiązanie", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "Pełne wiązanie", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "Wiązanie średnich", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Metoda klasyfikacji", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Postęp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Słowa kluczowe", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "(słowo1,słowo2,słowo3...)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Dendrogram", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Cięcie", None, QtGui.QApplication.UnicodeUTF8))

        self.comboBox2.setItemText(0, QtGui.QApplication.translate("Form", "Odległość", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox2.setItemText(1, QtGui.QApplication.translate("Form", "Niespójność", None, QtGui.QApplication.UnicodeUTF8))
        self.label7.setText(QtGui.QApplication.translate("Form", "Kryterium", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton2.setText(QtGui.QApplication.translate("Form", "Oblicz", None, QtGui.QApplication.UnicodeUTF8))


    def pop(self):
        self.window = Ui_Form()
# def main():
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow() # <-- Instantiate QMainWindow object.
#     #global ui
#     ui = Ui_Form()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

    # pobieranie tekstu z lineEdit (słowa kluczowe) print ui.lineEdit.text()

