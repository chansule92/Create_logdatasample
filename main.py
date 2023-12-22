import random
import datetime
hour = random.randint(0, 23)
minute = random.randint(0, 59)
second = random.randint(0, 59)
now = datetime.datetime.now()
rand_time = datetime.datetime(now.year, now.month, now.day, hour, minute, second)
TIME=rand_time.strftime("%Y%m%d%H%M%S")

ID = '1234567890'
CNTNR_ID = 'h2ywebsite'
COOKIE_ID = 'f0000145-3813-880d-3b98-6bfb6054fecf'
RFFR_URL = 'www.naver.com'
CONN_DEVICE_CD = 'Android'


temp=['','',ID,CNTNR_ID,COOKIE_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD,'','','','','','','','','','',TIME]

import event
event_list=[]
event_list.append(event.login(temp))


event_list.append(event.search(event_list[0]))
event_list.append(event.click(event_list[1]))
event_list.append(event.basket(event_list[2]))

print(event_list)
print(2)dasd