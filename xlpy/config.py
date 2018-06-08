# -*- coding: utf-8 -*-
import datetime

class Config(object):
    XL_HOST_DOMAIN              =  'https://my.xl.co.id'
    XL_HOST_DOMAINV2            =  'https://myprepaid.xl.co.id'
    XL_OTPRQ_QUERY_PATH         =  '/pre/LoginSendOTPRq'
    XL_PASSRQ_QUERY_PATH        =  '/prepaid/ForgotPasswordRq'
    XL_LOGIN_QUERY_PATH         =  '/pre/LoginValidateOTPRq'
    XL_LOGINPWD_QUERY_PATH      =  '/prepaid/LoginV2Rq'
    XL_PURCHASEPKG_QUERY_PATH   =  '/pre/opPurchase'
    XL_PURCHASEPKG_QUERY_PATHV2 =  '/prepaid/opPurchase'

    DATE        =  datetime.datetime.now().strftime("%Y%m%d%I%M%S")
    IMEI        =  'a26f8bbe24104a6d'

    HEADERS     =  {
        'Host': 'myprepaid.xl.co.id',
        'Connection' : 'keep-alive',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
        'Accept' : 'application/json, text/plain, */*',
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept-Encoding' : 'gzip, deflate, br',
	    'Content-Type' : 'application/json'
    }

    def __init__(self):
        self.imei    = self.IMEI
        self.date    = self.DATE
        self.headers = self.HEADERS
