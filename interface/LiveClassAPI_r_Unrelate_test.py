import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIUnrelateTest(unittest.TestCase):
    """取消文档关联接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/doc/unrelate?"
        self.unrelate_data = LiveAPIData.unrelateData(self)
        t = THQS.thqs()
        unrelate_data = t.get_thqs(self.unrelate_data)
        self.unrelate_url = url+unrelate_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''取消文档关联成功'''
        r = self.live.SendOut(self,self.unrelate_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.unrelate_url)
        print("输入参数：%s" % self.unrelate_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









