import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIRelateTest(unittest.TestCase):
    """文档关联接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/doc/relate?"
        self.relate_data = LiveAPIData.relateData(self)
        t = THQS.thqs()
        relate_data = t.get_thqs(self.relate_data)
        self.relate_url = url+relate_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''文档关联成功'''
        r = self.live.SendOut(self,self.relate_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.relate_url)
        print("输入参数：%s" % self.relate_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









