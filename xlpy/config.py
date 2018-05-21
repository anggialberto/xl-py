# -*- coding: utf-8 -*-
import datetime

class Config(object):
    XL_HOST_DOMAIN              =  'https://my.xl.co.id'
    
    XL_OTPRQ_QUERY_PATH         =  '/pre/LoginSendOTPRq'
    XL_PASSRQ_QUERY_PATH        =  '/prepaid/ForgotPasswordRq'
    XL_LOGIN_QUERY_PATH         =  '/pre/LoginValidateOTPRq'
    XL_PURCHASEPKG_QUERY_PATH   =  '/pre/opPurchase'

    DATE        =  datetime.datetime.now().strftime("%Y%m%d%I%M%S")
    IMEI        =  '3335892050'

    SERVICE_ID  =  {
        'XL_XTRA_KUOTA' : '8110577',
        'XL_GO_IZI'     : '8211231'
    }

    HEADERS     =  {
        'Host': 'my.xl.co.id',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
	'Content-Type': 'application/json'
    }

    def __init__(self):
        self.imei    = self.IMEI
        self.date    = self.DATE
        self.headers = self.HEADERS
