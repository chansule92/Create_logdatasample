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
    SEARCH_WORD = '겨울패딩'
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
    PRDT_CD = 'N30147'
    CATE_CD = 'NEF'
    BRAND_CD = 'NEO'
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
