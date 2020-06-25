import requests

import json

#This is python project to send sms
def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulk'
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
send_sms("8880132852","How are you?")
