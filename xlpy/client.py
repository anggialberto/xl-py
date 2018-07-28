import requests
import json

from .config import Config

class XL(Config):
    _sessionId = ""

    def __init__(self, msisdn):
        self.msisdn = msisdn
        Config.__init__(self)
    
    def reqOTP(self):
        payload = {
            "Header": None,
            "Body": {
                "Header": {
                    "ReqID": self.date,
                    "IMEI": self.imei
                },
                "LoginSendOTPRq": {
                    "msisdn": self.msisdn
                }
            }, 
            "sessionId": None,
            "onNet": "False",
            "platform": "04",
            "serviceId": "",
            "packageAmt": "",
            "reloadType": "",
            "reloadAmt": "",
            "packageRegUnreg": "",
            "appVersion": "3.8.0",
            "sourceName": "Chrome",
            "sourceVersion": "",
            "screenName": "login.enterLoginNumber"
        }
        r = requests.post(self.XL_HOST_DOMAIN + self.XL_OTPRQ_QUERY_PATH, json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        try:
            if(len(status) == 3):
                if(status['LoginSendOTPRs']):
                    return ({'message' : 'Successfully get OTP Code'})
                else:
                    return({'message' : status['message']})
            elif(len(status) == 2):
                return ({'message' : status['message']})
            else:
                return ({'message' : 'Error Parameter'})
        except:
            return ({'message' : 'Unknown Error'})
    
    def loginWithOTP(self, otpCode):
        payload = {
            "Header": None,
            "Body": {
                "Header": {
                    "ReqID": self.date,
                    "IMEI": self.imei
                },
                "LoginValidateOTPRq": {
                    "headerRq": {
                        "requestDate": self.date[:8],
                        "requestId": self.date,
                        "channel": "MYXLPRELOGIN"
                    },
                    "msisdn": self.msisdn,
                    "otp": otpCode
                }
            },
            "sessionId": None,
            "platform": "04",
            "msisdn_Type": "P",
            "serviceId": "",
            "packageAmt": "",
            "reloadType": "",
            "reloadAmt": "",
            "packageRegUnreg": "",
            "appVersion": "3.8.0",
            "sourceName": "Chrome",
            "sourceVersion": "",
            "screenName": "login.enterLoginOTP",
            "mbb_category": ""
        }
        r = requests.post(self.XL_HOST_DOMAIN + self.XL_LOGIN_QUERY_PATH , json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        try:
            if(len(status) == 5):
                self._sessionId = status['sessionId']
            else:
                return False
        except:
            pass
    
    def purchasePackage(self, serviceid):
        payload = {
            "Header": None,
            "Body": {
                "HeaderRequest": {
                    "applicationID": "3",
                    "applicationSubID": "1",
                    "touchpoint": "MYXL",
                    "requestID": self.date,
                    "msisdn": self.msisdn,
                    "serviceID": serviceid
            },
            "opPurchase": {
                "msisdn": self.msisdn,
                "serviceid": serviceid
            },
            "XBOXRequest": {
                "requestName": "GetSubscriberMenuId"
            },
            "Header": {
                "IMEI": self.imei,
                "ReqID": self.date
            }
          },
          "sessionId": self._sessionId,
          "serviceId": serviceid,
          "packageRegUnreg": "Reg",
          "reloadType": "",
          "reloadAmt": "",
          "platform": "04",
          "appVersion": "3.8.0",
          "sourceName": "Chrome",
          "sourceVersion": "",
          "msisdn_Type": "P",
          "screenName": "home.storeFrontReviewConfirm",
          "mbb_category": ""
        }
        r = requests.post(self.XL_HOST_DOMAIN + self.XL_PURCHASEPKG_QUERY_PATH , json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        try:
            if(len(status) == 4):
                return({'message' : 'Successfully purchased package'})
            else:
                return({'message' : status['message']})
        except:
            return({'message' : 'Unknown Error'})
