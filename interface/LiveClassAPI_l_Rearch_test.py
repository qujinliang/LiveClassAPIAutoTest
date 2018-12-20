import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPISearchTest(unittest.TestCase):
    """查询回放信息接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v2/record/search?"
        self.search_data = LiveAPIData.searchData(self)
        t = THQS.thqs()
        search_data = t.get_thqs(self.search_data)
        self.search_url = url+search_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_search(self):
        '''查询回放信息成功'''
        r = self.live.SendOut(self,self.search_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.search_url)
        print("输入参数：%s" % self.search_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









