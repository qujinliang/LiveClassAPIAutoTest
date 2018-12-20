import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIVideoTest(unittest.TestCase):
    """查询房间已关联的媒体接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/video/onrelated?"
        self.onrelated_data = LiveAPIData.onrelatedData(self)
        t = THQS.thqs()
        onrelated_data = t.get_thqs(self.onrelated_data)
        self.onrelated_url = url+onrelated_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''查询房间已关联的媒体成功'''
        r = self.live.SendOut(self,self.onrelated_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("输入参数：%s" % self.onrelated_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









