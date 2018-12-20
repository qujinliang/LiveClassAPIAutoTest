import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIChatmsgTest(unittest.TestCase):
    """获取聊天信息接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/live/chatmsg?"
        self.chatmsg_data = LiveAPIData.chatmsgData(self)
        t = THQS.thqs()
        chatmsg_data = t.get_thqs(self.chatmsg_data)
        self.chatmsg_url = url+chatmsg_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_chatmsg(self):
        '''获取聊天信息成功'''
        r = self.live.SendOut(self,self.chatmsg_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.chatmsg_url)
        print("输入参数：%s" % self.chatmsg_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









