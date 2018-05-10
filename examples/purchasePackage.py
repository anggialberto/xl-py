# -*- coding: utf-8 -*-
from xlpy import *

xl = XL('MSISDN/NO.TELP')
r = xl.loginWithOTP('OTP Code')
if(r != False):
    xl.purchasePackage('Service ID')
    print('Successfully purchased the package')
else:
    print("Login failed try again")