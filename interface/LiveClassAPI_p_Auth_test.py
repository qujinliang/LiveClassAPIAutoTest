import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIAuthTest(unittest.TestCase):
    """获取房间文档列表接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/doc/auth/list?"
        self.auth_data = LiveAPIData.authListData(self)
        t = THQS.thqs()
        auth_data = t.get_thqs(self.auth_data)
        self.auth_url = url+auth_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''获取房间文档列表成功'''
        r = self.live.SendOut(self,self.auth_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.auth_url)
        print("输入参数：%s" % self.auth_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









