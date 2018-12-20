import unittest
from pip._vendor import requests
import time
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


url = "https://ccapi.csslcloud.net"
url = url+"/api/room/create/sessionid?"
USERID = "99BB96FA148B8FAB"
t = THQS.thqs()
live = LiveAPIRequests.LiveAPIRequests

with open('../data/roomId_list.txt','r',encoding='utf-8') as f:
    roomid_list = f.readlines()

# def roomid_l():
#     for i in roomid_list:
#         return (i.strip('\n'))

for i in roomid_list:
    live_roomid = i.strip('\n')
    role1_data = {"name": "testauto", "userid": USERID, "roomid": live_roomid, "password":"123","role": '0', "client": '0'}
    role1_data = t.get_thqs(role1_data)
    role1_url = url+ role1_data

    response = requests.request("GET",role1_url)
    r = response.json()
    print(r)
    sessionid = r['data']['sessionid']
    with open('../data/sessionid_list31.txt','a',newline='\n',encoding='utf-8') as f:
        f.write(sessionid+'\n')
    time.sleep(0.8)
