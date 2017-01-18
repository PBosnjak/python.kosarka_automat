# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automatDesign.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # QTDesigner
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 50, 71, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumber.setNumDigits(2)
        self.lcdNumber.setProperty("intValue", 24)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(610, 50, 71, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lcdNumber_2.setPalette(palette)
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumber_2.setProperty("intValue", 24)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 200, 671, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 370, 321, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.pauzaBtn = QtGui.QPushButton(self.centralwidget)
        self.pauzaBtn.setGeometry(QtCore.QRect(200, 160, 75, 23))
        self.pauzaBtn.setObjectName(_fromUtf8("pauzaBtn"))
        self.nastaviBtn = QtGui.QPushButton(self.centralwidget)
        self.nastaviBtn.setGeometry(QtCore.QRect(500, 160, 75, 23))
        self.nastaviBtn.setObjectName(_fromUtf8("nastaviBtn"))
        self.resetBtn = QtGui.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(600, 510, 75, 23))
        self.resetBtn.setObjectName(_fromUtf8("resetBtn"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(230, 280, 311, 71))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.odaberiBtn = QtGui.QPushButton(self.centralwidget)
        self.odaberiBtn.setGeometry(QtCore.QRect(350, 240, 75, 23))
        self.odaberiBtn.setObjectName(_fromUtf8("odaberiBtn"))
        self.odaberiSBBtn = QtGui.QPushButton(self.centralwidget)
        self.odaberiSBBtn.setGeometry(QtCore.QRect(350, 410, 75, 23))
        self.odaberiSBBtn.setObjectName(_fromUtf8("odaberiSBBtn"))
        self.startBtn = QtGui.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(350, 10, 75, 23))
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

       
        # uspostavljanje timer-a
        self.timer = QtCore.QTimer()
        
        global t,t2
        t=24
        t2=0

        # akcije na odredene tipke
        self.startBtn.clicked.connect(self.start_count)
        self.pauzaBtn.clicked.connect(self.pause_count)
        self.nastaviBtn.clicked.connect(self.resume_count)
        self.odaberiBtn.clicked.connect(self.select_state)
        self.resetBtn.clicked.connect(self.restart_program)
        self.odaberiSBBtn.clicked.connect(self.free_throws)


        
        

        
        
        

        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Košarkaški sudac", None))
        self.pauzaBtn.setText(_translate("MainWindow", "Pauza", None))
        self.odaberiBtn.setText(_translate("MainWindow", "Odaberi", None))
        self.odaberiSBBtn.setText(_translate("MainWindow", "Odaberi", None))
        self.startBtn.setText(_translate("MainWindow", "Start", None))
        self.nastaviBtn.setText(_translate("MainWindow", "Nastavi", None))
        self.resetBtn.setText(_translate("MainWindow", "Reset", None))
  
    def start_count(self):
   
        self.states()
        self.timer.timeout.connect(self.countdown)
        self.timer.start(1000)
        
        
    def countdown(self):
        global t, t2
        
        
        if t>0:
            self.lcdNumber_2.display(24)
            if t == 1:
                t2 = 24
                
            t-=1
            self.lcdNumber.display(t)
            
        elif t2>0:
            self.lcdNumber.display(24)
            if t2 == 1:
                t = 24
                
            t2-=1
            self.lcdNumber_2.display(t2)
        
  
    def pause_count(self):
        self.timer.stop()
        

    def resume_count(self):
        self.timer.start()

    def write(self, text_write):
        self.textBrowser.append(text_write)

    def conditions(self):
        for i in range(0,len(stanja)):
            if stanja[i][1] == kazne[i][0]:
                text = "KAZNA: ", kazne[i][1]
                self.write(text)
            
    # lista mogucih dogadjaja
    def states(self):
        
        for i in range(0,len(stanja)):
            self.comboBox.addItem(stanja[i][0])
            
        self.comboBox.currentIndexChanged.connect(self.selection_output)
        

    def select_state(self):
        global text,text2, t, t2
        for count in stanja:
            
            if count[0] == text:
                
                temp = count[1]
            
                for count in kazne:
                    if temp == count[0]:
                        self.textBrowser.clear()
                        text = "KAZNA:", count[1]
                        text = ' '.join(text)
                        self.write(text)

                        if count[1] == "Promjena posjeda" and t>0 and t2==0:
                            t = 0
                            t2 = 24
                            self.resume_count()
                            self.lcdNumber.display(24)
                            self.comboBox_2.clear()

                        elif count[1] == "Promjena posjeda" and t2>0 and t==0:
                            t2 = 0
                            t = 24
                            self.resume_count()
                            self.lcdNumber_2.display(24)
                            self.comboBox_2.clear()
                        elif count[1] == "Nastavak igre":
                            self.resume_count()
                            self.comboBox_2.clear()
                        elif count[1] == "Slobodna bacanja":
                            
                            
                            
                            self.comboBox_2.addItem("")
                            self.comboBox_2.addItem("Pogodeno zadnje bacanje")
                            self.comboBox_2.addItem("Promaseno zadnje bacanje")
                            self.comboBox_2.currentIndexChanged.connect(self.selection_output2)
                            
                 

    def free_throws(self):
        global text2, t, t2
        if text2 == "Pogodeno zadnje bacanje" and t>0 and t2==0:
            t = 0
            t2 = 24
            self.resume_count()
            self.lcdNumber.display(24)
            self.comboBox_2.clear()
            self.write("Promjena strane")
        elif text2 == "Pogodeno zadnje bacanje" and t2>0 and t==0:
            t2 = 0
            t = 24
            self.resume_count()
            self.lcdNumber_2.display(24)
            self.comboBox_2.clear()
            self.write("Promjena strane")
        elif text2 == "Promaseno zadnje bacanje":
            self.resume_count()
            self.comboBox_2.clear()
            self.write("Nastavak igre")

    def selection_output(self):
        global text
        text = self.comboBox.currentText()
    def selection_output2(self):
        global text2
        text2 = self.comboBox_2.currentText()
    
    def restart_program(self):
    
        python = sys.executable
        os.execl(python, python, * sys.argv)
      
        
