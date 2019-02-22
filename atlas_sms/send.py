import requests
import simplejson as json
from requests.auth import HTTPBasicAuth

baseUrl = 'http://localhost:4000/v'
version_number = '1'
send_sms_endpoint = '/sms/send_sms'


class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: message={}".format(self.status)


class APIAuth:
    'base class for authentication of all api calls'

    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def __str__(self):
        return "Access_key is %s, secret_key is %s" % (self.access_key, self.secret_key)


class SMSObject:
    'class for all sms to be sent'

    def __init__(self, to, sender, content):
        self.to = to
        self.sender = sender
        self.content = content

    def __str__(self):
        return "To is %s, sender is %s , content is %s" % (self.to, self.sender, self.content)


def sendsms(api_auth: APIAuth, sms_payload: SMSObject):
    url = baseUrl+version_number+send_sms_endpoint
    data = {
        'to': sms_payload.to,
        'sender': sms_payload.sender,
        'content': sms_payload.content
    }
    auth = HTTPBasicAuth(api_auth.access_key, api_auth.secret_key)
    response = requests.post(url, data=data, auth=auth)
    if response.status_code != 200:
        raise APIError(response.json())
    else:
        print(response.json())
        return response.json()
    pass
