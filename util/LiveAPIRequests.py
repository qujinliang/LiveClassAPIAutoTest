from pip._vendor import requests
import json
import unittest


class LiveAPIRequests(unittest.TestCase):
    '''这是一个Requests 请求模块
       传入一个加密后的url发送请求然后返回json格式结果'''

    def SendOut(self,url=None,payload=None,headers=None):
        try:
            response = requests.request("GET", url, headers=headers)
            # 如果返回状态码不是200，抛出异常
            response.raise_for_status()
            # 返回结果转json格式赋值给变量r
            self.r = response.json()
            # 判断！如果返回状态不是Ok并且错误内容是系统内部错误，返回错误信息
            if 'result' in self.r:
                pass
            elif 'reason' in self.r:
                print("下面是接口返回:\n%s"%self.r)
            else:
                print("下面是接口返回:\n%s"%self.r)
            return self.r
        # 捕获json格式错误异常，response状态码不为200的异常
        except (json.decoder.JSONDecodeError,requests.RequestException) as e:
            print(e)
        # else:
        #     result = r.json()
        #     print(type(result),result,sep='\n')



