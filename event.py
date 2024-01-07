import random
import pandas as pd
from datetime import datetime, timedelta
WORD_LIST=pd.read_csv('SEARCH_WORD.csv')
WORD_LIST=WORD_LIST[['word']].values.tolist()
SITE_EVENT_LIST=pd.read_csv('SITE_EVENT.csv')
SITE_EVENT_LIST=SITE_EVENT_LIST[['event']].values.tolist()
PRDT_MST=pd.read_csv('PRDT_MST.csv')
PRDT_MST = PRDT_MST[['PRDT_CD','CATE_CD','BRAND_CD','PRDT_NAME','SALE_PRICE']]
PRDT_MST_LIST = PRDT_MST[['PRDT_CD','CATE_CD','BRAND_CD','PRDT_NAME','SALE_PRICE']].values.tolist()
def lpad(i, width, fillchar='0'):
    return str(i).rjust(width, fillchar)

def login(temp):
    MSG_ID = 'MG_LOGIN'
    MSG_NAME = '로그인'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ''
    SEARCH_WORD = ''
    PRDT_CD = ''
    CATE_CD = ''
    BRAND_CD = ''
    PRDT_QTY = ''
    BASKET_NO = ''
    NORM_SALE_AMT = ''
    ORD_NO = ''
    SALE_AMT = ''
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]



def search(temp):
    MSG_ID = 'MG_SEARCH'
    MSG_NAME = '상품검색'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ''
    SEARCH_WORD = random.choice(WORD_LIST)[0]
    PRDT_CD = ''
    CATE_CD = ''
    BRAND_CD = ''
    PRDT_QTY = ''
    BASKET_NO = ''
    NORM_SALE_AMT = ''
    ORD_NO = ''
    SALE_AMT = ''
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]



def click(temp):
    
    MSG_ID = 'MG_PRODUCT_CLICK'
    MSG_NAME = '상품탐색'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ''
    SEARCH_WORD = ''
    PRDT_CD = random.choice(PRDT_MST_LIST)[0]
    CATE_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['CATE_CD'].iloc[0]
    BRAND_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['BRAND_CD'].iloc[0]
    PRDT_QTY = ''
    BASKET_NO = ''
    NORM_SALE_AMT = ''
    ORD_NO = ''
    SALE_AMT = ''
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]

def basket(temp,bsk_number,k):
    if temp[10] == '':
        PRDT_CD = random.choice(PRDT_MST_LIST)[0]
    elif k != 0:
        PRDT_CD = random.choice(PRDT_MST_LIST)[0]
    else:
        PRDT_CD = temp[10]
    MSG_ID = 'MG_BASKET'
    MSG_NAME = '장바구니'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ''
    SEARCH_WORD = ''
    CATE_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['CATE_CD'].iloc[0]
    BRAND_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['BRAND_CD'].iloc[0]
    PRDT_QTY = random.randrange(1,5)
    BASKET_NO = 'BSK'+lpad(bsk_number,6,'0')
    NORM_SALE_AMT = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['SALE_PRICE'].iloc[0]
    ORD_NO = ''
    SALE_AMT = ''
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]


def wishlist(temp):
    if temp[10] == '':
        PRDT_CD = random.choice(PRDT_MST_LIST)[0]
    else :
        PRDT_CD = temp[10]
    MSG_ID = 'MG_WISHLIST'
    MSG_NAME = '찜'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ''
    SEARCH_WORD = ''
    CATE_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['CATE_CD'].iloc[0]
    BRAND_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['BRAND_CD'].iloc[0]
    PRDT_QTY = 1
    BASKET_NO = ''
    NORM_SALE_AMT = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['SALE_PRICE'].iloc[0]
    ORD_NO = ''
    SALE_AMT = ''
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]

def order(temp,ord_number,k):
    if temp[10] == '':
        PRDT_CD = random.choice(PRDT_MST_LIST)[0]
    elif k != 0:
        PRDT_CD = random.choice(PRDT_MST_LIST)[0]
    else:
        PRDT_CD = temp[10]
    MSG_ID = 'MG_ORDER'
    MSG_NAME = '주문'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ''
    SEARCH_WORD = ''
    CATE_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['CATE_CD'].iloc[0]
    BRAND_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['BRAND_CD'].iloc[0]
    PRDT_QTY = random.randrange(1,5)
    BASKET_NO = ''
    NORM_SALE_AMT = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['SALE_PRICE'].iloc[0]
    ORD_NO = 'ORD'+lpad(ord_number,6,'0')
    SALE_AMT = (PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['SALE_PRICE'].iloc[0]) * 0.8
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]


def event(temp):
    MSG_ID = 'MG_EVENT'
    MSG_NAME = '이벤트'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = random.choice(SITE_EVENT_LIST)[0]
    SEARCH_WORD = ''
    PRDT_CD = ''
    CATE_CD = ''
    BRAND_CD = ''
    PRDT_QTY = ''
    BASKET_NO = ''
    NORM_SALE_AMT = ''
    ORD_NO = ''
    SALE_AMT = ''
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]


def generate_random_date(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y%m%d')
    end_date = datetime.strptime(end_date_str, '%Y%m%d')

    date_difference = (end_date - start_date).days

    random_days = random.randint(0, date_difference)

    random_date = start_date + timedelta(days=random_days)

    return random_date.strftime('%Y%m%d')