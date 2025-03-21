import requests
import random
import time 
from config import tokens as d
from config import admin
import start
import math
def truncate(number, digits=9):
    stepper = 10.0 ** digits
    number = float(number)
    return math.trunc(stepper * number) / stepper

head = []
for i in d:
    headers = {
    'authorization': f'Bearer {i}',
    'content-type': 'application/json',
    'origin': 'https://byteapi.su',
    'referer': 'https://byteapi.su/app/',
    'sec-ch-ua-platform': '"Android"',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
    }
    head.append(headers)

while True:
    for i in head:
        json_data = {'data': random.randint(90,99)}
        response = requests.post('https://byteapi.su/data/click', headers=i, json=json_data )
        time.sleep(1)
        if response.status_code == 200:
            print(i["authorization"].split(" ")[1][:-50]+":","Сделано",json_data["data"],"     Баланс:  ",truncate(response.json()["data"]["balance"]))
            #if float(response.json()["data"]["balance"]) >= 500:
                #requests.post('https://byteapi.su/data/transfer', headers=i, json={"receiver":str(admin),"amount":response.json()["data"]["balance"],"comment":""})
        elif response.status_code == 429:
            start.st()
        else:
            print(i["authorization"].split(" ")[1][:-50]+":","Ошибка",response.status_code)
            time.sleep(5000)
    print("=========================")

