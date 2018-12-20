import unittest
import time
from util import withOpenDef
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveClassAPICreateTest(unittest.TestCase):
    """创建直播间接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/create?"
        data = LiveAPIData.createData(self)
        self.sql_data = LiveAPIData.insert_roomid
        self.create_data,self.create_all_data,self.create_white_data,self.bat_create_data= data[0],data[1],data[2],data[3]

        # 加密传输数据
        t = THQS.thqs()
        create_data = t.get_thqs(self.create_data)
        create_all_data = t.get_thqs(self.create_all_data)
        create_white_data = t.get_thqs(self.create_white_data)
        bat_create_data = t.get_thqs(self.bat_create_data)

        # 拼接请求url
        self.create_url = url+create_data
        self.createa_all_url = url+create_all_data
        self.create_white_url = url+create_white_data
        self.bat_create_url = url+bat_create_data
        self.live = LiveAPIRequests.LiveAPIRequests

        # 实例化写入TXT的模块
        self.with_roomid = withOpenDef.WithOpenDef()

    def tearDown(self):
        pass

    def test_for_create(self):
        '''创建1000个直播间'''
        i = 0
        while i<=10:
            r = self.live.SendOut(self,self.create_url)
            print(r)
            roomid = r['data']['roomid']
            self.with_roomid.withWriteRoomId(roomid)
            time.sleep(0.7)
            i+=1


    # def test_a_create(self):
    #     '''创建直播间成功'''
    #     r = self.live.SendOut(self,self.create_url)
    #     if r == None:
    #         print('请求失败，没有返回数据')
    #         self.assertEqual(None,'')
    #         return
    #     print("请求url:%s"%self.create_url)
    #     print("输入参数：%s"%self.create_data)
    #     print("返回数据: %s"%r)
    #     self.assertEqual(r['result'],'OK')
    #     roomids = r['data']['roomid']
    #     if roomids == None:
    #         return
    #     self.with_roomid.withWriteRoomId(roomids)
    #     self.sql_data(self,roomid=roomids)
    #
    # def test_b_create(self):
    #     '''创建直播间：全填'''
    #     r = self.live.SendOut(self, self.createa_all_url)
    #     if r == None:
    #         print('请求失败，没有返回数据')
    #         self.assertEqual(None,'')
    #         return
    #     print("请求url:%s" % self.createa_all_url)
    #     print("输入参数：%s" % self.create_all_data)
    #     print("返回数据: %s" % r)
    #     self.assertEqual(r['result'], 'OK')
    #     ROOMIDS = r['data']['roomid']
    #     if ROOMIDS == None:
    #         return
    #
    # def test_c_create(self):
    #     '''创建直播间：白名单'''
    #     r = self.live.SendOut(self, self.create_white_url)
    #     if r == None:
    #         print('请求失败，没有返回数据')
    #         self.assertEqual(None,'')
    #         return
    #     print("请求url:%s" % self.create_white_url)
    #     print("输入参数：%s" % self.create_white_data)
    #     print("返回数据: %s" % r)
    #     self.assertEqual(r['result'], 'OK')
    #     ROOMIDS = r['data']['roomid']
    #     if ROOMIDS == None:
    #         return
    #
    # def test_d_create(self):
    #     '''创建直播间：超范围参数'''
    #     r = self.live.SendOut(self, self.bat_create_url)
    #     if r == None:
    #         print('请求失败，没有返回数据')
    #         self.assertEqual(None,'')
    #         return
    #     print("输入参数：%s" % self.bat_create_url)
    #     print("输入参数：%s" % self.bat_create_data)
    #     print("返回数据: %s" % r)
    #     self.assertEqual(r['result'], 'FAIL')
    #     self.assertEqual(r['errorMsg'], 'role : Not a valid choice. ')






