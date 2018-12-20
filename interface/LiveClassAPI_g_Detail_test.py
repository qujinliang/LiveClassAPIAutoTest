import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIDetailTest(unittest.TestCase):
    """获取房间信息接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/room_detail?"
        self.detail_data = LiveAPIData.detailData(self)
        t = THQS.thqs()
        detail_data = t.get_thqs(self.detail_data)
        self.detail_url = url+detail_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_detail(self):
        '''获取房间信息成功'''
        r = self.live.SendOut(self,self.detail_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.detail_url)
        print("请求数据: %s" % self.detail_data)
        print("返回数据：%s" % r)
        self.assertEqual(r['result'],'OK')









