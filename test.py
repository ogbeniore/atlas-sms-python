from sms.send import SMSObject
from sms.send import APIAuth
from sms.send import sendsms

api_auth = APIAuth(
    access_key='dhbf', secret_key='kjhbdjh')
sms_payload = SMSObject(to='+250780102786',
                        sender='+250780102783', content='This is a test message')


sendsms(api_auth, sms_payload)
