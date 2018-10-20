#
# Created by: BinanceWinner
# Version : 1.01
#

bw_version=1.01 #Version 
glo_email="" #Email
glo_password="" #Password
glo_info="" #Login information
active_trader_list = set() #Active Traders


import sys
import requests
import pandas as pd
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
#from main import Ui_MainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 304)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 141, 261))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 232))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        ########################TRADER BOXS#############################
        self.trader_box1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box1.setObjectName("trader_box1")
        self.verticalLayout_2.addWidget(self.trader_box1)
        self.trader_box1.hide()

        self.trader_box2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box2.setObjectName("trader_box2")
        self.verticalLayout_2.addWidget(self.trader_box2)
        self.trader_box2.hide()

        self.trader_box3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box3.setObjectName("trader_box3")
        self.verticalLayout_2.addWidget(self.trader_box3)
        self.trader_box3.hide()

        self.trader_box4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box4.setObjectName("trader_box3")
        self.verticalLayout_2.addWidget(self.trader_box4)
        self.trader_box4.hide()

        self.trader_box5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box5.setObjectName("trader_box5")
        self.verticalLayout_2.addWidget(self.trader_box5)
        self.trader_box5.hide()

        self.trader_box6 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box6.setObjectName("trader_box6")
        self.verticalLayout_2.addWidget(self.trader_box6)
        self.trader_box6.hide()


        self.trader_box7 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box7.setObjectName("trader_box7")
        self.verticalLayout_2.addWidget(self.trader_box7)
        self.trader_box7.hide()

        self.trader_box8 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box8.setObjectName("trader_box8")
        self.verticalLayout_2.addWidget(self.trader_box8)
        self.trader_box8.hide()

        self.trader_box9 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box9.setObjectName("trader_box9")
        self.verticalLayout_2.addWidget(self.trader_box9)
        self.trader_box9.hide()

        self.trader_box10 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.trader_box10.setObjectName("trader_box10")
        self.verticalLayout_2.addWidget(self.trader_box10)
        self.trader_box10.hide()

        ########################TRADER BOXS END#############################
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 10, 211, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.buy_limitorder_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.buy_limitorder_input.setGeometry(QtCore.QRect(83, 88, 21, 20))
        self.buy_limitorder_input.setObjectName("buy_limitorder_input")
        self.buy_limitorder = QtWidgets.QRadioButton(self.groupBox_2)
        self.buy_limitorder.setGeometry(QtCore.QRect(10, 90, 211, 17))
        self.buy_limitorder.setObjectName("buy_limitorder")
        self.buy_bestoffer = QtWidgets.QRadioButton(self.groupBox_2)
        self.buy_bestoffer.setGeometry(QtCore.QRect(10, 60, 111, 17))
        self.buy_bestoffer.setObjectName("buy_bestoffer")
        self.buy_marketbuy = QtWidgets.QRadioButton(self.groupBox_2)
        self.buy_marketbuy.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.buy_marketbuy.setObjectName("buy_marketbuy")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 110, 191, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 91, 16))
        self.label_2.setObjectName("label_2")
        self.buy_trader_dif = QtWidgets.QLineEdit(self.groupBox_2)
        self.buy_trader_dif.setGeometry(QtCore.QRect(100, 130, 16, 20))
        self.buy_trader_dif.setObjectName("buy_trader_dif")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(120, 132, 47, 13))
        self.label_6.setObjectName("label_6")
        self.buy_limitorder.raise_()
        self.buy_limitorder_input.raise_()
        self.buy_bestoffer.raise_()
        self.buy_marketbuy.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.buy_trader_dif.raise_()
        self.label_6.raise_()
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 180, 211, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.sell_bestoffer = QtWidgets.QRadioButton(self.groupBox_3)
        self.sell_bestoffer.setGeometry(QtCore.QRect(10, 60, 111, 17))
        self.sell_bestoffer.setObjectName("sell_bestoffer")
        self.sell_marketsell = QtWidgets.QRadioButton(self.groupBox_3)
        self.sell_marketsell.setGeometry(QtCore.QRect(10, 30, 161, 17))
        self.sell_marketsell.setObjectName("sell_marketsell")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 10, 291, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 281, 115))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(3, 10, 3, 10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.key_api = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.key_api.setObjectName("key_api")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.key_api)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.key_secret = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.key_secret.setObjectName("key_secret")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.key_secret)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.max_btc = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.max_btc.setObjectName("max_btc")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.max_btc)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(110, 132, 75, 31))
        self.pushButton.setStyleSheet("background-color:rgb(85, 170, 127);\n" "color: #FFF;")
        self.pushButton.setObjectName("pushButton")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(380, 180, 301, 91))
        self.groupBox_5.setObjectName("groupBox_5")
        self.status_area = QtWidgets.QTextEdit(self.groupBox_5)
        self.status_area.setGeometry(QtCore.QRect(10, 20, 281, 61))
        self.status_area.setObjectName("status_area")
        self.texti_problem = QtWidgets.QLabel(self.centralwidget)
        self.texti_problem.setGeometry(QtCore.QRect(10, 280, 141, 16))
        self.texti_problem.setOpenExternalLinks(True)
        self.texti_problem.setObjectName("texti_problem")
        self.texti_v1 = QtWidgets.QLabel(self.centralwidget)
        self.texti_v1.setGeometry(QtCore.QRect(650, 280, 47, 13))
        self.texti_v1.setObjectName("texti_v1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BinanceWinner Auto Trade Program - " + glo_email))
        self.groupBox.setTitle(_translate("MainWindow", "1. Trader Selection"))
        #self.trader_box1.setText(_translate("MainWindow", "CheckBox"))
        self.groupBox_2.setTitle(_translate("MainWindow", "2. Buy Settings"))
        self.buy_limitorder_input.setText(_translate("MainWindow", "99"))
        self.buy_limitorder.setText(_translate("MainWindow", "Limit Order        /100 (Trader Price)"))
        self.buy_bestoffer.setText(_translate("MainWindow", "Best Offer for Buy"))
        self.buy_marketbuy.setText(_translate("MainWindow", "Markey Buy"))
        self.label.setText(_translate("MainWindow", "-----------------------------------------------"))
        self.label_2.setText(_translate("MainWindow", "Trader Difference:"))
        self.buy_trader_dif.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "%"))
        self.groupBox_3.setTitle(_translate("MainWindow", "3. Sell Settings"))
        self.sell_bestoffer.setText(_translate("MainWindow", "Best Offer for Sell"))
        self.sell_marketsell.setText(_translate("MainWindow", "Market Sell"))
        self.groupBox_4.setTitle(_translate("MainWindow", "4. Genereal Settings and Run"))
        self.label_3.setText(_translate("MainWindow", "Binance Api Key:"))
        self.label_4.setText(_translate("MainWindow", "Binance Secret Key: "))
        self.label_5.setText(_translate("MainWindow", "Max.Allocated  BTC :"))
        self.max_btc.setText(_translate("MainWindow", "0.5"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton.clicked.connect(self.run_button)
        self.groupBox_5.setTitle(_translate("MainWindow", "Status"))
        self.texti_problem.setText(
            _translate("MainWindow", "<html><head/><body><p>2018 © BinanceWinner.com</p></body></html>"))
        self.texti_v1.setText(_translate("MainWindow", "v" + str(bw_version)))

        ###Start Main codes

        print(glo_info)
        a=1
        for b in glo_info["trader_name"]:
            if a==1:
                self.trader_box1.setText(_translate("MainWindow", str(b)))
                self.trader_box1.show()
            elif a==2:
                self.trader_box2.setText(_translate("MainWindow", str(b)))
                self.trader_box2.show()
            elif a==3:
                self.trader_box3.setText(_translate("MainWindow", str(b)))    
                self.trader_box3.show()
            elif a == 4:
                self.trader_box4.setText(_translate("MainWindow", str(b)))
                self.trader_box4.show()
            elif a==5:
                self.trader_box5.setText(_translate("MainWindow", str(b)))
                self.trader_box5.show()
            elif a == 6:
                self.trader_box6.setText(_translate("MainWindow", str(b)))
                self.trader_box6.show()
            elif a == 7:
                self.trader_box7.setText(_translate("MainWindow", str(b)))
                self.trader_box7.show()
            elif a == 8:
                self.trader_box8.setText(_translate("MainWindow", str(b)))
                self.trader_box8.show()
            elif a == 9:
                self.trader_box9.setText(_translate("MainWindow", str(b)))
                self.trader_box9.show()
            elif a == 10:
                self.trader_box10.setText(_translate("MainWindow", str(b)))
                self.trader_box10.show()
            a += 1
            #self.trader_box10.stateChanged.connect(self.clickBox)


        #self.checks_add =  QtWidgets.QCheckBox(self.verticalLayoutWidget)
        #self.checks_add.setObjectName("checks_add")
        #self.checks_add = self.checks_add+self.verticalLayout_2.addWidget(self.checks_add)
        
    def run_button(self):
        if self.pushButton.text()=="Run":
            self.pushButton.setText("Stop")
            self.pushButton.setStyleSheet("background-color:rgb(252, 76, 76);\n" "color: #FFF;")
            print("Start")
            self.trader_box2.setChecked(True)
            global active_trader_list
            if self.trader_box1.isChecked()== True:
                active_trader_list.add(self.trader_box1.text())
            #print(active_trader_list)
            if self.trader_box2.isChecked()== True:
                active_trader_list.add(self.trader_box2.text())
            if self.trader_box3.isChecked()== True:
                active_trader_list.add(self.trader_box3.text())
            if self.trader_box4.isChecked()== True:
                active_trader_list.add(self.trader_box4.text())
            if self.trader_box5.isChecked()== True:
                active_trader_list.add(self.trader_box5.text())
            if self.trader_box6.isChecked()== True:
                active_trader_list.add(self.trader_box6.text())
            if self.trader_box7.isChecked()== True:
                active_trader_list.add(self.trader_box7.text())
            if self.trader_box8.isChecked()== True:
                active_trader_list.add(self.trader_box8.text())
            if self.trader_box9.isChecked()== True:
                active_trader_list.add(self.trader_box9.text())
            if self.trader_box10.isChecked()== True:
                active_trader_list.add(self.trader_box10.text())
            print(active_trader_list)



            self.trader_box1.setEnabled(False)
            self.trader_box2.setEnabled(False)
            self.trader_box3.setEnabled(False)
            self.trader_box4.setEnabled(False)
            self.trader_box5.setEnabled(False)
            self.trader_box6.setEnabled(False)
            self.trader_box7.setEnabled(False)
            self.trader_box8.setEnabled(False)
            self.trader_box9.setEnabled(False)
            self.trader_box10.setEnabled(False)
        else:
            self.pushButton.setText("Run")
            self.pushButton.setStyleSheet("background-color:rgb(85, 170, 127);\n" "color: #FFF;")
            print("Stop")
            
            
            active_trader_list = None
            active_trader_list = set()
            self.trader_box1.setEnabled(True)
            self.trader_box2.setEnabled(True)
            self.trader_box3.setEnabled(True)
            self.trader_box4.setEnabled(True)
            self.trader_box5.setEnabled(True)
            self.trader_box6.setEnabled(True)
            self.trader_box7.setEnabled(True)
            self.trader_box8.setEnabled(True)
            self.trader_box9.setEnabled(True)
            self.trader_box10.setEnabled(True)



        #print(self.pushButton.text())
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(249, 249)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 0, 181, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setObjectName("label")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 80, 211, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.texti_email = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.texti_email.setStyleSheet("font: bold 12pt \"Arial\";\n" "color : black;")
        self.texti_email.setObjectName("texti_email")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.texti_email)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.texti_password = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.texti_password.setStyleSheet("color: rgb(30, 30, 30);\n" "font: bold 12pt \"Arial\";\n" "")
        self.texti_password.setObjectName("texti_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.texti_password)
        self.input_password = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_password)
        self.btn_login = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.btn_login.setObjectName("btn_login")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_login)
        self.texti_problem = QtWidgets.QLabel(Dialog)
        self.texti_problem.setGeometry(QtCore.QRect(70, 210, 121, 16))
        self.texti_problem.setOpenExternalLinks(True)
        self.texti_problem.setObjectName("texti_problem")
        self.text_login_error = QtWidgets.QLabel(Dialog)
        self.text_login_error.setGeometry(QtCore.QRect(20, 180, 211, 20))
        self.text_login_error.setStyleSheet("color:rgb(255, 0, 0);\n" "font: 87 10pt \"Arial Black\";")
        self.text_login_error.setText("")
        self.text_login_error.setObjectName("text_login_error")
        self.texti_copyright = QtWidgets.QLabel(Dialog)
        self.texti_copyright.setGeometry(QtCore.QRect(10, 230, 141, 16))
        self.texti_copyright.setObjectName("texti_copyright")
        self.texti_v1 = QtWidgets.QLabel(Dialog)
        self.texti_v1.setGeometry(QtCore.QRect(210, 230, 47, 13))
        self.texti_v1.setObjectName("texti_v1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        self.btn_login.clicked.connect(self.login_click)
        
    
    def login_click(self):
        self.Login_error = False
        self.Login_error_msg = 0
        in_email=self.lineEdit_3.text()
        in_passwd=self.input_password.text()
        
        global bw_version
        v_check=requests.get("https://www.binancewinner.com/engine/trade_version.txt")
        if (v_check.text!=str(bw_version)):
           self.Login_error = True
           self.Login_error_msg = "Please Update Program"
           self.text_login_error.setText(self.Login_error_msg)
           in_email=""
           
        
        if (in_email!="" and in_passwd!=""):
            url_bw="http://www.binancewinner.com/engine/trader-api.php?email="+in_email+"&password="+in_passwd
            response=requests.get(url_bw)
            if(response.status_code !=200):
                self.text_login_error.setText("BinanceWinner is offline")
            else:
                login_json=pd.DataFrame(response.json())
                try:
                    if(login_json.columns.values=="error"):
                        self.Login_error = True
                        lgn_err_code=login_json.iloc[:,0:1].values
                        if (lgn_err_code==0):
                            self.Login_error_msg="Fill in all fields"
                        elif (lgn_err_code==1):
                            self.Login_error_msg="Invalid e-mail and password"
                        elif (lgn_err_code==1):
                            self.Login_error_msg="Please Upgrade Plus member"
                        self.text_login_error.setText(self.Login_error_msg)
                    else:
                        print("Success")
                except KeyError:     
                    sys.stderr.write("")
                    sys.stderr.flush()
                except ValueError:     
                    sys.stderr.write("")
                    sys.stderr.flush()
                if self.Login_error==False:
                    print("Giriş")
                    ##Main Enter
                    global glo_email
                    global glo_password
                    global glo_info
                    glo_email=in_email
                    glo_password=in_passwd
                    glo_info=login_json
                    Dialog.hide()

                    self.main_enter =  QtWidgets.QMainWindow()

                    self.ui = Ui_MainWindow()
                    self.ui.setupUi(self.main_enter)
                    self.main_enter.show()
                    
                    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BinanceWinner Auto Trade"))
        self.texti_email.setText(_translate("Dialog", "E-mail:"))
        self.texti_password.setText(_translate("Dialog", "Password:"))
        self.btn_login.setText(_translate("Dialog", "Login"))
        self.texti_problem.setText(_translate("Dialog", "<a href=\'https://www.binancewinner.com\'>Do you have a problem ?</a>"))
        self.texti_copyright.setText(_translate("Dialog", "2018 © BinanceWinner.com"))
        self.texti_v1.setText(_translate("Dialog", "v"+str(bw_version)))
        
        ####### Kaldır
        self.lineEdit_3.setText(_translate("Dialog", "rcpyksl@gmail.com"))
        self.input_password.setText(_translate("Dialog", "asdasd123"))


if __name__ == "__main__":
    
    app = QCoreApplication.instance()
    if app is None:
         app = QtWidgets.QApplication(sys.argv)
    
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
    #sys.exit(app.exec_())
    #sys.exit(app.exec_())








