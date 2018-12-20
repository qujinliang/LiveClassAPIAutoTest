import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIUpdateTest(unittest.TestCase):
    """编辑直播间接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/update?"
        data = LiveAPIData.updateData(self)
        self.update_data,self.bat_update_data = data[0],data[1]
        t = THQS.thqs()
        update_data = t.get_thqs(self.update_data)
        bat_update_data = t.get_thqs(self.bat_update_data)
        self.update_url = url+update_data
        self.bat_update_url = url+bat_update_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_update(self):
        '''更新直播间:成功'''
        r = self.live.SendOut(self,self.update_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'OK')
            return
        print("请求url:b %s"% self.update_url)
        print("请求数据: %s"%self.update_data)
        print("返回数据：%s"%r)
        self.assertEqual(r['result'],'OK')

    def test_b_update(self):
        '''更新直播间:超范围'''
        r = self.live.SendOut(self,self.bat_update_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'OK')
            return
        print("请求url:  %s"% self.bat_update_url)
        print("请求数据: %s"%self.bat_update_data)
        print("返回数据：%s"%r)
        self.assertEqual(r['result'],'FAIL')
        self.assertEqual(r['errorMsg'], 'role : Not a valid choice. ')









