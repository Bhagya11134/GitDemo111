import requests

import json

#This is a python project for message sending.
def send_sms(number,message):
    url = 'http://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'Tc5kJDQUPa1oOwGM4X0HFye6KpuxsjBzWd8E29SnhiqgYtRm7fB708MQSXFEkufHrTxb2zKDIGjVgAWJ',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
         }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
send_sms("7821923181","Hey there!")
