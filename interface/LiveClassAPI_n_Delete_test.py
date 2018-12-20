import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIDeleteTest(unittest.TestCase):
    """删除文档接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/doc/delete?"
        self.delete_data = LiveAPIData.deleteData(self)
        t = THQS.thqs()
        delete_data = t.get_thqs(self.delete_data)
        self.delete_url = url+delete_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''获取直播间列表成功'''
        r = self.live.SendOut(self,self.delete_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.delete_url)
        print("输入参数：%s" % self.delete_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









