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
            "Header" : None,
            "Body" : {  
                "Header":{  
                    "ReqID" : self.date,
                    "IMEI" : self.imei
                },
                "LoginSendOTPRq":{  
                    "msisdn" : self.msisdn
                }
            },
            "sessionId" : None,
            "onNet" : "False",
            "platform" : "04",
            "serviceId" : "",
            "packageAmt" : "",
            "reloadType" : "",
            "reloadAmt" : "",
            "packageRegUnreg" : "",
            "appVersion" : "3.7.0",
            "sourceName" : "Chrome",
            "sourceVersion" : "",
            "screenName" : "login.enterLoginNumber"
        }
        try:
            r = requests.post(self.XL_HOST_DOMAIN + self.XL_OTPRQ_QUERY_PATH, json=payload, headers=self.headers)
        except:
            r = requests.post(self.XL_HOST_DOMAIN + self.XL_OTPRQ_QUERY_PATH, json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        if(len(status) == 3):
            if ("LoginSendOTPRs" in status): return {"message" : "Successfully get OTP"}
            else: return {"message" : status['message']}
        if(len(status) == 1): return {"message" : "Failed get OTP"}
    
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
            "platform" : "00",
            "staySigned" : "True",
            "onNetLogin" : "NO",
            "appVersion" : "3.0.2",
            "sourceName" : "Chrome",
            "sourceVersion" : ""
        }
        try:
            r = requests.post(self.XL_HOST_DOMAIN + self.XL_PASSRQ_QUERY_PATH, json=payload, headers=self.headers)
        except:
            r = requests.post(self.XL_HOST_DOMAIN + self.XL_PASSRQ_QUERY_PATH, json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        try:
            if (status['SOAP-ENV:Envelope']['SOAP-ENV:Body'][0]['ns0:CommonResponse'][0]['ns0:ResponseCode'] == '00'): 
                return {"message" : "Successfully get Password"}
            else: 
                return {"message" : "Failed get Password"}
        except:
            return {'message' : status['message']}
    
    def loginWithOTP(self, otpCode):
        payload = {
            "Header" : None,
            "Body" : {
                "Header" : {
                    "ReqID" : self.date,
                    "IMEI" : self.imei
                },
                "LoginValidateOTPRq" : {
                    "headerRq" : {
                        "requestDate" : self.date[:8],
                        "requestId" : self.date,
                        "channel" : "MYXLPRELOGIN"                                                
                    },
                    "msisdn" : self.msisdn,
                    "otp" : otpCode
                }
            },
            "sessionid" : None,
            "platform" : "04",
            "msisdn_Type" : "P",
            "serviceid" : "",
            "packageAmt" : "",
            "reloadType" : "",
            "reloadAmt" : "",
            "packageRegUnreg" : "",
            "appVersion" : "3.7.0",
            "sourceName" : "Chrome",
            "sourceVersion" : "",
            "screenName" : "login.enterLoginOTP",
            "mbb_category" : ""
        }
        try:
            r = requests.post(self.XL_HOST_DOMAIN + self.XL_LOGIN_QUERY_PATH, json=payload, headers=self.headers)
        except:
            r = requests.post(self.XL_HOST_DOMAIN + self.XL_LOGIN_QUERY_PATH, json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        if(len(status) == 5): self._sessionId = status['sessionId']
        else: return False
    
    def purchasePackage(self, serviceid):        
        payload = {
            "Header" : None,
            "Body" : {
                "HeaderRequest" : {
                    "applicationID" : "3",
                    "applicationSubID" : "1",
                    "touchpoint" : "MYXL",
                    "requestID" : self.date,
                    "msisdn" : self.msisdn,
                    "serviceID" : self._sessionId
                },
                "opPurchase" : {
                    "msisdn" : self.msisdn,
                    "serviceid" : serviceid
                },
                
                "XBOXRequest" : {
                    "requestName" : "GetSubscriberMenuId",
                    "Subscriber_Number" : "2099690413",
                    "Source" : "mapps",
                    "PayCat" : "PRE-PAID",
                    "Rembal" : "0",
                    "Shortcode" : "mapps"
                },
                "Header" : {
                    "IMEI" : self.imei,
                    "ReqID" : self.date
                }
            },
            "sessionId" : self._sessionId,
            "serviceId" : serviceid,
            "packageRegUnreg" : "Reg",
            "reloadType" : "", 
            "reloadAmt" : "",
            "platform" : "04",
            "appVersion" : "3.7.0",
            "sourceName"  :"Chrome",
            "sourceVersion" : "",
            "msisdn_Type" : "P",
            "screenName" : "home.storeFrontReviewConfirm",
            "mbb_category" : ""
        }
        try:
            r = requests.post(self.XL_HOST_DOMAIN + self.XL_PURCHASEPKG_QUERY_PATH, json=payload, headers=self.headers)
        except:
            r = requests.post(self.XL_HOST_DOMAIN + self.XL_PURCHASEPKG_QUERY_PATH, json=payload, headers=self.headers, verify=False)
        status = json.loads(r.content)
        if(len(status) == 4): return {"message" : "Successfully purchased the package"}
        else: return {"message" : status['message']}
