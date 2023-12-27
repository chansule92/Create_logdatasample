import random
import datetime
import pandas as pd
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
import os
from pathlib import Path



class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def hideHBox(self):
            # Hide the QHBoxLayout
            self.layout().itemAt(0).widget().setVisible(False)

    def initUI(self):
        #프로그램 형태 만들기
        grid = QGridLayout()
        step0grid = QHBoxLayout()
        step0grid.addWidget(QLabel("이벤트 추가/제거"),0)
        step0grid.addWidget(QLabel(""),0)
        step0grid.addWidget(QLabel("이벤트 선택"),2)
        step0grid.addWidget(QLabel(""),0)
        step0grid.addWidget(QLabel("확률"),4)
        step1grid = QHBoxLayout()
        step2grid = QHBoxLayout()
        step3grid = QHBoxLayout()
        step4grid = QHBoxLayout()
        step5grid = QHBoxLayout()
        step6grid = QHBoxLayout()
        step7grid = QHBoxLayout()
        #추가버튼
        self.Button_add_step1 = QPushButton("+")
        self.Button_add_step2 = QPushButton("+")
        self.Button_add_step3 = QPushButton("+")
        self.Button_add_step4 = QPushButton("+")
        self.Button_add_step5 = QPushButton("+")
        self.Button_add_step6 = QPushButton("+")
        self.Button_add_step1.clicked.connect(self.addstep2)
        self.Button_add_step2.clicked.connect(self.addstep3)
        self.Button_add_step3.clicked.connect(self.addstep4)
        self.Button_add_step4.clicked.connect(self.addstep5)
        self.Button_add_step5.clicked.connect(self.addstep6)
        self.Button_add_step6.clicked.connect(self.addstep7)
        self.Button_add_step1.setMaximumWidth(56)
        self.Button_add_step2.setMaximumWidth(25)
        self.Button_add_step3.setMaximumWidth(25)
        self.Button_add_step4.setMaximumWidth(25)
        self.Button_add_step5.setMaximumWidth(25)
        self.Button_add_step6.setMaximumWidth(25)
        step1grid.addWidget(self.Button_add_step1,0)
        step2grid.addWidget(self.Button_add_step2,0)
        step3grid.addWidget(self.Button_add_step3,0)
        step4grid.addWidget(self.Button_add_step4,0)
        step5grid.addWidget(self.Button_add_step5,0)
        step6grid.addWidget(self.Button_add_step6,0)
        #삭제버튼
        self.Button_out_step2 = QPushButton("-")
        self.Button_out_step3 = QPushButton("-")
        self.Button_out_step4 = QPushButton("-")
        self.Button_out_step5 = QPushButton("-")
        self.Button_out_step6 = QPushButton("-")
        self.Button_out_step7 = QPushButton("-")
        self.Button_out_step2.clicked.connect(self.outstep2)
        self.Button_out_step3.clicked.connect(self.outstep3)
        self.Button_out_step4.clicked.connect(self.outstep4)
        self.Button_out_step5.clicked.connect(self.outstep5)
        self.Button_out_step6.clicked.connect(self.outstep6)
        self.Button_out_step7.clicked.connect(self.outstep7)
        self.Button_out_step2.setMaximumWidth(25)
        self.Button_out_step3.setMaximumWidth(25)
        self.Button_out_step4.setMaximumWidth(25)
        self.Button_out_step5.setMaximumWidth(25)
        self.Button_out_step6.setMaximumWidth(25)
        self.Button_out_step7.setMaximumWidth(56)
        step2grid.addWidget(self.Button_out_step2,1)
        step3grid.addWidget(self.Button_out_step3,1)
        step4grid.addWidget(self.Button_out_step4,1)
        step5grid.addWidget(self.Button_out_step5,1)
        step6grid.addWidget(self.Button_out_step6,1)
        step7grid.addWidget(self.Button_out_step7,1)
        #단계라벨
        self.Steb1Label=QLabel("Step 1 :")
        self.Steb2Label=QLabel("Step 2 :")
        self.Steb3Label=QLabel("Step 3 :")
        self.Steb4Label=QLabel("Step 4 :")
        self.Steb5Label=QLabel("Step 5 :")
        self.Steb6Label=QLabel("Step 6 :")
        self.Steb7Label=QLabel("Step 7 :")
        step1grid.addWidget(self.Steb1Label,2) 
        step2grid.addWidget(self.Steb2Label,2) 
        step3grid.addWidget(self.Steb3Label,2) 
        step4grid.addWidget(self.Steb4Label,2) 
        step5grid.addWidget(self.Steb5Label,2) 
        step6grid.addWidget(self.Steb6Label,2) 
        step7grid.addWidget(self.Steb7Label,2) 
        #확률입력
        self.per_edit1=QLineEdit(self)
        self.per_edit2=QLineEdit(self)
        self.per_edit3=QLineEdit(self)
        self.per_edit4=QLineEdit(self)
        self.per_edit5=QLineEdit(self)
        self.per_edit6=QLineEdit(self)
        self.per_edit7=QLineEdit(self)
        self.per_edit1.setFixedWidth(40)
        self.per_edit2.setFixedWidth(40)
        self.per_edit3.setFixedWidth(40)
        self.per_edit4.setFixedWidth(40)
        self.per_edit5.setFixedWidth(40)
        self.per_edit6.setFixedWidth(40)
        self.per_edit7.setFixedWidth(40)
        self.per_edit1.setValidator(QIntValidator(self)) 
        self.per_edit1.setValidator(QIntValidator(1,100,self))
        self.per_edit1.setText('70')
        self.per_edit2.setValidator(QIntValidator(self)) 
        self.per_edit2.setValidator(QIntValidator(1,100,self)) 
        self.per_edit2.setText('70')
        self.per_edit3.setValidator(QIntValidator(self)) 
        self.per_edit3.setValidator(QIntValidator(1,100,self))  
        self.per_edit3.setText('70')
        self.per_edit4.setValidator(QIntValidator(self)) 
        self.per_edit4.setValidator(QIntValidator(1,100,self))  
        self.per_edit4.setText('70')
        self.per_edit5.setValidator(QIntValidator(self)) 
        self.per_edit5.setValidator(QIntValidator(1,100,self)) 
        self.per_edit5.setText('70') 
        self.per_edit6.setValidator(QIntValidator(self)) 
        self.per_edit6.setValidator(QIntValidator(1,100,self))  
        self.per_edit6.setText('70')
        self.per_edit7.setValidator(QIntValidator(self)) 
        self.per_edit7.setValidator(QIntValidator(1,100,self))  
        self.per_edit7.setText('70')

        #콤보 박스 생성
        cb1 = QComboBox(self)
        cb1.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb1.activated[str].connect(self.onActivated)
        cb2 = QComboBox(self)
        cb2.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb2.activated[str].connect(self.onActivated)
        cb3 = QComboBox(self)
        cb3.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb3.activated[str].connect(self.onActivated)
        cb4 = QComboBox(self)
        cb4.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb4.activated[str].connect(self.onActivated)
        cb5 = QComboBox(self)
        cb5.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb5.activated[str].connect(self.onActivated)
        cb6 = QComboBox(self)
        cb6.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb6.activated[str].connect(self.onActivated)
        cb7 = QComboBox(self)
        cb7.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb7.activated[str].connect(self.onActivated)


        #이벤트정의
        self.steb1 = cb1
        self.steb2 = cb2
        self.steb3 = cb3
        self.steb4 = cb4
        self.steb5 = cb5
        self.steb6 = cb6
        self.steb7 = cb7
        self.SEARCH_BUTTON = QPushButton("찾아보기...")
        self.SEARCH_BUTTON.clicked.connect(self.PATH_SELECT)

        step1grid.addWidget(self.steb1,3)
        step2grid.addWidget(self.steb2,3)
        step3grid.addWidget(self.steb3,3)
        step4grid.addWidget(self.steb4,3)
        step5grid.addWidget(self.steb5,3)
        step6grid.addWidget(self.steb6,3)
        step7grid.addWidget(self.steb7,3)

        step1grid.addWidget(self.per_edit1,4)
        step2grid.addWidget(self.per_edit2,4)
        step3grid.addWidget(self.per_edit3,4)
        step4grid.addWidget(self.per_edit4,4)
        step5grid.addWidget(self.per_edit5,4)
        step6grid.addWidget(self.per_edit6,4)
        step7grid.addWidget(self.per_edit7,4)
        #숨김정의
        self.Button_add_step2.setVisible(False)
        self.Button_out_step2.setVisible(False)
        self.Steb2Label.setVisible(False)
        self.steb2.setVisible(False)
        self.per_edit2.setVisible(False)
        self.Button_add_step3.setVisible(False)
        self.Button_out_step3.setVisible(False)
        self.Steb3Label.setVisible(False)
        self.steb3.setVisible(False)
        self.per_edit3.setVisible(False)
        self.Button_add_step4.setVisible(False)
        self.Button_out_step4.setVisible(False)
        self.Steb4Label.setVisible(False)
        self.steb4.setVisible(False)
        self.per_edit4.setVisible(False)
        self.Button_add_step5.setVisible(False)
        self.Button_out_step5.setVisible(False)
        self.Steb5Label.setVisible(False)
        self.steb5.setVisible(False)
        self.per_edit5.setVisible(False)
        self.Button_add_step6.setVisible(False)
        self.Button_out_step6.setVisible(False)
        self.Steb6Label.setVisible(False)
        self.steb6.setVisible(False)
        self.per_edit6.setVisible(False)
        self.Button_out_step7.setVisible(False)
        self.Steb7Label.setVisible(False)
        self.steb7.setVisible(False)
        self.per_edit7.setVisible(False)

        grid.addLayout(step0grid,0,0)
        grid.addLayout(step1grid,1,0)
        grid.addLayout(step2grid,2,0)
        grid.addLayout(step3grid,3,0)
        grid.addLayout(step4grid,4,0)
        grid.addLayout(step5grid,5,0)
        grid.addLayout(step6grid,6,0)
        grid.addLayout(step7grid,7,0)


        self.PATH = QLabel(" ")
        grid.addWidget(self.PATH,8,1)




        ##grid.addWidget(self.SEARCH_BUTTON,4,2)

        #DB선택 라디오버튼
        #생성,취소버튼
        CreateButton = QPushButton("생성")
        CancleButton = QPushButton("취소")
        CreateButton.clicked.connect(self.CreateButton)
        CancleButton.clicked.connect(self.close)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(CreateButton)
        hbox.addWidget(CancleButton)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        ##vbox.addWidget(self.result)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(400,400,300,50)
        self.setWindowTitle('Logdata Creation')
        self.show()

    def CreateButton(self):
        step_list=[]
        if self.steb1.currentText()!='선택하세요':
           step_list.append(self.steb1.currentText())
        if self.steb2.currentText()!='선택하세요':
           step_list.append(self.steb2.currentText())
        if self.steb3.currentText()!='선택하세요':
           step_list.append(self.steb3.currentText())
        if self.steb4.currentText()!='선택하세요':
           step_list.append(self.steb4.currentText())
        if self.steb5.currentText()!='선택하세요':
           step_list.append(self.steb5.currentText())
        if self.steb6.currentText()!='선택하세요':
           step_list.append(self.steb6.currentText())
        if self.steb7.currentText()!='선택하세요':
           step_list.append(self.steb7.currentText())



        print(step_list)

    def addstep2(self):
        self.Button_add_step2.setVisible(True)
        self.Button_out_step2.setVisible(True)
        self.Steb2Label.setVisible(True)
        self.steb2.setVisible(True)
        self.per_edit2.setVisible(True)

    def addstep3(self):
        self.Button_add_step3.setVisible(True)
        self.Button_out_step3.setVisible(True)
        self.Steb3Label.setVisible(True)
        self.steb3.setVisible(True)
        self.per_edit3.setVisible(True)

    def addstep4(self):
        self.Button_add_step4.setVisible(True)
        self.Button_out_step4.setVisible(True)
        self.Steb4Label.setVisible(True)
        self.steb4.setVisible(True)
        self.per_edit4.setVisible(True)

    def addstep5(self):
        self.Button_add_step5.setVisible(True)
        self.Button_out_step5.setVisible(True)
        self.Steb5Label.setVisible(True)
        self.steb5.setVisible(True)
        self.per_edit5.setVisible(True)

    def addstep6(self):
        self.Button_add_step6.setVisible(True)
        self.Button_out_step6.setVisible(True)
        self.Steb6Label.setVisible(True)
        self.steb6.setVisible(True)
        self.per_edit6.setVisible(True)

    def addstep7(self):
        self.Button_out_step7.setVisible(True)
        self.Steb7Label.setVisible(True)
        self.steb7.setVisible(True)
        self.per_edit7.setVisible(True)

    def outstep2(self):
        self.Button_add_step2.setVisible(False)
        self.Button_out_step2.setVisible(False)
        self.Steb2Label.setVisible(False)
        self.steb2.setVisible(False)
        self.per_edit2.setVisible(False)


    def outstep3(self):
        self.Button_add_step3.setVisible(False)
        self.Button_out_step3.setVisible(False)
        self.Steb3Label.setVisible(False)
        self.steb3.setVisible(False)
        self.per_edit3.setVisible(False)


    def outstep4(self):
        self.Button_add_step4.setVisible(False)
        self.Button_out_step4.setVisible(False)
        self.Steb4Label.setVisible(False)
        self.steb4.setVisible(False)
        self.per_edit4.setVisible(False)


    def outstep5(self):
        self.Button_add_step5.setVisible(False)
        self.Button_out_step5.setVisible(False)
        self.Steb5Label.setVisible(False)
        self.steb5.setVisible(False)
        self.per_edit5.setVisible(False)


    def outstep6(self):
        self.Button_add_step6.setVisible(False)
        self.Button_out_step6.setVisible(False)
        self.Steb6Label.setVisible(False)
        self.steb6.setVisible(False)
        self.per_edit6.setVisible(False)


    def outstep7(self):
        self.Button_out_step7.setVisible(False)
        self.Steb7Label.setVisible(False)
        self.steb7.setVisible(False)
        self.per_edit7.setVisible(False)


    def onActivated(self,text):
        text

    def PATH_SELECT(self):
        dirName = QFileDialog.getExistingDirectory(self,self.tr("Open Data file"),"./",QFileDialog.ShowDirsOnly)
        self.dirName = dirName.replace('''/''','''\\''')
        self.PATH.setText(dirName)
        return dirName
    
    def close(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())

