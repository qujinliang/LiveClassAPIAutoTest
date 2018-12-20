import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIVideoTest(unittest.TestCase):
    """设为暖场视频接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/video/warm/set?"
        self.warm_set_data = LiveAPIData.warmSetData(self)
        t = THQS.thqs()
        warm_set_data = t.get_thqs(self.warm_set_data)
        self.warm_set_url = url+warm_set_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''设为暖场视频成功'''
        r = self.live.SendOut(self,self.warm_set_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("输入参数：%s" % self.warm_set_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









