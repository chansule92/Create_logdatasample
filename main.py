import random
import datetime
import pandas as pd
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
import os
from pathlib import Path
import event


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
        step0grid.addWidget(QLabel(""))
        step0grid.addWidget(QLabel("이벤트 선택"),2)
        step0grid.addWidget(QLabel(""))
        step0grid.addWidget(QLabel("확률"),4)
        step0grid.addWidget(QLabel(""))
        step0grid.addWidget(QLabel("소요시간(0~)"),6)
        step1grid = QHBoxLayout()
        step2grid = QHBoxLayout()
        step3grid = QHBoxLayout()
        step4grid = QHBoxLayout()
        step5grid = QHBoxLayout()
        step6grid = QHBoxLayout()
        step7grid = QHBoxLayout()
        dategrid = QHBoxLayout()
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
        step2grid.addWidget(self.Button_out_step2)
        step3grid.addWidget(self.Button_out_step3)
        step4grid.addWidget(self.Button_out_step4)
        step5grid.addWidget(self.Button_out_step5)
        step6grid.addWidget(self.Button_out_step6)
        step7grid.addWidget(self.Button_out_step7)
        dategrid.addWidget(QLabel("생성날짜 : "))
        #단계라벨
        self.Steb1Label=QLabel("Step 1 :")
        self.Steb2Label=QLabel("Step 2 :")
        self.Steb3Label=QLabel("Step 3 :")
        self.Steb4Label=QLabel("Step 4 :")
        self.Steb5Label=QLabel("Step 5 :")
        self.Steb6Label=QLabel("Step 6 :")
        self.Steb7Label=QLabel("Step 7 :")
        step1grid.addWidget(self.Steb1Label) 
        step2grid.addWidget(self.Steb2Label) 
        step3grid.addWidget(self.Steb3Label) 
        step4grid.addWidget(self.Steb4Label) 
        step5grid.addWidget(self.Steb5Label) 
        step6grid.addWidget(self.Steb6Label) 
        step7grid.addWidget(self.Steb7Label) 
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
        self.per_edit1.setText('100')
        self.per_edit1.setDisabled(True)
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
        #시간차입력
        self.time_edit1=QLineEdit(self)
        self.time_edit2=QLineEdit(self)
        self.time_edit3=QLineEdit(self)
        self.time_edit4=QLineEdit(self)
        self.time_edit5=QLineEdit(self)
        self.time_edit6=QLineEdit(self)
        self.time_edit7=QLineEdit(self)
        self.time_edit1.setFixedWidth(40)
        self.time_edit2.setFixedWidth(40)
        self.time_edit3.setFixedWidth(40)
        self.time_edit4.setFixedWidth(40)
        self.time_edit5.setFixedWidth(40)
        self.time_edit6.setFixedWidth(40)
        self.time_edit7.setFixedWidth(40)
        self.time_edit1.setValidator(QIntValidator(self)) 
        self.time_edit1.setValidator(QIntValidator(1,7200,self))
        self.time_edit1.setText('600')
        self.time_edit2.setValidator(QIntValidator(self)) 
        self.time_edit2.setValidator(QIntValidator(1,7200,self)) 
        self.time_edit2.setText('600')
        self.time_edit3.setValidator(QIntValidator(self)) 
        self.time_edit3.setValidator(QIntValidator(1,7200,self))  
        self.time_edit3.setText('600')
        self.time_edit4.setValidator(QIntValidator(self)) 
        self.time_edit4.setValidator(QIntValidator(1,7200,self))  
        self.time_edit4.setText('600')
        self.time_edit5.setValidator(QIntValidator(self)) 
        self.time_edit5.setValidator(QIntValidator(1,7200,self)) 
        self.time_edit5.setText('600') 
        self.time_edit6.setValidator(QIntValidator(self)) 
        self.time_edit6.setValidator(QIntValidator(1,7200,self))  
        self.time_edit6.setText('600')
        self.time_edit7.setValidator(QIntValidator(self)) 
        self.time_edit7.setValidator(QIntValidator(1,7200,self))  
        self.time_edit7.setText('600')
        #시간차입력
        self.cycle_edit1=QLineEdit(self)
        self.cycle_edit2=QLineEdit(self)
        self.cycle_edit3=QLineEdit(self)
        self.cycle_edit4=QLineEdit(self)
        self.cycle_edit5=QLineEdit(self)
        self.cycle_edit6=QLineEdit(self)
        self.cycle_edit7=QLineEdit(self)
        self.cycle_edit1.setFixedWidth(40)
        self.cycle_edit2.setFixedWidth(40)
        self.cycle_edit3.setFixedWidth(40)
        self.cycle_edit4.setFixedWidth(40)
        self.cycle_edit5.setFixedWidth(40)
        self.cycle_edit6.setFixedWidth(40)
        self.cycle_edit7.setFixedWidth(40)
        self.cycle_edit1.setText('1')
        self.cycle_edit2.setText('1')
        self.cycle_edit3.setText('1')
        self.cycle_edit4.setText('1')
        self.cycle_edit5.setText('1')
        self.cycle_edit6.setText('1')
        self.cycle_edit7.setText('1')
        #콤보 박스 생성
        cb1 = QComboBox(self)
        cb1.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb1.activated[str].connect(self.onActivated1)
        cb2 = QComboBox(self)
        cb2.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb2.activated[str].connect(self.onActivated2)
        cb3 = QComboBox(self)
        cb3.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb3.activated[str].connect(self.onActivated3)
        cb4 = QComboBox(self)
        cb4.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb4.activated[str].connect(self.onActivated4)
        cb5 = QComboBox(self)
        cb5.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb5.activated[str].connect(self.onActivated5)
        cb6 = QComboBox(self)
        cb6.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb6.activated[str].connect(self.onActivated6)
        cb7 = QComboBox(self)
        cb7.addItems(['선택하세요','Login','Event','Search','Click','Wishlist','Basket','Order'])
        cb7.activated[str].connect(self.onActivated7)
        #생성시간
        self.start_date=QLineEdit(self)
        self.end_date=QLineEdit(self)
        dategrid.addWidget(self.start_date)
        dategrid.addWidget(QLabel("~"))
        dategrid.addWidget(self.end_date)
        self.start_date.setText('20240101')
        self.end_date.setText('20240131')
        self.start_date.setFixedWidth(80)
        self.end_date.setFixedWidth(80)

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

        step1grid.addWidget(self.steb1)
        step2grid.addWidget(self.steb2)
        step3grid.addWidget(self.steb3)
        step4grid.addWidget(self.steb4)
        step5grid.addWidget(self.steb5)
        step6grid.addWidget(self.steb6)
        step7grid.addWidget(self.steb7)

        step1grid.addWidget(self.per_edit1)
        step2grid.addWidget(self.per_edit2)
        step3grid.addWidget(self.per_edit3)
        step4grid.addWidget(self.per_edit4)
        step5grid.addWidget(self.per_edit5)
        step6grid.addWidget(self.per_edit6)
        step7grid.addWidget(self.per_edit7)

        step1grid.addWidget(self.time_edit1)
        step2grid.addWidget(self.time_edit2)
        step3grid.addWidget(self.time_edit3)
        step4grid.addWidget(self.time_edit4)
        step5grid.addWidget(self.time_edit5)
        step6grid.addWidget(self.time_edit6)
        step7grid.addWidget(self.time_edit7)

        step1grid.addWidget(self.cycle_edit1)
        step2grid.addWidget(self.cycle_edit2)
        step3grid.addWidget(self.cycle_edit3)
        step4grid.addWidget(self.cycle_edit4)
        step5grid.addWidget(self.cycle_edit5)
        step6grid.addWidget(self.cycle_edit6)
        step7grid.addWidget(self.cycle_edit7)
        #숨김정의
        self.cycle_edit1.setVisible(False)
        self.Button_add_step2.setVisible(False)
        self.Button_out_step2.setVisible(False)
        self.Steb2Label.setVisible(False)
        self.steb2.setVisible(False)
        self.per_edit2.setVisible(False)
        self.time_edit2.setVisible(False)
        self.cycle_edit2.setVisible(False)
        self.Button_add_step3.setVisible(False)
        self.Button_out_step3.setVisible(False)
        self.Steb3Label.setVisible(False)
        self.steb3.setVisible(False)
        self.per_edit3.setVisible(False)
        self.time_edit3.setVisible(False)
        self.cycle_edit3.setVisible(False)
        self.Button_add_step4.setVisible(False)
        self.Button_out_step4.setVisible(False)
        self.Steb4Label.setVisible(False)
        self.steb4.setVisible(False)
        self.per_edit4.setVisible(False)
        self.time_edit4.setVisible(False)
        self.cycle_edit4.setVisible(False)
        self.Button_add_step5.setVisible(False)
        self.Button_out_step5.setVisible(False)
        self.Steb5Label.setVisible(False)
        self.steb5.setVisible(False)
        self.per_edit5.setVisible(False)
        self.time_edit5.setVisible(False)
        self.cycle_edit5.setVisible(False)
        self.Button_add_step6.setVisible(False)
        self.Button_out_step6.setVisible(False)
        self.Steb6Label.setVisible(False)
        self.steb6.setVisible(False)
        self.per_edit6.setVisible(False)
        self.time_edit6.setVisible(False)
        self.cycle_edit6.setVisible(False)
        self.Button_out_step7.setVisible(False)
        self.Steb7Label.setVisible(False)
        self.steb7.setVisible(False)
        self.per_edit7.setVisible(False)
        self.time_edit7.setVisible(False)
        self.cycle_edit7.setVisible(False)

        grid.addLayout(step0grid,0,0,alignment=Qt.AlignTop)
        grid.addLayout(step1grid,1,0,alignment=Qt.AlignTop)
        grid.addLayout(step2grid,2,0,alignment=Qt.AlignTop)
        grid.addLayout(step3grid,3,0,alignment=Qt.AlignTop)
        grid.addLayout(step4grid,4,0,alignment=Qt.AlignTop)
        grid.addLayout(step5grid,5,0,alignment=Qt.AlignTop)
        grid.addLayout(step6grid,6,0,alignment=Qt.AlignTop)
        grid.addLayout(step7grid,7,0,alignment=Qt.AlignTop)
        grid.addLayout(dategrid,8,0,alignment=Qt.AlignTop)


        self.PATH = QLabel(" ")
        grid.addWidget(self.PATH,9,1)




        ##grid.addWidget(self.SEARCH_BUTTON,4,2)

        #DB선택 라디오버튼
        #생성,취소버튼
        CreateButton = QPushButton("생성")
        CancleButton = QPushButton("취소")
        CreateButton.clicked.connect(self.CreateButton)
        CancleButton.clicked.connect(self.close)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.SEARCH_BUTTON)
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

    def addstep2(self):
        self.Button_add_step2.setVisible(True)
        self.Button_out_step2.setVisible(True)
        self.Steb2Label.setVisible(True)
        self.steb2.setVisible(True)
        self.per_edit2.setVisible(True)
        self.time_edit2.setVisible(True)
        
    def addstep3(self):
        self.Button_add_step3.setVisible(True)
        self.Button_out_step3.setVisible(True)
        self.Steb3Label.setVisible(True)
        self.steb3.setVisible(True)
        self.per_edit3.setVisible(True)
        self.time_edit3.setVisible(True)

    def addstep4(self):
        self.Button_add_step4.setVisible(True)
        self.Button_out_step4.setVisible(True)
        self.Steb4Label.setVisible(True)
        self.steb4.setVisible(True)
        self.per_edit4.setVisible(True)
        self.time_edit4.setVisible(True)

    def addstep5(self):
        self.Button_add_step5.setVisible(True)
        self.Button_out_step5.setVisible(True)
        self.Steb5Label.setVisible(True)
        self.steb5.setVisible(True)
        self.per_edit5.setVisible(True)
        self.time_edit5.setVisible(True)

    def addstep6(self):
        self.Button_add_step6.setVisible(True)
        self.Button_out_step6.setVisible(True)
        self.Steb6Label.setVisible(True)
        self.steb6.setVisible(True)
        self.per_edit6.setVisible(True)
        self.time_edit6.setVisible(True)

    def addstep7(self):
        self.Button_out_step7.setVisible(True)
        self.Steb7Label.setVisible(True)
        self.steb7.setVisible(True)
        self.per_edit7.setVisible(True)
        self.time_edit7.setVisible(True)

    def outstep2(self):
        self.Button_add_step2.setVisible(False)
        self.Button_out_step2.setVisible(False)
        self.Steb2Label.setVisible(False)
        self.steb2.setVisible(False)
        self.per_edit2.setVisible(False)
        self.time_edit2.setVisible(False)

    def outstep3(self):
        self.Button_add_step3.setVisible(False)
        self.Button_out_step3.setVisible(False)
        self.Steb3Label.setVisible(False)
        self.steb3.setVisible(False)
        self.per_edit3.setVisible(False)
        self.time_edit3.setVisible(False)

    def outstep4(self):
        self.Button_add_step4.setVisible(False)
        self.Button_out_step4.setVisible(False)
        self.Steb4Label.setVisible(False)
        self.steb4.setVisible(False)
        self.per_edit4.setVisible(False)
        self.time_edit4.setVisible(False)

    def outstep5(self):
        self.Button_add_step5.setVisible(False)
        self.Button_out_step5.setVisible(False)
        self.Steb5Label.setVisible(False)
        self.steb5.setVisible(False)
        self.per_edit5.setVisible(False)
        self.time_edit5.setVisible(False)

    def outstep6(self):
        self.Button_add_step6.setVisible(False)
        self.Button_out_step6.setVisible(False)
        self.Steb6Label.setVisible(False)
        self.steb6.setVisible(False)
        self.per_edit6.setVisible(False)
        self.time_edit6.setVisible(False)

    def outstep7(self):
        self.Button_out_step7.setVisible(False)
        self.Steb7Label.setVisible(False)
        self.steb7.setVisible(False)
        self.per_edit7.setVisible(False)
        self.time_edit7.setVisible(False)

    def onActivated1(self,text):
        if text in ('Basket','Order'):
            self.cycle_edit1.setVisible(True)
        else:
            self.cycle_edit1.setVisible(False)

    def onActivated2(self,text):
        if text in ('Basket','Order'):
            self.cycle_edit2.setVisible(True)
        else:
            self.cycle_edit2.setVisible(False)

    def onActivated3(self,text):
        if text in ('Basket','Order'):
            self.cycle_edit3.setVisible(True)
        else:
            self.cycle_edit3.setVisible(False)

    def onActivated4(self,text):
        if text in ('Basket','Order'):
            self.cycle_edit4.setVisible(True)
        else:
            self.cycle_edit4.setVisible(False)

    def onActivated5(self,text):
        if text in ('Basket','Order'):
            self.cycle_edit5.setVisible(True)
        else:
            self.cycle_edit5.setVisible(False)

    def onActivated6(self,text):
        if text in ('Basket','Order'):
            self.cycle_edit6.setVisible(True)
        else:
            self.cycle_edit6.setVisible(False)

    def onActivated7(self,text):
        if text in ('Basket','Order'):
            self.cycle_edit7.setVisible(True)
        else:
            self.cycle_edit7.setVisible(False)

    def PATH_SELECT(self):
        dirName = QFileDialog.getExistingDirectory(self,self.tr("Open Data file"),"./",QFileDialog.ShowDirsOnly)
        self.dirName = dirName.replace('''/''','''\\''')
        self.PATH.setText(dirName)
        return dirName
    
    def close(self):
        sys.exit()


    def CreateButton(self):
        step_list=[]
        if self.steb1.currentText()!='선택하세요':
           step_list.append([self.steb1.currentText(),int(self.per_edit1.text()),int(self.time_edit1.text()),int(self.cycle_edit1.text())])
        if self.steb2.currentText()!='선택하세요':
           step_list.append([self.steb2.currentText(),int(self.per_edit2.text()),int(self.time_edit2.text()),int(self.cycle_edit2.text())])
        if self.steb3.currentText()!='선택하세요':
           step_list.append([self.steb3.currentText(),int(self.per_edit3.text()),int(self.time_edit3.text()),int(self.cycle_edit3.text())])
        if self.steb4.currentText()!='선택하세요':
           step_list.append([self.steb4.currentText(),int(self.per_edit4.text()),int(self.time_edit4.text()),int(self.cycle_edit4.text())])
        if self.steb5.currentText()!='선택하세요':
           step_list.append([self.steb5.currentText(),int(self.per_edit5.text()),int(self.time_edit5.text()),int(self.cycle_edit5.text())])
        if self.steb6.currentText()!='선택하세요':
           step_list.append([self.steb6.currentText(),int(self.per_edit6.text()),int(self.time_edit6.text()),int(self.cycle_edit6.text())])
        if self.steb7.currentText()!='선택하세요':
           step_list.append([self.steb7.currentText(),int(self.per_edit7.text()),int(self.time_edit7.text()),int(self.cycle_edit7.text())])
        CUST_LIST=pd.read_csv('CUST_LIST.csv',low_memory=False)
        CUST_LIST = CUST_LIST[['VSTR_ID','COOKIE_ID','CUST_ID']]
        CNTNR_ID = 'website'
        RFFR_URL_LIST=pd.read_csv('RFFR_URL.csv',low_memory=False)
        RFFR_URL_LIST=RFFR_URL_LIST[['url']].values.tolist()
        DEVICE_LIST=pd.read_csv('DEVICE.csv',low_memory=False)
        DEVICE_LIST=DEVICE_LIST[['device']].values.tolist()
        
        event_list=[]
        bsk_number=1
        ord_number=1
        for i in range(0,len(CUST_LIST)):
            VSTR_ID=CUST_LIST.iloc[i][0]
            COOKIE_ID=CUST_LIST.iloc[i][1]
            CUST_ID=CUST_LIST.iloc[i][2]
            RFFR_URL = random.choice(RFFR_URL_LIST)[0]
            CONN_DEVICE_CD = random.choice(DEVICE_LIST)[0]
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            random_date=event.generate_random_date(self.start_date.text(),self.end_date.text())
            year=int(random_date[0:4])
            month=int(random_date[4:6])
            day=int(random_date[6:8])
            rand_time = datetime.datetime(year, month, day, hour, minute, second)
            TIME=rand_time.strftime("%Y%m%d%H%M%S")
            temp=['','',CUST_ID,CNTNR_ID,VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD,'','','','','','','','','','',TIME]
            for j in step_list:
                if j[0]=='Login' and random.randint(0,100)<=j[1]:
                    temp=event.login(temp)
                    event_list.append(temp)
                    random_second=random.randint(0,j[2])
                    temp[18]=(datetime.datetime.strptime(temp[18],'%Y%m%d%H%M%S')+datetime.timedelta(seconds=random_second)).strftime('%Y%m%d%H%M%S')
                elif j[0]=='Event' and random.randint(0,100)<=j[1]:
                    temp=event.event(temp)
                    event_list.append(temp)
                    random_second=random.randint(0,j[2])
                    temp[18]=(datetime.datetime.strptime(temp[18],'%Y%m%d%H%M%S')+datetime.timedelta(seconds=random_second)).strftime('%Y%m%d%H%M%S')
                elif j[0]=='Search' and random.randint(0,100)<=j[1]:
                    temp=event.search(temp)
                    event_list.append(temp)
                    random_second=random.randint(0,j[2])
                    temp[18]=(datetime.datetime.strptime(temp[18],'%Y%m%d%H%M%S')+datetime.timedelta(seconds=random_second)).strftime('%Y%m%d%H%M%S')
                elif j[0]=='Click' and random.randint(0,100)<=j[1]:
                    temp=event.click(temp)
                    event_list.append(temp)
                    random_second=random.randint(0,j[2])
                    temp[18]=(datetime.datetime.strptime(temp[18],'%Y%m%d%H%M%S')+datetime.timedelta(seconds=random_second)).strftime('%Y%m%d%H%M%S')
                elif j[0]=='Wishlist' and random.randint(0,100)<=j[1]:
                    temp=event.wishlist(temp)
                    event_list.append(temp)
                    random_second=random.randint(0,j[2])
                    temp[18]=(datetime.datetime.strptime(temp[18],'%Y%m%d%H%M%S')+datetime.timedelta(seconds=random_second)).strftime('%Y%m%d%H%M%S')
                elif j[0]=='Basket' and random.randint(0,100)<=j[1]:
                    for k in range(0,random.randint(0,j[3])):
                        temp=event.basket(temp,bsk_number,k)
                        event_list.append(temp)
                    bsk_number=bsk_number+1
                    random_second=random.randint(0,j[2])
                    temp[18]=(datetime.datetime.strptime(temp[18],'%Y%m%d%H%M%S')+datetime.timedelta(seconds=random_second)).strftime('%Y%m%d%H%M%S')
                elif j[0]=='Order' and random.randint(0,100)<=j[1]:
                    for k0 in range(0,random.randint(0,j[3])):
                        temp=event.order(temp,ord_number,k0)
                        event_list.append(temp)
                    ord_number=ord_number+1
                    random_second=random.randint(0,j[2])
                    temp[18]=(datetime.datetime.strptime(temp[18],'%Y%m%d%H%M%S')+datetime.timedelta(seconds=random_second)).strftime('%Y%m%d%H%M%S')
                else :
                    break

        df=pd.DataFrame(event_list)
        
        df.columns=['MSG_ID','MSG_NAME','CUST_ID','CNTNR_ID','VSTR_ID','COOKIE_ID','RFFR_URL','CONN_DEVICE_CD','SITE_EVNT_ID','SEARCH_WORD','PRDT_CD','CATE_CD','BRAND_CD','PRDT_QTY','BASKET_NO','NORM_SALE_AMT','ORD_NO','SALE_AMT','LOG_DTTM']
        df=df.sort_values(by=['LOG_DTTM','CUST_ID']).reset_index(drop=True)
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        df.to_csv(self.dirName + """\\{}_logdata.csv""".format(now),index=False,encoding='cp949')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())