RFFR_URL_LIST=pd.read_csv('RFFR_URL.csv',low_memory=False)
RFFR_URL_LIST=RFFR_URL_LIST[['url']].values.tolist()
CUST_LIST=pd.read_csv('CUST_LIST.csv',low_memory=False)
CUST_LIST = CUST_LIST[['VSTR_ID','COOKIE_ID','CUST_ID']].head(1)
DEVICE_LIST=pd.read_csv('DEVICE.csv',low_memory=False)
DEVICE_LIST=DEVICE_LIST[['device']].values.tolist()
hour = random.randint(0, 23)
minute = random.randint(0, 59)
second = random.randint(0, 59)
now = datetime.datetime.now()
rand_time = datetime.datetime(now.year, now.month, now.day, hour, minute, second)
TIME=rand_time.strftime("%Y%m%d%H%M%S")

CNTNR_ID = 'website'
import event
event_list=[]

"""
로그인
"""
bsk_number=0
ord_number=0

for i in range(0,len(CUST_LIST)):
    VSTR_ID=CUST_LIST.iloc[i][0]
    COOKIE_ID=CUST_LIST.iloc[i][1]
    CUST_ID=CUST_LIST.iloc[i][2]
    RFFR_URL = random.choice(RFFR_URL_LIST)[0]
    CONN_DEVICE_CD = random.choice(DEVICE_LIST)[0]
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    now = datetime.datetime.now()
    rand_time = datetime.datetime(now.year, now.month, now.day, hour, minute, second)
    TIME=rand_time.strftime("%Y%m%d%H%M%S")
    temp=['','',CUST_ID,CNTNR_ID,VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD,'','','','','','','','','','',TIME]
    
    event_list.append(event.login(temp))
    """temp[18]=temp[18]+시간더하기"""
    event_list.append(event.order(temp,1,0))
    """temp[18]=temp[18]+시간더하기"""
    event_list.append(event.order(temp,1,1))
print(event_list)