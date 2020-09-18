# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'site_opens.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from selenium import webdriver
import time
import config

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" %
              self.threadpool.maxThreadCount())
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 648)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_solution_testing = QPushButton(
            self.centralwidget)
        self.pushButton_solution_testing.setGeometry(
            QRect(10, 0, 211, 111))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_solution_testing.setFont(font)
        self.pushButton_solution_testing.setObjectName(
            "pushButton_solution_testing")
        self.pushButton_Trimble_Tx2 = QPushButton(self.centralwidget)
        self.pushButton_Trimble_Tx2.setGeometry(
            QRect(10, 110, 211, 111))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Trimble_Tx2.setFont(font)
        self.pushButton_Trimble_Tx2.setObjectName("pushButton_Trimble_Tx2")
        self.pushButton_Trimble_Tx1 = QPushButton(self.centralwidget)
        self.pushButton_Trimble_Tx1.setGeometry(
            QRect(10, 220, 211, 111))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Trimble_Tx1.setFont(font)
        self.pushButton_Trimble_Tx1.setObjectName("pushButton_Trimble_Tx1")
        self.pushButton_Chesnut = QPushButton(self.centralwidget)
        self.pushButton_Chesnut.setGeometry(QRect(10, 330, 211, 111))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Chesnut.setFont(font)
        self.pushButton_Chesnut.setObjectName("pushButton_Chesnut")
        self.pushButton_Mixed_site = QPushButton(self.centralwidget)
        self.pushButton_Mixed_site.setGeometry(QRect(10, 440, 211, 111))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Mixed_site.setFont(font)
        self.pushButton_Mixed_site.setObjectName("pushButton_Mixed_site")
        self.pushButton_Rep_Inferred = QPushButton(
            self.centralwidget)
        self.pushButton_Rep_Inferred.setGeometry(
            QRect(230, 330, 211, 111))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Rep_Inferred.setFont(font)
        self.pushButton_Rep_Inferred.setObjectName("pushButton_Rep_Inferred")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 638, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_Trimble_Tx2.clicked.connect(
            lambda: self.execute_thread(config.orgTrimbleTx2_RD, config.siteTrimbleTx2_RD))
        self.pushButton_Trimble_Tx1.clicked.connect(
            lambda: self.execute_thread(config.orgTrimbleRd_Tx1, config.siteTrimbleRd_Tx1))
        self.pushButton_Chesnut.clicked.connect(
            lambda: self.execute_thread(config.orgrepublicChesnut, config.siteRepublicChesnut))
        self.pushButton_Mixed_site.clicked.connect(
            lambda: self.execute_thread(config.orgMixedParking, config.siteMixedParking))
        self.pushButton_Rep_Inferred.clicked.connect(
            lambda: self.execute_thread(config.orgrepublicChesnut, config.siteRepublicInferred))
        self.pushButton_solution_testing.clicked.connect(
            lambda: self.execute_thread(config.orgSolutionTesting1, config.siteSolutionTesting1))

# Functions ###################################################################

    def execute_thread(self, org_name, site_name):
        # Pass the function to execute
        # Any other args, kwargs are passed to the run function
        worker = Worker(self.siteSelector, org_name, site_name)

        # Execute
        self.threadpool.start(worker)

    def logIn(self):        
        self.browser = webdriver.Chrome(config.CHROMEDRIVER)
        self.browser.get(config.BASE_URL)
        try:
            time.sleep(3)
            self.browser.find_element_by_id("parking").click()
            username = self.browser.find_element_by_id('email')
            username.send_keys(config.FUNCTIONAL_2_USERNAME)
            self.browser.find_element_by_id("btn-submit").click()
            time.sleep(5)
            password = self.browser.find_element_by_name('password')
            password.send_keys(config.FUNCTIONAL_2_PASSWORD)
            self.browser.find_element_by_id("btn-submit").click()
            time.sleep(12)
        except Exception as e :
            print(e)

    def siteSelector(self, org_name, site_name):
        
        self.logIn()       


        try:
            search_org_name_field = self.browser.find_element_by_xpath(
                '//*[@id="Customer-grid"]/div[3]/div[1]/div[2]/input')

            search_org_name_field.send_keys(org_name)
            self.browser.find_element_by_xpath(
                '//*[@id="Customer-grid"]/div[5]/div/div/div[7]/div/img').click()

            time.sleep(5)
            self.browser.find_element_by_xpath(
                '//*[@id="' + site_name + '"]/div[1]/h2').click()
            time.sleep(3)

            self.browser.find_element_by_xpath(
                '//*[@id="navbar"]/ul/li[3]/a/span/b').click()
            self.browser.find_element_by_xpath(
                '//*[@id="parkingOptimizationLink"]/b').click()
        except Exception as e :
            print(e)
            
        time.sleep(25)
        QApplication.processEvents()

# Main window ###################################################################
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_solution_testing.setText(
            _translate("MainWindow", "Solution Testing_1"))
        self.pushButton_Trimble_Tx2.setText(
            _translate("MainWindow", "TrimbleTx2_RD"))
        self.pushButton_Trimble_Tx1.setText(
            _translate("MainWindow", "TrimbleRd_Tx1"))
        self.pushButton_Chesnut.setText(
            _translate("MainWindow", "republic - Chesnut"))
        self.pushButton_Mixed_site.setText(
            _translate("MainWindow", "Mixed parking"))
        self.pushButton_Rep_Inferred.setText(
            _translate("MainWindow", "republic - Inferred"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    sys.exit(app.exec_())
