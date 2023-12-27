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
        self.Button_add_step1 = QPushButton("+")
        self.Button_add_step2 = QPushButton("+")
        self.Button_add_step3 = QPushButton("+")
        self.Button_add_step4 = QPushButton("+")
        self.Button_add_step5 = QPushButton("+")
        self.Button_add_step6 = QPushButton("+")
        self.Button_add_step7 = QPushButton("+")
        self.Button_add_step1.setMaximumWidth(56)
        self.Button_add_step2.setMaximumWidth(25)
        self.Button_add_step3.setMaximumWidth(25)
        self.Button_add_step4.setMaximumWidth(25)
        self.Button_add_step5.setMaximumWidth(25)
        self.Button_add_step6.setMaximumWidth(25)
        self.Button_add_step7.setMaximumWidth(25)
        step1grid.addWidget(self.Button_add_step1,0)
        step2grid.addWidget(self.Button_add_step2,0)
        step3grid.addWidget(self.Button_add_step3,0)
        step4grid.addWidget(self.Button_add_step4,0)
        step5grid.addWidget(self.Button_add_step5,0)
        step6grid.addWidget(self.Button_add_step6,0)
        step7grid.addWidget(self.Button_add_step7,0)
        self.Button_out_step2 = QPushButton("-")
        self.Button_out_step3 = QPushButton("-")
        self.Button_out_step4 = QPushButton("-")
        self.Button_out_step5 = QPushButton("-")
        self.Button_out_step6 = QPushButton("-")
        self.Button_out_step7 = QPushButton("-")
        self.Button_out_step2.setMaximumWidth(25)
        self.Button_out_step3.setMaximumWidth(25)
        self.Button_out_step4.setMaximumWidth(25)
        self.Button_out_step5.setMaximumWidth(25)
        self.Button_out_step6.setMaximumWidth(25)
        self.Button_out_step7.setMaximumWidth(25)
        step2grid.addWidget(self.Button_out_step2,1)
        step3grid.addWidget(self.Button_out_step3,1)
        step4grid.addWidget(self.Button_out_step4,1)
        step5grid.addWidget(self.Button_out_step5,1)
        step6grid.addWidget(self.Button_out_step6,1)
        step7grid.addWidget(self.Button_out_step7,1)
        step1grid.addWidget(QLabel("Step 1 :"),2) 
        step2grid.addWidget(QLabel("Step 2 :"),2) 
        step3grid.addWidget(QLabel("Step 3 :"),2) 
        step4grid.addWidget(QLabel("Step 4 :"),2) 
        step5grid.addWidget(QLabel("Step 5 :"),2) 
        step6grid.addWidget(QLabel("Step 6 :"),2) 
        step7grid.addWidget(QLabel("Step 7 :"),2) 
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
        cb1.addItem('Login')
        cb1.addItem('Event')
        cb1.addItem('Search')
        cb1.addItem('Click')
        cb1.addItem('Wishlist')
        cb1.addItem('Basket')
        cb1.addItem('Order')
        cb1.activated[str].connect(self.onActivated)
        cb2 = QComboBox(self)
        cb2.addItem('Login')
        cb2.addItem('Event')
        cb2.addItem('Search')
        cb2.addItem('Click')
        cb2.addItem('Wishlist')
        cb2.addItem('Basket')
        cb2.addItem('Order')
        cb2.activated[str].connect(self.onActivated)
        cb3 = QComboBox(self)
        cb3.addItem('Login')
        cb3.addItem('Event')
        cb3.addItem('Search')
        cb3.addItem('Click')
        cb3.addItem('Wishlist')
        cb3.addItem('Basket')
        cb3.addItem('Order')
        cb3.activated[str].connect(self.onActivated)
        cb4 = QComboBox(self)
        cb4.addItem('Login')
        cb4.addItem('Event')
        cb4.addItem('Search')
        cb4.addItem('Click')
        cb4.addItem('Wishlist')
        cb4.addItem('Basket')
        cb4.addItem('Order')
        cb4.activated[str].connect(self.onActivated)
        cb5 = QComboBox(self)
        cb5.addItem('Login')
        cb5.addItem('Event')
        cb5.addItem('Search')
        cb5.addItem('Click')
        cb5.addItem('Wishlist')
        cb5.addItem('Basket')
        cb5.addItem('Order')
        cb5.activated[str].connect(self.onActivated)
        cb6 = QComboBox(self)
        cb6.addItem('Login')
        cb6.addItem('Event')
        cb6.addItem('Search')
        cb6.addItem('Click')
        cb6.addItem('Wishlist')
        cb6.addItem('Basket')
        cb6.addItem('Order')
        cb6.activated[str].connect(self.onActivated)
        cb7 = QComboBox(self)
        cb7.addItem('Login')
        cb7.addItem('Event')
        cb7.addItem('Search')
        cb7.addItem('Click')
        cb7.addItem('Wishlist')
        cb7.addItem('Basket')
        cb7.addItem('Order')
        cb7.activated[str].connect(self.onActivated)


        #입력 변수 생성
        self.steb1 = cb1
        self.steb2 = cb2
        self.steb3 = cb3
        self.steb4 = cb4
        self.steb5 = cb5
        self.steb6 = cb6
        self.steb7 = cb7
        self.SEARCH_BUTTON = QPushButton("찾아보기...")
        self.SEARCH_BUTTON.clicked.connect(self.PATH_SELECT)
        #입력칸 배치
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

        step1grid.addWidget(QLabel("%"),5) 
        step2grid.addWidget(QLabel("%"),5) 
        step3grid.addWidget(QLabel("%"),5) 
        step4grid.addWidget(QLabel("%"),5) 
        step5grid.addWidget(QLabel("%"),5) 
        step6grid.addWidget(QLabel("%"),5) 
        step7grid.addWidget(QLabel("%"),5) 


        grid.addLayout(step0grid,0,0)
        grid.addLayout(step1grid,1,0)
        grid.addLayout(step2grid,2,0)
        grid.addLayout(step3grid,3,0)
        grid.addLayout(step4grid,4,0)
        grid.addLayout(step5grid,5,0)
        grid.addLayout(step6grid,6,0)
        grid.addLayout(step7grid,7,0)


        self.PATH = QLabel(" ")
        ##grid.addWidget(self.PATH,4,1)




        ##grid.addWidget(self.SEARCH_BUTTON,4,2)

        #DB선택 라디오버튼
        #생성,취소버튼
        CreateButton = QPushButton("생성")
        CancleButton = QPushButton("취소")
        ##CreateButton.clicked.connect(self.CreateJson)
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

        self.setGeometry(400,400,300,300)
        self.setWindowTitle('Logdata Creation')
        self.show()


    def onActivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

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