import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import os
from PyQt5.QtWidgets import QWidget, QTextEdit, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QFileDialog

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(682, 643)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(190, 36, 381, 31))
        self.textEdit.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.textEdit_2 = QtWidgets.QLineEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 136, 381, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(190, 220, 381, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(190, 310, 381, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 360, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(190, 370, 381, 111))
        self.textEdit_5.setObjectName("textEdit_5")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 490, 381, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(190, 560, 381, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.yaziyi_temizle)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_3.clicked.connect(self.gonder)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "E-posta Gönderme"))
        self.label.setText(_translate("Form", "Gönderici e-posta:"))
        self.label_2.setText(_translate("Form", "Parola:"))
        self.label_3.setText(_translate("Form", "Alıcı e-posta:"))
        self.label_4.setText(_translate("Form", "Konu:"))
        self.label_5.setText(_translate("Form", "Mesaj:"))
        self.pushButton_2.setText(_translate("Form", "Temizle"))
        self.pushButton.setText(_translate("Form", "Aç"))
        self.pushButton_3.setText(_translate("Form", "Gönder"))

    def yaziyi_temizle(self):
        self.textEdit_5.clear()

    def open(self):
        try:
            FileName = QFileDialog.getOpenFileName(None, "Open File", os.getenv("HOME"))

            with open(FileName[0], 'r') as File:
                self.textEdit_5.setText(File.read())

        except FileNotFoundError:
            pass

    def gonder(self):

        mesaj = MIMEMultipart()

        mesaj["From"] = self.textEdit.toPlainText()#

        parola = self.textEdit_2.text()


        mesaj["To"] = self.textEdit_3.toPlainText()#

        mesaj["Subject"] = self.textEdit_4.toPlainText()#

        yazi = self.textEdit_5.toPlainText()#

        mesaj_govdesi = MIMEText(yazi, "plain")#

        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.ehlo()

            mail.starttls()

            mail.login(self.textEdit.toPlainText(), self.textEdit_2.text())#

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

            print("Mail başarıyla gönderildi...")
            self.textEdit_5.setText("Mail başarıyla gönderildi...")

            mail.close()

        except:
            print("Mail göndermesi başarısız oldu.")
            self.textEdit_5.setText("Mail göndermesi başarısız oldu.")







app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())

