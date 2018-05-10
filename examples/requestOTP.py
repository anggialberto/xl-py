# -*- coding: utf-8 -*-
from xlpy import *

xl = XL('MSISDN/NO.TELP')
xl.reqOTP()

#status = xl.reqOTP()
#print(status['message'])