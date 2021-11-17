import requests
import json


def get_token(UserApiKey='', SecretKey=''):
    url = 'http://RestfulSms.com/api/Token'
    headers = {
        "Content-Type": "application/json",
    }
    body = {
        "UserApiKey": UserApiKey,
        "SecretKey": SecretKey
    }
    response = requests.post(url, data=json.dumps(body), headers=headers)
    if response.status_code is 201:
        if response.json()['IsSuccessful'] is True:
            secure_token = response.json()['TokenKey']
            return secure_token
    return None


def get_credit(token=''):
    url = 'http://RestfulSms.com/api/credit'
    headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': token
    }
    response = requests.get(url, headers=headers)
    return response
