import requests
import time
from config import json_data
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://byteapi.su',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://byteapi.su/app/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

def st():
    for i in json_data:
        response = requests.post('https://byteapi.su/data/init', headers=headers, json=i)
        data = response.json()["data"]["user"]
        print(data["id"],data["balance"],data["perTap"])
        time.sleep(1)