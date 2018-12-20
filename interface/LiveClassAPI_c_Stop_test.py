import time
import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIStopTest(unittest.TestCase):
    """停止直播接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/live/stop?"
        data = LiveAPIData.stopData(self)
        self.stop_data,self.nouserid_data = data[0],data[1]
        t = THQS.thqs()
        stop_data = t.get_thqs(self.stop_data)
        nouserid_data = t.get_thqs(self.nouserid_data)
        self.stop_url = url+stop_data
        self.nouserid_url = url+nouserid_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_stop(self):
        '''停止直播成功'''
        time.sleep(5)
        r = self.live.SendOut(self,self.stop_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.stop_url)
        print("输入参数：%s" % self.stop_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')

    def test_b_stop(self):
        '''停止直播成功:不传userid'''
        time.sleep(5)
        r = self.live.SendOut(self,self.nouserid_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.nouserid_url)
        print("输入参数：%s" % self.nouserid_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')







