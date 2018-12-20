import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIRecordTest(unittest.TestCase):
    """查询回放列表接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v2/record/info?"
        self.record_data = LiveAPIData.recordData(self)
        t = THQS.thqs()
        record_data = t.get_thqs(self.record_data)
        self.record_url = url+record_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_record(self):
        '''查询回访列表成功'''
        r = self.live.SendOut(self,self.record_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.record_url)
        print("输入参数：%s" % self.record_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









