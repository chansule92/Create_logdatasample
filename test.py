import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        global grid
        grid = QGridLayout()
        self.groupbox1 = self.Steb1Group()[0]
        self.groupbox2 = self.Steb2Group()[0]
        self.groupbox3 = self.Steb3Group()[0]
        self.groupbox4 = self.Steb4Group()[0]
        self.groupbox5 = self.Steb5Group()[0]
        self.groupbox6 = self.Steb6Group()[0]
        self.groupbox7 = self.Steb7Group()[0]
        grid.addWidget(self.groupbox1, 1, 0)
        grid.addWidget(self.groupbox2, 2, 0)
        grid.addWidget(self.groupbox3, 3, 0)
        grid.addWidget(self.groupbox4, 4, 0)
        grid.addWidget(self.groupbox5, 5, 0)
        grid.addWidget(self.groupbox6, 6, 0)
        grid.addWidget(self.groupbox7, 7, 0)
        self.groupbox2.setVisible(False)
        self.groupbox3.setVisible(False)
        self.groupbox4.setVisible(False)
        self.groupbox5.setVisible(False)
        self.groupbox6.setVisible(False)
        self.groupbox7.setVisible(False)
        self.setLayout(grid)

        self.Button_add_step1.clicked.connect(self.toggleSteb2Groupbox)
        self.Button_add_step2.clicked.connect(self.toggleSteb3Groupbox)
        self.Button_add_step3.clicked.connect(self.toggleSteb4Groupbox)
        self.Button_add_step4.clicked.connect(self.toggleSteb5Groupbox)
        self.Button_add_step5.clicked.connect(self.toggleSteb6Groupbox)
        self.Button_add_step6.clicked.connect(self.toggleSteb7Groupbox)
        

        self.Button_out_step2.clicked.connect(self.toggleSteb2Groupboxout)
        self.Button_out_step3.clicked.connect(self.toggleSteb3Groupboxout)
        self.Button_out_step4.clicked.connect(self.toggleSteb4Groupboxout)
        self.Button_out_step5.clicked.connect(self.toggleSteb5Groupboxout)
        self.Button_out_step6.clicked.connect(self.toggleSteb6Groupboxout)
        self.Button_out_step7.clicked.connect(self.toggleSteb7Groupboxout)

        self.SEARCH_BUTTON = QPushButton("찾아보기...")
        self.SEARCH_BUTTON.clicked.connect(self.PATH_SELECT)
        CreateButton = QPushButton("생성")
        CreateButton.clicked.connect(self.CreateButton)
        CancleButton = QPushButton("취소")
        CancleButton.clicked.connect(self.close)
        grid.addWidget(self.SEARCH_BUTTON,8,0)
        grid.addWidget(CreateButton, 8, 1)
        grid.addWidget(CancleButton, 8, 2)
        self.setWindowTitle('Box Layout')
        self.setGeometry(0, 300, 400, 100)
        self.show()


    def PATH_SELECT(self):
        dirName = QFileDialog.getExistingDirectory(self,self.tr("Open Data file"),"./",QFileDialog.ShowDirsOnly)
        self.dirName = dirName.replace('''/''','''\\''')
        self.PATH.setText(dirName)
        return dirName


    def Steb1Group(self):
        groupbox = QGroupBox('Step1')
        self.Button_add_step1 = QPushButton("+")
        self.Button_add_step1.setMaximumWidth(56)
        cb1 = QComboBox(self)
        cb1.addItems(['Login','Event','Search','Click','Wishlist','Basket','Order'])
        self.steb1 = cb1

        self.per_edit1 = QLineEdit(self)
        self.per_edit1.setFixedWidth(40)
        self.per_edit1.setValidator(QIntValidator(1, 100, self))
        self.per_edit1.setText('70')
        self.prdt_qty1 = QLineEdit(self)
        self.prdt_qty1.setFixedWidth(40)
        self.prdt_qty1.setValidator(QIntValidator(1, 10, self))
        self.prdt_qty1.setText('1')
        grid1 = QGridLayout()
        grid1.addWidget(self.Button_add_step1, 1, 0)
        grid1.addWidget(self.steb1, 1, 1)
        grid1.addWidget(self.prdt_qty1, 1, 2)
        grid1.addWidget(self.per_edit1, 1, 3)
        self.prdt_qty1.setEnabled(False)
        event_name = self.steb1.activated[str]
        self.steb1.activated[str].connect(self.handleComboBoxTextChange1)
        groupbox.setLayout(grid1)
        return [groupbox,event_name]

    def Steb2Group(self):
        groupbox = QGroupBox('Step2')
        self.Button_add_step2 = QPushButton("+")
        self.Button_add_step2.setMaximumWidth(25)
        self.Button_out_step2 = QPushButton("-")
        self.Button_out_step2.setMaximumWidth(25)
        cb2 = QComboBox(self)
        cb2.addItems(['Login','Event','Search','Click','Wishlist','Basket','Order'])
        self.steb2 = cb2

        self.per_edit2 = QLineEdit(self)
        self.per_edit2.setFixedWidth(40)
        self.per_edit2.setValidator(QIntValidator(1, 100, self))
        self.per_edit2.setText('70')
        self.prdt_qty2 = QLineEdit(self)
        self.prdt_qty2.setFixedWidth(40)
        self.prdt_qty2.setValidator(QIntValidator(1, 10, self))
        self.prdt_qty2.setText('1')
        grid1 = QGridLayout()
        grid1.addWidget(self.Button_add_step2, 1, 0)
        grid1.addWidget(self.Button_out_step2, 1, 1)
        grid1.addWidget(self.steb2, 1, 2)
        grid1.addWidget(self.prdt_qty2, 1, 3)
        grid1.addWidget(self.per_edit2, 1, 4)
        event=self.steb1.currentText()
        if event in ('Basket','Order'):
            self.prdt_qty2.setEnabled(True)
        else:
            self.prdt_qty2.setEnabled(False)
        cb2.activated[str].connect(self.handleComboBoxTextChange2)
        groupbox.setLayout(grid1)

        return [groupbox,self.handleComboBoxTextChange2]
    
    def Steb3Group(self):
        groupbox = QGroupBox('Step3')
        self.Button_add_step3 = QPushButton("+")
        self.Button_add_step3.setMaximumWidth(25)
        self.Button_out_step3 = QPushButton("-")
        self.Button_out_step3.setMaximumWidth(25)
        cb3 = QComboBox(self)
        cb3.addItems(['Login','Event','Search','Click','Wishlist','Basket','Order'])
        self.steb3 = cb3

        self.per_edit3 = QLineEdit(self)
        self.per_edit3.setFixedWidth(40)
        self.per_edit3.setValidator(QIntValidator(1, 100, self))
        self.per_edit3.setText('70')
        self.prdt_qty3 = QLineEdit(self)
        self.prdt_qty3.setFixedWidth(40)
        self.prdt_qty3.setValidator(QIntValidator(1, 10, self))
        self.prdt_qty3.setText('1')
        grid1 = QGridLayout()
        grid1.addWidget(self.Button_add_step3, 1, 0)
        grid1.addWidget(self.Button_out_step3, 1, 1)
        grid1.addWidget(self.steb3, 1, 2)
        grid1.addWidget(self.prdt_qty3, 1, 3)
        grid1.addWidget(self.per_edit3, 1, 4)
        event=self.steb1.currentText()
        if event in ('Basket','Order'):
            self.prdt_qty3.setEnabled(True)
        else:
            self.prdt_qty3.setEnabled(False)
        cb3.activated[str].connect(self.handleComboBoxTextChange3)
        groupbox.setLayout(grid1)

        return [groupbox,event]
    
    def Steb4Group(self):
        groupbox = QGroupBox('Step4')
        self.Button_add_step4 = QPushButton("+")
        self.Button_add_step4.setMaximumWidth(25)
        self.Button_out_step4 = QPushButton("-")
        self.Button_out_step4.setMaximumWidth(25)
        cb4 = QComboBox(self)
        cb4.addItems(['Login','Event','Search','Click','Wishlist','Basket','Order'])
        self.steb4 = cb4

        self.per_edit4 = QLineEdit(self)
        self.per_edit4.setFixedWidth(40)
        self.per_edit4.setValidator(QIntValidator(1, 100, self))
        self.per_edit4.setText('70')
        self.prdt_qty4 = QLineEdit(self)
        self.prdt_qty4.setFixedWidth(40)
        self.prdt_qty4.setValidator(QIntValidator(1, 10, self))
        self.prdt_qty4.setText('1')
        grid1 = QGridLayout()
        grid1.addWidget(self.Button_add_step4, 1, 0)
        grid1.addWidget(self.Button_out_step4, 1, 1)
        grid1.addWidget(self.steb4, 1, 2)
        grid1.addWidget(self.prdt_qty4, 1, 3)
        grid1.addWidget(self.per_edit4, 1, 4)
        event=self.steb1.currentText()
        if event in ('Basket','Order'):
            self.prdt_qty4.setEnabled(True)
        else:
            self.prdt_qty4.setEnabled(False)
        cb4.activated[str].connect(self.handleComboBoxTextChange4)
        groupbox.setLayout(grid1)

        return [groupbox,self.handleComboBoxTextChange4]

    def Steb5Group(self):
        groupbox = QGroupBox('Step5')
        self.Button_add_step5 = QPushButton("+")
        self.Button_add_step5.setMaximumWidth(25)
        self.Button_out_step5 = QPushButton("-")
        self.Button_out_step5.setMaximumWidth(25)
        cb5 = QComboBox(self)
        cb5.addItems(['Login','Event','Search','Click','Wishlist','Basket','Order'])
        self.steb5 = cb5

        self.per_edit5 = QLineEdit(self)
        self.per_edit5.setFixedWidth(40)
        self.per_edit5.setValidator(QIntValidator(1, 100, self))
        self.per_edit5.setText('70')
        self.prdt_qty5 = QLineEdit(self)
        self.prdt_qty5.setFixedWidth(40)
        self.prdt_qty5.setValidator(QIntValidator(1, 10, self))
        self.prdt_qty5.setText('1')
        grid1 = QGridLayout()
        grid1.addWidget(self.Button_add_step5, 1, 0)
        grid1.addWidget(self.Button_out_step5, 1, 1)
        grid1.addWidget(self.steb5, 1, 2)
        grid1.addWidget(self.prdt_qty5, 1, 3)
        grid1.addWidget(self.per_edit5, 1, 4)
        event=self.steb1.currentText()
        if event in ('Basket','Order'):
            self.prdt_qty5.setEnabled(True)
        else:
            self.prdt_qty5.setEnabled(False)
        cb5.activated[str].connect(self.handleComboBoxTextChange5)
        groupbox.setLayout(grid1)

        return [groupbox,self.handleComboBoxTextChange5]

    def Steb6Group(self):
        groupbox = QGroupBox('Step6')
        self.Button_add_step6 = QPushButton("+")
        self.Button_add_step6.setMaximumWidth(25)
        self.Button_out_step6 = QPushButton("-")
        self.Button_out_step6.setMaximumWidth(25)
        cb6 = QComboBox(self)
        cb6.addItems(['Login','Event','Search','Click','Wishlist','Basket','Order'])
        self.steb6 = cb6

        self.per_edit6 = QLineEdit(self)
        self.per_edit6.setFixedWidth(40)
        self.per_edit6.setValidator(QIntValidator(1, 100, self))
        self.per_edit6.setText('70')
        self.prdt_qty6 = QLineEdit(self)
        self.prdt_qty6.setFixedWidth(40)
        self.prdt_qty6.setValidator(QIntValidator(1, 10, self))
        self.prdt_qty6.setText('1')
        grid1 = QGridLayout()
        grid1.addWidget(self.Button_add_step6, 1, 0)
        grid1.addWidget(self.Button_out_step6, 1, 1)
        grid1.addWidget(self.steb6, 1, 2)
        grid1.addWidget(self.prdt_qty6, 1, 3)
        grid1.addWidget(self.per_edit6, 1, 4)
        event=self.steb1.currentText()
        if event in ('Basket','Order'):
            self.prdt_qty6.setEnabled(True)
        else:
            self.prdt_qty6.setEnabled(False)
        cb6.activated[str].connect(self.handleComboBoxTextChange6)
        groupbox.setLayout(grid1)

        return [groupbox,self.handleComboBoxTextChange6]

    def Steb7Group(self):
        groupbox = QGroupBox('Step7')
        self.Button_out_step7 = QPushButton("-")
        self.Button_out_step7.setMaximumWidth(56)
        cb7 = QComboBox(self)
        cb7.addItems(['Login','Event','Search','Click','Wishlist','Basket','Order'])
        self.steb7 = cb7

        self.per_edit7 = QLineEdit(self)
        self.per_edit7.setFixedWidth(40)
        self.per_edit7.setValidator(QIntValidator(1, 100, self))
        self.per_edit7.setText('70')
        self.prdt_qty7 = QLineEdit(self)
        self.prdt_qty7.setFixedWidth(40)
        self.prdt_qty7.setValidator(QIntValidator(1, 10, self))
        self.prdt_qty7.setText('1')
        grid1 = QGridLayout()
        grid1.addWidget(self.Button_out_step7, 1, 1)
        grid1.addWidget(self.steb7, 1, 2)
        grid1.addWidget(self.prdt_qty7, 1, 3)
        grid1.addWidget(self.per_edit7, 1, 4)
        event=self.steb1.currentText()
        if event in ('Basket','Order'):
            self.prdt_qty7.setEnabled(True)
        else:
            self.prdt_qty7.setEnabled(False)
        cb7.activated[str].connect(self.handleComboBoxTextChange7)
        groupbox.setLayout(grid1)

        return [groupbox,self.handleComboBoxTextChange7]


    def handleComboBoxTextChange1(self, text):
        if text in ['Order','Basket']:
            self.prdt_qty1.setEnabled(True)
        else:
            self.prdt_qty1.setEnabled(False)      
    
    def handleComboBoxTextChange2(self, text):
        if text in ['Order','Basket']:
            self.prdt_qty2.setEnabled(True)
        else:
            self.prdt_qty2.setEnabled(False)
        return text
    
    def handleComboBoxTextChange3(self, text):
        if text in ['Order','Basket']:
            self.prdt_qty3.setEnabled(True)
        else:
            self.prdt_qty3.setEnabled(False)
        return text

    
    def handleComboBoxTextChange4(self, text):
        if text in ['Order','Basket']:
            self.prdt_qty4.setEnabled(True)
        else:
            self.prdt_qty4.setEnabled(False)
        return text

    
    def handleComboBoxTextChange5(self, text):
        if text in ['Order','Basket']:
            self.prdt_qty5.setEnabled(True)
        else:
            self.prdt_qty5.setEnabled(False)
        return text

    
    def handleComboBoxTextChange6(self, text):
        if text in ['Order','Basket']:
            self.prdt_qty6.setEnabled(True)
        else:
            self.prdt_qty6.setEnabled(False)
        return text

    
    def handleComboBoxTextChange7(self, text):
        if text in ['Order','Basket']:
            self.prdt_qty7.setEnabled(True)
        else:
            self.prdt_qty7.setEnabled(False)
        return text



    def toggleSteb2Groupbox(self):
        if len(grid)==1 :
            grid.addWidget(self.groupbox2, 2, 0)
            step=2
        else :
            self.groupbox2.setVisible(not self.groupbox2.isVisible())
            step=1

    def toggleSteb3Groupbox(self):
        if len(grid)==2:
            grid.addWidget(self.groupbox3, 3, 0)
            step=3
        else : 
            self.groupbox3.setVisible(not self.groupbox3.isVisible())
            step=2

    def toggleSteb4Groupbox(self):
        if len(grid)==3:
            grid.addWidget(self.groupbox4, 4, 0)
            step=4
        else : 
            self.groupbox4.setVisible(not self.groupbox4.isVisible())
            step=3

    def toggleSteb5Groupbox(self):
        if len(grid)==4:
            grid.addWidget(self.groupbox5, 5, 0)
            step=5
        else : 
            self.groupbox5.setVisible(not self.groupbox5.isVisible())
            step=4

    def toggleSteb6Groupbox(self):
        if len(grid)==5:
            grid.addWidget(self.groupbox6, 6, 0)
            step=6
        else : 
            self.groupbox6.setVisible(not self.groupbox6.isVisible())
            step=5

    def toggleSteb7Groupbox(self):
        if len(grid)==6:
            grid.addWidget(self.groupbox7, 7, 0)
            step=7
        else :
            self.groupbox7.setVisible(not self.groupbox7.isVisible())
            step=6

            
            
    def toggleSteb2Groupboxout(self):
        self.groupbox2.setVisible(not self.groupbox2.isVisible())
        step=1

            
    def toggleSteb3Groupboxout(self):
        self.groupbox3.setVisible(not self.groupbox3.isVisible())
        step=2

            
    def toggleSteb4Groupboxout(self):
        self.groupbox4.setVisible(not self.groupbox4.isVisible())
        step=3

            
    def toggleSteb5Groupboxout(self):
        self.groupbox5.setVisible(not self.groupbox5.isVisible())
        step=4

            
    def toggleSteb6Groupboxout(self):
        self.groupbox6.setVisible(not self.groupbox6.isVisible())
        step=5

            
    def toggleSteb7Groupboxout(self):
        self.groupbox7.setVisible(not self.groupbox7.isVisible())
        step=6

    def printed(self,text):
        return print(text)

    def CreateButton(self):
        print(self.Steb1Group()[1])
        







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    
    sys.exit(app.exec_())


