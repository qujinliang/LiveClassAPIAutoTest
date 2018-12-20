import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIVideoTest(unittest.TestCase):
    """取消暖场视频接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/video/warm/unset?"
        self.warm_unset_data = LiveAPIData.warmUnsetData(self)
        t = THQS.thqs()
        warm_unset_data = t.get_thqs(self.warm_unset_data)
        self.warm_unset_url = url+warm_unset_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''取消暖场视频成功'''
        r = self.live.SendOut(self,self.warm_unset_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("输入参数：%s" % self.warm_unset_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









