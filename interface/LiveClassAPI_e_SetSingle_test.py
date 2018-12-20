import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPISetTest(unittest.TestCase):
    """切换合流布局模式接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/set_single?"
        self.setSingle_data = LiveAPIData.set_singleData(self)
        t = THQS.thqs()
        setSingle_data = t.get_thqs(self.setSingle_data)
        self.setSingle_url = url+setSingle_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_setSingle(self):
        '''切换合流布局模式成功'''
        r = self.live.SendOut(self,self.setSingle_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.setSingle_url)
        print("请求数据: %s" % self.setSingle_data)
        print("返回数据：%s" % r)
        self.assertEqual(r['result'],'OK')









