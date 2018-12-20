import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPICloseTest(unittest.TestCase):
    """关闭直播间接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/close?"
        self.close_data = LiveAPIData.closeData(self)
        t = THQS.thqs()
        close_data = t.get_thqs(self.close_data)
        self.close_url = url+close_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_update(self):
        '''关闭直播间成功'''
        r = self.live.SendOut(self,self.close_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("输入参数：%s" % self.close_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









