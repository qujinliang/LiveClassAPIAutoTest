import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIListTest(unittest.TestCase):
    """获取直播间列表接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/list?"
        data = LiveAPIData.listData(self)
        self.list_data,self.list_all_data,self.list_bat_data = data[0],data[1],data[2]
        t = THQS.thqs()
        list_data = t.get_thqs(self.list_data)
        list_all_data = t.get_thqs(self.list_all_data)
        list_bat_data = t.get_thqs(self.list_bat_data)
        self.list_url = url+list_data
        self.list_all_url = url+list_all_data
        self.list_bat_url = url + list_bat_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''获取直播间列表成功'''
        r = self.live.SendOut(self,self.list_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.list_url)
        print("请求数据: %s" % self.list_data)
        print("返回数据：%s" % r)
        self.assertEqual(r['result'],'OK')

    def test_b_list(self):
        '''获取直播间列表成功：全传'''
        r = self.live.SendOut(self, self.list_all_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.list_all_url)
        print("请求数据: %s" % self.list_all_data)
        print("返回数据：%s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_c_list(self):
        '''获取直播间列表失败：超范围'''
        r = self.live.SendOut(self, self.list_bat_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'OK')
            return
        print("请求url:  %s" % self.list_bat_url)
        print("请求数据: %s" % self.list_bat_data)
        print("返回数据：%s" % r)
        self.assertEqual(r['result'], 'FAIL')
        self.assertEqual(r['errorMsg'], 'role : Not a valid choice. ')









