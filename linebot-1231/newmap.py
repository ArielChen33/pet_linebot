from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


import json
from math import radians, cos, sin, asin, sqrt
from message import *
from new import *
from Function import *
from newmap import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
input_file1 = open ('Taipei1.json',encoding="utf-8")
input_file2 = open ('NewTaipeiCity1.json',encoding="utf-8")
json_array1 = json.load(input_file1)
json_array2 = json.load(input_file2)

#======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
#=======================
def get_shop(latitude,longitude):
    name = []
    lon = []
    lat = []
    place = []
    d = []
    lst = []
    plst = []
    for item in json_array1:
        name.append(item['業者名稱'])
        lon.append(item['經度'])
        lat.append(item['緯度'])
        place.append(item['連絡地址'])
        
    for item in json_array2:
        name.append(item['業者名稱'])
        lon.append(item['經度'])
        lat.append(item['緯度'])
        place.append(item['連絡地址'])
        
    def haversine(lon1, lat1, lon2, lat2):
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r

    lon1 = longitude
    lat1 = latitude


    for i in range(len(name)):
        lon2 = lon[i]
        lat2 = lat[i]
        d.append(haversine(lon1, lat1, lon2, lat2))
    i = 1
    for i in range(5):
        min_value = min(d)
        lst.append(name[d.index(min_value)])
        plst.append(place[d.index(min_value)])
        d[d.index(min_value)] = 99999999999999999999999999999
        i += 1


        
    input_file1.close()
    input_file2.close()

    contents=dict()
    contents['type']='carousel'
    bubbles=[]
    for i in range(5):
        bubble = {  "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": lst[i],
                                "weight": "bold",
                                "size": "xxl",
                                "margin": "md",
                                "wrap": True,
                                "style": "normal"
                            },
                            {
                                "type": "text",
                                "text": "聯絡資訊",
                                "margin": "md",
                                "size": "lg",
                                "align": "start",
                                "decoration": "none"
                            },
                            {
                                "type": "separator"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "地址:"+plst[i],
                                    "size": "sm",
                                    "wrap": True
                                }
                                ],
                                "margin": "sm"
                            },
                                    
                            ]
                                },
                        "styles": {
                                "footer": {
                                "separator": True
                                    }
                                }
                                }
        bubbles.append(bubble)
        contents['contents']=bubbles
        message = FlexSendMessage(alt_text='寵物店資訊',contents=contents)
        
    return message