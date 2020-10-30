
import os
import sys
import requests
from urllib.request import urlopen

import json
import random

def face2getname(imgurl):
    client_id = ""
    client_secret = ""
    url = "https://naveropenapi.apigw.ntruss.com/vision/v1/celebrity" # 유명인 얼굴인식

    img = urlopen(imgurl).read()
    files = {'image': img}
    # files = {'image': open('aaa.jpeg', 'rb')}
    headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
        json_dic = json.loads(response.text)
        # print(json_dic.get('faces')[0].get('celebrity').get('value'))
        return json_dic.get('faces')[0].get('celebrity').get('value')
    else:
        print("Error Code:" + rescode)

# get_name('https://image.bugsm.co.kr/artist/images/1000/800491/80049126.jpg')

def rnd_name():
    names = ['김대원','김경태','신윤한','이지훈','정회윤','조명진','김태환','김상희','강준필','조성활','김현정','송선종','신무철','배성환']
    return random.choice(names)
    
print(rnd_name())