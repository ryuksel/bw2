#
# Created by: BinanceWinner
# Version : 1.01
#


##Global vars
bw_version=1.01 #Version 
glo_email="" #Email
glo_password="" #Password
glo_info="" #Login information
active_trader_list = set() #Active Traders
buy_choice= int
buy_choice_limit_order= float
buy_diff = float
sell_choice= int
win32_dl = 0
min_btc = float(0.002)
show_pd=""

import sys
import requests
import pandas as pd
from decimal import Decimal
import math
#import time
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#from PyQt5.QtCore import QTime, QTimer
from binance.client import Client
import sqlite3
import time
try:
    import win32api
    win32_dl=1
except:
    win32_dl=0
#from main import Ui_MainWindow


class Ui_MainWindow(object):
    def __init__(self):
        object.__init__(self)
    def setupUi(self, MainWindow):
        self.window = MainWindow
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
        self.buy_limitorder_input.setGeometry(QtCore.QRect(83, 90, 28, 17))
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
        self.buy_trader_dif.setGeometry(QtCore.QRect(100, 130, 22, 16))
        self.buy_trader_dif.setObjectName("buy_trader_dif")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(124, 132, 47, 13))
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
        self.sell_bestoffer.setGeometry(QtCore.QRect(10, 40, 111, 17))
        self.sell_bestoffer.setObjectName("sell_bestoffer")
        self.sell_marketsell = QtWidgets.QRadioButton(self.groupBox_3)
        self.sell_marketsell.setGeometry(QtCore.QRect(10, 20, 161, 17))
        self.sell_marketsell.setObjectName("sell_marketsell")
        
        self.label_sellwq = QtWidgets.QLabel(self.groupBox_3)
        self.label_sellwq.setGeometry(QtCore.QRect(10, 55, 191, 16))
        self.label_2x = QtWidgets.QLabel(self.groupBox_3)
        self.label_2x.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_2x.setObjectName("label_2x")
        self.sell_stoploss = QtWidgets.QLineEdit(self.groupBox_3)
        self.sell_stoploss.setGeometry(QtCore.QRect(80, 70, 28, 16))
        self.sell_stoploss.setObjectName("sell_stoploss")
        self.label_6x = QtWidgets.QLabel(self.groupBox_3)
        self.label_6x.setGeometry(QtCore.QRect(110, 72, 47, 13))
        self.label_6x.setObjectName("label_6x")

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
        
        self.save_changes = QtWidgets.QCheckBox(self.groupBox_4)
        self.save_changes.setGeometry(QtCore.QRect(15, 102, 95, 31))
        self.save_changes.setObjectName("save_changes")
        
        
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
        self.buy_limitorder.setText(_translate("MainWindow", "Limit Order          % (Trader Price)"))
        self.buy_bestoffer.setText(_translate("MainWindow", "Best Offer for Buy"))
        self.buy_marketbuy.setText(_translate("MainWindow", "Markey Buy"))
        self.label.setText(_translate("MainWindow", "-----------------------------------------------"))
        self.label_2.setText(_translate("MainWindow", "Trader Difference:"))

        self.label_6.setText(_translate("MainWindow", "%"))
        self.groupBox_3.setTitle(_translate("MainWindow", "3. Sell Settings"))
        self.sell_bestoffer.setText(_translate("MainWindow", "Best Offer for Sell"))
        self.sell_marketsell.setText(_translate("MainWindow", "Market Sell"))
        self.label_sellwq.setText(_translate("MainWindow", "-----------------------------------------------"))
        self.label_2x.setText(_translate("MainWindow", "Stoploss Limit:"))
        self.label_6x.setText(_translate("MainWindow", "%"))

        self.groupBox_4.setTitle(_translate("MainWindow", "4. Genereal Settings and Run"))
        self.label_3.setText(_translate("MainWindow", "Binance Api Key:"))
        self.label_4.setText(_translate("MainWindow", "Binance Secret Key: "))
        self.label_5.setText(_translate("MainWindow", "Max.Allocated  BTC :"))
        self.save_changes.setText(_translate("MainWindow","Save Changes"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton.clicked.connect(self.run_button)
        self.groupBox_5.setTitle(_translate("MainWindow", "Status"))
        self.texti_problem.setText(
            _translate("MainWindow", "<html><head/><body><p>2018 © BinanceWinner.com</p></body></html>"))
        self.texti_v1.setText(_translate("MainWindow", "v" + str(bw_version)))

        ###Load Save Changes
        con = sqlite3.connect("bw_db.db")
        cursor = con.cursor()
        cursor.execute("Select * From save_settings")
        save_data = cursor.fetchall()
        load_trader=save_data[0][0]
        load_buy_method=save_data[0][1]
        load_buy_diff = save_data[0][2]
        load_buy_limit_field = save_data[0][3]
        load_sell_method = save_data[0][4]
        load_sell_stoploss = save_data[0][5]
        load_api_key= save_data[0][6]
        load_secret_key = save_data[0][7]
        load_max_btc = save_data[0][8]
        con.close()

        if load_trader is not None:
            load_trader = load_trader.replace("{","")
            load_trader = load_trader.replace("}", "")
            load_trader = load_trader.replace("'", "")
            trader_split = load_trader.split(",")
        else:
            trader_split = list()
        if load_buy_method is not None:
            if int(load_buy_method)==1:
                self.buy_marketbuy.setChecked(True)
            elif int(load_buy_method)==2:
                self.buy_bestoffer.setChecked(True)
            else:
                self.buy_limitorder.setChecked(True)
        else:
            self.buy_marketbuy.setChecked(True)
        if load_buy_limit_field is not None:
            self.buy_limitorder_input.setText(_translate("MainWindow", str(load_buy_limit_field)))
        else:
            self.buy_limitorder_input.setText(_translate("MainWindow", "99"))
        if load_buy_diff is not None:
            self.buy_trader_dif.setText(_translate("MainWindow", str(load_buy_diff)))
        else:
            self.buy_trader_dif.setText(_translate("MainWindow", "1.0"))
        if load_sell_method is not None:
            if int(load_sell_method)==1:
                self.sell_marketsell.setChecked(True)
            else:
                self.sell_bestoffer.setChecked(True)
        else:
            self.sell_marketsell.setChecked(True)
        if load_sell_stoploss is not None:
            self.sell_stoploss.setText(_translate("MainWindow", str(load_sell_stoploss)))
        else:
            self.sell_stoploss.setText(_translate("MainWindow", "10"))
        if load_api_key is not None:
            self.key_api.setText(_translate("MainWindow", str(load_api_key)))
        else:
            self.key_api.setText(_translate("MainWindow", ""))
        if load_secret_key is not None:
            self.key_secret.setText(_translate("MainWindow", str(load_secret_key)))
        else:
            self.key_secret.setText(_translate("MainWindow", ""))
        if load_max_btc is not None:
            self.max_btc.setText(_translate("MainWindow", str(load_max_btc)))
        else:
            self.max_btc.setText(_translate("MainWindow", "0.5"))



        ###Start Main codes
        a=1
        for b in glo_info["trader_name"]:
            if a==1:
                self.trader_box1.setText(_translate("MainWindow", str(b)))
                self.trader_box1.show()
                if any(b in s for s in trader_split):
                    self.trader_box1.setChecked(True)
            elif a==2:
                self.trader_box2.setText(_translate("MainWindow", str(b)))
                self.trader_box2.show()
                if any(b in s for s in trader_split):
                    self.trader_box2.setChecked(True)
            elif a==3:
                self.trader_box3.setText(_translate("MainWindow", str(b)))    
                self.trader_box3.show()
                if any(b in s for s in trader_split):
                    self.trader_box3.setChecked(True)
            elif a == 4:
                self.trader_box4.setText(_translate("MainWindow", str(b)))
                self.trader_box4.show()
                if any(b in s for s in trader_split):
                    self.trader_box4.setChecked(True)
            elif a==5:
                self.trader_box5.setText(_translate("MainWindow", str(b)))
                self.trader_box5.show()
                if any(b in s for s in trader_split):
                    self.trader_box5.setChecked(True)
            elif a == 6:
                self.trader_box6.setText(_translate("MainWindow", str(b)))
                self.trader_box6.show()
                if any(b in s for s in trader_split):
                    self.trader_box6.setChecked(True)
            elif a == 7:
                self.trader_box7.setText(_translate("MainWindow", str(b)))
                self.trader_box7.show()
                if any(b in s for s in trader_split):
                    self.trader_box7.setChecked(True)
            elif a == 8:
                self.trader_box8.setText(_translate("MainWindow", str(b)))
                self.trader_box8.show()
                if any(b in s for s in trader_split):
                    self.trader_box8.setChecked(True)
            elif a == 9:
                self.trader_box9.setText(_translate("MainWindow", str(b)))
                self.trader_box9.show()
                if any(b in s for s in trader_split):
                    self.trader_box9.setChecked(True)
            elif a == 10:
                self.trader_box10.setText(_translate("MainWindow", str(b)))
                self.trader_box10.show()
                if any(b in s for s in trader_split):
                    self.trader_box10.setChecked(True)
            a += 1
            #self.trader_box10.stateChanged.connect(self.clickBox)


        #self.checks_add =  QtWidgets.QCheckBox(self.verticalLayoutWidget)
        #self.checks_add.setObjectName("checks_add")
        #self.checks_add = self.checks_add+self.verticalLayout_2.addWidget(self.checks_add)
        self.timer = QtCore.QTimer(self.window)
        self.timer.timeout.connect(self.showTime)        
    def run_button(self):
        
        if self.pushButton.text()=="Run":

            #######Trader selections
            global active_trader_list
            if self.trader_box1.isChecked()== True:
                active_trader_list.add(self.trader_box1.text())
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
            
            
            


            ####Buy choice            
            global buy_choice
            if self.buy_marketbuy.isChecked()== True:
                buy_choice = 1 
            elif self.buy_bestoffer.isChecked()== True:
                buy_choice = 2 
            elif self.buy_limitorder.isChecked()== True:
                buy_choice = 3
            global buy_diff
            buy_diff = self.buy_trader_dif.text()
            global buy_choice_limit_order
            buy_choice_limit_order = self.buy_limitorder_input.text()



            ####Sell Choice
            global sell_choice
            if self.sell_marketsell.isChecked() == True:
                sell_choice = 1
            elif self.sell_bestoffer.isChecked() == True:
                sell_choice = 2



            ####Save changes
            if self.save_changes.isChecked()== True:
                a_t_list=repr(active_trader_list)
                con = sqlite3.connect("bw_db.db")
                cursor = con.cursor()
                cursor.execute("UPDATE save_settings set trader_selector=(?) , buy_method = (?) , buy_diff = (?) , buy_limit_field = (?) , sell_method = (?) , sell_stoploss = (?) , api_key = (?) , secret_key = (?) , max_btc = (?)",[a_t_list, buy_choice, buy_diff, buy_choice_limit_order, sell_choice, self.sell_stoploss.text(), self.key_api.text(), self.key_secret.text(), self.max_btc.text()])
                con.commit()
                con.close()
           

            ##### RUN checks
            
            val_key_api=self.key_api.text().replace(",",".")
            val_key_secret=self.key_secret.text().replace(",",".")
            val_max_btc=self.max_btc.text().replace(",",".")
            sell_stoploss=self.sell_stoploss.text().replace(",",".")
            
            run_error=0
            try_binance=0
            if len(active_trader_list)==0:
                run_error=1
                run_error_msg="Please select trader(s)"
            else:
                if (buy_choice!=1 and buy_choice!=2 and buy_choice!=3):
                    run_error=1
                    run_error_msg="Please Choose Your Buy Method"
                else:
                    if (buy_choice==3 and (float(buy_choice_limit_order)<80 or float(buy_choice_limit_order)>101)):
                        run_error=1
                        run_error_msg="Please enter the correct value for the limit order"
                    else:
                        if (float(buy_diff)<0 or float(buy_diff)>5):
                            run_error=1
                            run_error_msg="Trader Difference must be between 0 and 5"
                        else:
                            if (sell_choice!=1 and sell_choice!=2):
                                run_error=1
                                run_error_msg="Please Choose Your Sell Method"
                            else:
                                if (val_key_api=="" or val_key_secret==""):
                                    run_error=1
                                    run_error_msg="Please Fill in Your Key Api and Key Secret"
                                else:
                                    
                                    if (float(val_max_btc)<0.01):
                                        run_error=1
                                        run_error_msg="Max.Allocated BTC must be greater than 0.01 BTC"
                                    else:
                                        if float(sell_stoploss)<1:
                                            run_error=1
                                            run_error_msg="Stoploss must be more than 1 %"
                                        else:
                                            if (run_error==0):
                                                try_binance=1
                                            else:
                                                run_error=1
                                                run_error_msg="Please fill in all fields correctly"
                                        
            
            binance_error=0
            binance_error_msg=""
            if try_binance==1:

                ##Binance Login try
                try: 
                    self.client = Client(self.key_api.text(), self.key_secret.text())
                    acc_info = self.client.get_account()
                    balance = self.client.get_asset_balance(asset='BTC')
                    if acc_info["canTrade"]==True:
                        binance_error=0
                except Exception as e:
                    print( str(e))
                    if win32_dl==1:
                        try:
                            gt = self.client.get_server_time()
                            aa = str(gt)
                            bb = aa.replace("{'serverTime': ","")
                            aa = bb.replace("}","")
                            gg=int(aa)
                            ff=gg-10799260
                            uu=ff/1000
                            yy=int(uu)
                            tt=time.localtime(yy)
                            win32api.SetSystemTime(tt[0],tt[1],0,tt[2],tt[3],tt[4],tt[5],0)
                        except:
                            print("burdan")
                            binance_error=1
                            binance_error_msg="Please Fill in Your Key Api and Key Secret Correctly"
                    else:
                        print("burdan2")
                        binance_error=1
                        binance_error_msg="Please Fill in Your Key Api and Key Secret Correctly"
                    
                     
            if run_error==1:
               msgBox = QMessageBox()
               msgBox.setText(run_error_msg)    
               msgBox.setStandardButtons(QMessageBox.Ok)
               msgBox.setDefaultButton(QMessageBox.Ok)
               ret = msgBox.exec_()
            elif binance_error==1:
               msgBox = QMessageBox()
               msgBox.setText(binance_error_msg)    
               msgBox.setStandardButtons(QMessageBox.Ok)
               msgBox.setDefaultButton(QMessageBox.Ok)
               ret = msgBox.exec_()
            else:
                 ###Complete RUN!####
                 self.pushButton.setText("Stop")
                 self.pushButton.setStyleSheet("background-color:rgb(252, 76, 76);\n" "color: #FFF;")
                 print("Start")
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
                 self.buy_marketbuy.setEnabled(False)
                 self.buy_bestoffer.setEnabled(False)
                 self.buy_limitorder.setEnabled(False)
                 self.buy_limitorder_input.setEnabled(False)
                 self.buy_trader_dif.setEnabled(False)
                 self.sell_marketsell.setEnabled(False)
                 self.sell_bestoffer.setEnabled(False)
                 self.key_api.setEnabled(False)
                 self.key_secret.setEnabled(False)
                 self.max_btc.setEnabled(False)
                 
                 

                 self.timer.start(5000)

                 self.showTime()




        else:
            
            self.timer.stop()
            

            self.pushButton.setText("Run")
            self.pushButton.setStyleSheet("background-color:rgb(85, 170, 127);\n" "color: #FFF;")
            print("Stop")
            
            
            #######Trader selections
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
            self.buy_marketbuy.setEnabled(True)
            self.buy_bestoffer.setEnabled(True)
            self.buy_limitorder.setEnabled(True)
            self.buy_limitorder_input.setEnabled(True)
            self.buy_trader_dif.setEnabled(True)
            self.sell_marketsell.setEnabled(True)
            self.sell_bestoffer.setEnabled(True)
            self.key_api.setEnabled(True)
            self.key_secret.setEnabled(True)
            self.max_btc.setEnabled(True)

            #timer.deleteLater()

    def showTime(self):
        ### Decide to process ( buy or sell )
        con = sqlite3.connect("bw_db.db")
        order_data = pd.read_sql_query("Select * From orders WHERE status ='0' or status='1'", con)
        num_row = len(order_data)
        total_spent_btc = 0
        process_buy=0
        process_sell=0
        real_disposable_btc = 0
        data_traders = set()
        data_selling = set()

        if num_row>0:
            process_sell=1
            #order_data['idandstatust']=str(order_data.id) + '???' +  str(order_data.status)
            for i in order_data['id'].where(order_data['status']==1):
                if str(i)!="nan":
                    data_selling.add(int(i))
            order_data['spents'] = order_data.buy_amount * order_data.buy_my_price
            for i in order_data['spents']:
                total_spent_btc += i
        disposable_btc = float(self.max_btc.text()) - float(total_spent_btc)
        if disposable_btc>min_btc:
            balance = self.client.get_asset_balance(asset='BTC')
            if (float(balance["free"])>min_btc):
                process_buy = 1
                data_traders = active_trader_list
                if (float(balance["free"])>=disposable_btc):
                    real_disposable_btc = disposable_btc
                else:
                    real_disposable_btc = balance["free"]
        try:
            r = requests.get("http://www.binancewinner.com/engine/trader-api-req.php", params={"traders[]":data_traders,"open_orders[]":data_selling,"email":glo_email,"password":glo_password})
            if (r.status_code==200):
                global show_pd
                show_pd=pd.DataFrame(r.json())
                
                #####START BUY!!!!
                try:
                    if int(show_pd["buy"]["id"])>0:
                        print("Aldık")
                        global symbol_info
                        symbol_info = self.client.get_symbol_info(show_pd["buy"]["coin_name"])
                        global order_book
                        order_book =  self.client.get_order_book(symbol=show_pd["buy"]["coin_name"])                        
                        
                        price_tick_size=Decimal(symbol_info["filters"][0]["tickSize"]) #Price Tick Size
                        min_qty=symbol_info["filters"][1]["minQty"] #Minimum Quantity
                        step_qty=symbol_info["filters"][1]["stepSize"]  #Step Quantity Size
                        
                        print(self.decimal_find(price_tick_size))
                        global order
                        #order = self.client.get_open_orders(symbol='NEOUSDT')
                        order = self.client.get_all_orders(symbol='GVTBTC')
                        
                        
                        #print(order)
                        if buy_choice==1: ## Market Buy
                            global buy_qty
                            buy_qty=Decimal(real_disposable_btc)/Decimal(order_book["asks"][0][0])
                            buy_qty=Decimal(buy_qty)*Decimal(0.9)
                            buy_qty=Decimal(buy_qty)-(Decimal(buy_qty)%Decimal(min_qty))
                            #buy_qty=math.floor(buy_qty)
                            getcontext().prec = int(self.decimal_find(price_tick_size))
                            print(buy_qty)
                        elif buy_choice==2: ## Best Offer Buy
                            pass
                            
                            
                except Exception as e:
                    print( str(e))
                    print("Don't buy")

                #####START SELL!!!!
                try:
                    if int(show_pd["sell"]["id"])>0:
                        print("Sattık")
                        if sell_choice==1: ## Market Sell
                            pass
                        #print(show_pd["sell"])
                except:
                    print("Don't sell")                                        
        except:
            pass #CONNECTION ERROR but we will act as if we do not exist :)

        print(data_traders,data_selling)
        print(process_buy,process_sell)
        print(real_disposable_btc)
        print(total_spent_btc)
        
        
        self.status_area.append("Working")

        print(active_trader_list)
    def decimal_find(self,x):
        if Decimal(x)*10==1:
            deci=1
        elif Decimal(x)*100==1:
            deci=2   
        elif Decimal(x)*1000==1:
            deci=3   
        elif Decimal(x)*10000==1:
            deci=4   
        elif Decimal(x)*100000==1:
            deci=5   
        elif Decimal(x)*1000000==1:
            deci=6   
        elif Decimal(x)*10000000==1:
            deci=7   
        elif Decimal(x)*100000000==1:
            deci=8   
        elif Decimal(x)*1000000000==1:
            deci=9
        return deci
    
    
    def best_offer(self,symbol,trader_price,buy_sell):
        symbol_info = client.get_symbol_info(symbol)
        order_book =  client.get_order_book(symbol=symbol)
        
        price_tick_size=Decimal(symbol_info["filters"][0]["tickSize"]) #Price Tick Size
        min_qty=symbol_info["filters"][1]["minQty"] #Minimum Quantity
        step_qty=symbol_info["filters"][1]["stepSize"]  #Step Quantity Size
        symbol_status=symbol_info["status"]
        
        best_sell=Decimal(order_book["asks"][0][0]) + 1
        best_buy=Decimal(order_book["bids"][0][0]) + 1
        
        best_buy += price_tick_size
        best_sell -= price_tick_size
        
        trader_price=Decimal(trader_price)
        
        if (buy_sell==0):
            b_t=best_buy 
            b_t=str(b_t).replace("1.","0.")
        else:
            b_t=best_sell
            b_t=str(b_t).replace("1.","0.")
                
        return b_t
            
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
        try:
            v_check=requests.get("https://www.binancewinner.com/engine/trade_version.txt")
        except:
            self.Login_error_msg="Internet Connection Error"                            
            self.text_login_error.setText(self.Login_error_msg)
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
                        elif (lgn_err_code==2):
                            self.Login_error_msg="Please Upgrade Plus member"
                        elif (lgn_err_code==3):
                            self.Login_error_msg="You haven't trader"                            
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









