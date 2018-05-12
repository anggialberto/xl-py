# -*- coding: utf-8 -*-
from xlpy import *

xl = XL('MSISDN/NO.TELP')
r = xl.loginWithOTP('OTP Code')
if(r != False):
    print(xl.purchasePackage('Service ID')['message'])
else:
    print("Login failed try again")
