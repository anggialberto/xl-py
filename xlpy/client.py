import requests
import json

from .config import Config

class XL(Config):
    _sessionId = ""

    def __init__(self, msisdn):
        self.msisdn = msisdn
        Config.__init__(self)
    
    def reqPassword(self):
        payload = {
            "Body" : {
                "Header" : {
                    "ReqID" : self.date,
                    "IMEI" : self.imei
                },
                "ForgotPasswordRq" : {
                    "msisdn" : self.msisdn,
                    "username" : ""
                }
            },
            "sessionId" : None
        }
        r = requests.post(self.XL_HOST_DOMAINV2 + self.XL_PASSRQ_QUERY_PATH, json=payload, headers=self.headers)
        status = json.loads(r.content)
        try:
            if(status['SOAP-ENV:Envelope']['SOAP-ENV:Body'][0]['ns0:CommonResponse'][0]['ns0:ErrorMessage'] == ['SUCCESS_FORGOT_PASSWORDMYXL_NEW']):
                return {"message" : "Successfully get Password"}
            else: 
                return {"message" : "Failed get Password"}
        except:
            return {'message' : status['message']}
        
    def loginWithPassword(self, password):
        params = {"password" : password}
        r = requests.get("http://xlpy.herokuapp.com/api/encrypt", params=params)
        status = r.json()
        payload = {
            "Body" : {
                "Header" : {
                    "IMEI" : self.imei,
                    "ReqID" : self.date
                },
                "LoginV2Rq" : {
                    "msisdn" : self.msisdn,
                    "pass" : status["encrypted"]
                }
            },
            "onNet" : "True",
            "staySigned" : "False",
            "platform" : "00",
            "onNetLogin" : "YES",
            "appVersion" : "3.0.2",
            "sourceName" : "Android",
            "sourceVersion" : "5.1"
        }
        try:
            r = requests.post(self.XL_HOST_DOMAINV2 + self.XL_LOGINPWD_QUERY_PATH, json=payload, headers=self.headers)
        except:
            r = requests.post(self.XL_HOST_DOMAINV2 + self.XL_LOGINPWD_QUERY_PATH, json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        if(len(status) == 6): self._sessionId = status['sessionId']
        else: return False
    
    def purchasePackage(self, serviceid):        
        payload = {
            "Body" : {
                "HeaderRequest" : {
                    "applicationID" : "3",
                    "applicationSubID" : "1",
                    "touchpoint" : "MYXL",
                    "requestID" : self.date,
                    "msisdn" : self.msisdn,
                    "serviceID" : serviceid
                },
                "opPurchase" : {
                    "msisdn" : self.msisdn,
                    "serviceid" : serviceid
                },
                "Header" : {
                    "IMEI" : self.imei,
                    "ReqID" : self.date
                }
            },
            "sessionId" : self._sessionId,
            "onNet" : "True",
            "platform" : "00",
            "staySigned" : "True",
            "onNetLogin" : "YES",
            "appVersion" : "3.0.2",
            "sourceName" : "Android",
            "sourceVersion" : "5.1"
        }
        try:
            r = requests.post(self.XL_HOST_DOMAINV2 + self.XL_PURCHASEPKG_QUERY_PATHV2, json=payload, headers=self.headers)
        except:
            r = requests.post(self.XL_HOST_DOMAINV2 + self.XL_PURCHASEPKG_QUERY_PATHV2, json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        if(len(status) == 4): return {"message" : "Successfully purchased the package"}
        else: return {"message" : status['message']}
