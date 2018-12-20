import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPICloseTest(unittest.TestCase):
    """获取sessionid接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/create/sessionid?"
        data = LiveAPIData.sessionidData(self)
        t = THQS.thqs()
        # 拆分获得的数组赋值给变量
        self.role0_data,self.role1_data,self.role2_data,self.client_data = data[0],data[1],data[2],data[3]
        self.bat_data = data[4]
        # 分别加密
        role0_data = t.get_thqs(self.role0_data)
        role1_data = t.get_thqs(self.role1_data)
        role2_data = t.get_thqs(self.role2_data)
        client_data = t.get_thqs(self.client_data)
        bat_data = t.get_thqs(self.bat_data)
        self.role0_url, self.role1_url,self.role2_url = url+role0_data,url+role1_data,url+role2_data
        self.client_url = url+client_data
        self.bat_url = url+bat_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_role0(self):
        '''获取sessionid成功：老师带密码'''
        r = self.live.SendOut(self,self.role0_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.role0_url)
        print("输入参数：%s" % self.role0_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')

    def test_b_role1(self):
        '''获取sessionid成功：互动'''
        r = self.live.SendOut(self,self.role1_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.role1_url)
        print("输入参数：%s" % self.role1_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')

    def test_c_role2(self):
        '''获取sessionid成功：旁听'''
        r = self.live.SendOut(self,self.role2_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.role2_url)
        print("输入参数：%s" % self.role1_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')

    def test_d_client1(self):
        '''获取sessionid成功：移动端'''
        r = self.live.SendOut(self,self.client_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.client_url)
        print("输入参数：%s" % self.client_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')

    def test_e_client1(self):
        '''获取sessionid失败：超范围'''
        r = self.live.SendOut(self,self.bat_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.bat_url)
        print("输入参数：%s" % self.bat_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'FAIL')
        self.assertEqual(r['errorMsg'], 'role : Not a valid choice. ')









