import random
import pandas as pd
WORD_LIST=pd.read_csv('SEARCH_WORD.csv')
WORD_LIST=WORD_LIST[['word']].values.tolist()
PRDT_MST=pd.read_csv('PRDT_MST.csv')
PRDT_MST = PRDT_MST[['PRDT_CD','CATE_CD','BRAND_CD','PRDT_NAME','SALE_PRICE']].head().values.tolist()


def login(temp):
    MSG_ID = 'MG_LOGIN'
    MSG_NAME = '로그인'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ' '
    SEARCH_WORD = ' '
    PRDT_CD = ' '
    CATE_CD = ' '
    BRAND_CD = ' '
    PRDT_QTY = ' '
    BASKET_NO = ' '
    NORM_SALE_AMT = ' '
    ORD_NO = ' '
    SALE_AMT = ' '
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
    SITE_EVNT_ID = ' '
    SEARCH_WORD = random.choice(WORD_LIST)[0]
    PRDT_CD = ' '
    CATE_CD = ' '
    BRAND_CD = ' '
    PRDT_QTY = ' '
    BASKET_NO = ' '
    NORM_SALE_AMT = ' '
    ORD_NO = ' '
    SALE_AMT = ' '
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]

def click(temp):
    if temp[10] == ' ':
        PRDT_CD = random.choice(PRDT_MST)[0]
    MSG_ID = 'MG_PRODUCT_CLICK'
    MSG_NAME = '상품탐색'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ' '
    SEARCH_WORD = ' '
    PRDT_CD = PRDT_CD
    CATE_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['CATE_CD'][0]
    BRAND_CD = PRDT_MST[PRDT_MST['PRDT_CD']==PRDT_CD]['BRAND_CD'][0]
    PRDT_QTY = ' '
    BASKET_NO = ' '
    NORM_SALE_AMT = ' '
    ORD_NO = ' '
    SALE_AMT = ' '
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]

def basket(temp):
    MSG_ID = 'MG_BASKET'
    MSG_NAME = '장바구니'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ' '
    SEARCH_WORD = ' '
    PRDT_CD = 'N30147'
    CATE_CD = 'NEF'
    BRAND_CD = 'NEO'
    PRDT_QTY = 1
    BASKET_NO = 'BSK000001'
    NORM_SALE_AMT = 15000
    ORD_NO = ' '
    SALE_AMT = ' '
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]


def wishlist(temp):
    MSG_ID = 'MG_WISHLIST'
    MSG_NAME = '찜'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ' '
    SEARCH_WORD = ' '
    PRDT_CD = 'N30147'
    CATE_CD = 'NEF'
    BRAND_CD = 'NEO'
    PRDT_QTY = 1
    BASKET_NO = ''
    NORM_SALE_AMT = 15000
    ORD_NO = ' '
    SALE_AMT = ' '
    LOAD_DTTM = temp[18]
    return [MSG_ID, MSG_NAME, CUST_ID, CNTNR_ID, VSTR_ID, COOKIE_ID, RFFR_URL,CONN_DEVICE_CD, SITE_EVNT_ID, SEARCH_WORD, PRDT_CD, CATE_CD, BRAND_CD, PRDT_QTY, BASKET_NO, NORM_SALE_AMT, ORD_NO, SALE_AMT, LOAD_DTTM]

def order(temp):
    MSG_ID = 'MG_ORDER'
    MSG_NAME = '주문'
    CUST_ID = temp[2]
    CNTNR_ID = temp[3]
    VSTR_ID = temp[4]
    COOKIE_ID = temp[5]
    RFFR_URL = temp[6]
    CONN_DEVICE_CD = temp[7]
    SITE_EVNT_ID = ' '
    SEARCH_WORD = ' '
    PRDT_CD = 'N30147'
    CATE_CD = 'NEF'
    BRAND_CD = 'NEO'
    PRDT_QTY = 1
    BASKET_NO = ''
    NORM_SALE_AMT = 15000
    ORD_NO = 'ORD000001'
    SALE_AMT = 12000
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
    SITE_EVNT_ID = 'EVENT001'
    SEARCH_WORD = ' '
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
