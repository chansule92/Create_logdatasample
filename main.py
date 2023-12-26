import random
import datetime
import pandas as pd

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