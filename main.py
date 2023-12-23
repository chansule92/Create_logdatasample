import random
import datetime
import pandas as pd

hour = random.randint(0, 23)
minute = random.randint(0, 59)
second = random.randint(0, 59)
now = datetime.datetime.now()
rand_time = datetime.datetime(now.year, now.month, now.day, hour, minute, second)
TIME=rand_time.strftime("%Y%m%d%H%M%S")

RFFR_URL_LIST=pd.read_csv('RFFR_URL.csv')
RFFR_URL_LIST=RFFR_URL_LIST[['url']].values.tolist()
CUST_LIST=pd.read_csv('CUST_LIST.csv')
CUST_LIST = CUST_LIST[['VSTR_ID','COOKIE_ID','CUST_ID']]
DEVICE_LIST=pd.read_csv('DEVICE.csv')
DEVICE_LIST=DEVICE_LIST[['device']].values.tolist()

CNTNR_ID = 'website'
ID = CUST_LIST['CUST_ID'][0]
VSTR_ID=CUST_LIST['COOKIE_ID'][0]
COOKIE_ID = CUST_LIST['COOKIE_ID'][0]
RFFR_URL = random.choice(RFFR_URL_LIST)[0]
CONN_DEVICE_CD = random.choice(DEVICE_LIST)[0]


temp=['','',ID,CNTNR_ID,VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD,'','','','','','','','','','',TIME]

import event
event_list=[]
event_list.append(event.login(temp))


event_list.append(event.search(event_list[0]))
event_list.append(event.click(event_list[1]))
event_list.append(event.basket(event_list[2]))


print(RFFR_URL)