if __name__ == "__main__":
    global stanja, kazne

    stanja = (['',''],
              ["Nepravilno vodenje lopte - mijesanje lopte",                               1],
              ["Beskontaktno nesportsko ponasanje",		                           3],
              ["Pogreska vise protivnickih igraca u isto vrijeme",                         2],
              ["Bilo koji dio tijela igraca se nalazi na granici ili van igralista",       1],     			
              ["Lopta na granici ili van igralista",			                   1],
              ["Igrac je promjenio stajnu nogu",     			                   1],
              ["Igrac sa loptom se ustao sa poda",     			                   1],
              ["Igrac je napravio vise od dva koraka prilikom igranja na kos",             1],			
              ["Igrac nastavio voditi loptu nakon sto ju je vodio i primio s obje ruke",   1],   			
              ["Igrac ili lopta se iz prednjeg polja vrati u zadnje polje",     	   1], 		
              ["Napadac je utjecao na loptu koja je imala silaznu putanju prema kosu",     1],    			
              ["Obrambeni igrac je utjecao na loptu u silaznoj putanji prema kosu",        1],			
              ["Napadac se nalazi u protivnickom reketu duze od 3 sekunde",     	   1],		
              ["Napadacka ekipa nije uptila sut prema kosu unutar 24 sekunde",             1],   			
              ["Grubi nesportski kontakt s igracem",     			           3],
              ["Beskontaktno nesportsko ponasanje",     			           3],
              ["Pogreska vise igraca u isto vrijeme",				           2],
              ["Osobna pogreska - igrac je imao namjeru igranja na kos",                   3],
              ["Osobna pogreska - igrac nije imao namjeru igranja na kos",                 1])

    kazne = ([1,"Promjena posjeda"],
             [2,"Nastavak igre"],
             [3,"Slobodna bacanja"])

    




    
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    

