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

        r = requests.post(self.XL_HOST_DOMAIN + self.XL_OTPRQ_QUERY_PATH, json=payload, headers=self.headers)
        status = json.loads(r.content)
        if(len(status) == 3):
            if ("LoginSendOTPRs" in status): return {"message" : "Successfully get OTP"}
            else: return {"message" : status['message']}
        if(len(status) == 1): return {"message" : "Failed get OTP"}
    
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

        r = requests.post(self.XL_HOST_DOMAIN + self.XL_LOGIN_QUERY_PATH, json=payload, headers=self.headers)
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

        r = requests.post(self.XL_HOST_DOMAIN + self.XL_PURCHASEPKG_QUERY_PATH, json=payload, headers=self.headers)
        status = json.loads(r.content)
        if(len(status) == 4): return {"message" : "Successfully purchased the package"}
        else: return {"message" : status['message']}