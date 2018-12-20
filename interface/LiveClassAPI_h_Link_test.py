import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPILinkTest(unittest.TestCase):
    """获取房间登陆连接接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/link?"
        self.link_data = LiveAPIData.linkData(self)
        t = THQS.thqs()
        link_data = t.get_thqs(self.link_data)
        self.link_url = url+link_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_link(self):
        '''获取房间登陆连接成功'''
        r = self.live.SendOut(self,self.link_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.link_url)
        print("请求数据: %s" % self.link_data)
        print("返回数据：%s" % r)
        self.assertEqual(r['result'],'OK')









