import unittest
from util import THQS
from util import withOpenDef
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIStartTest(unittest.TestCase):
    """开始直播接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/room/live/start?"
        data = LiveAPIData.startData(self)
        self.start_data = data[0]
        self.nouserid_data = data[1]
        t = THQS.thqs()
        start_data,nouserid_data = t.get_thqs(self.start_data),t.get_thqs(self.nouserid_data)
        self.start_url = url+start_data
        self.nouserid_url = url+nouserid_data
        self.live = LiveAPIRequests.LiveAPIRequests
        self.with_liveid = withOpenDef.WithOpenDef()

    def tearDown(self):
        pass

    def test_a_start(self):
        '''开始直播成功'''
        r = self.live.SendOut(self,self.start_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.start_url)
        print("请求数据: %s" % self.start_data)
        print("返回数据：%s" % r)
        self.assertEqual(r['result'],'OK')
        ROOMIDS = r['liveId']
        if ROOMIDS == None:
            return
        self.with_liveid.withWiteLiveId(ROOMIDS)

    def test_b_start(self):
        '''开始直播成功：不传userid'''
        r = self.live.SendOut(self, self.nouserid_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.nouserid_url)
        print("请求数据: %s" % self.nouserid_data)
        print("返回数据：%s" % r)
        self.assertEqual(r['result'], 'OK')
        ROOMIDS = r['liveId']
        if ROOMIDS == None:
            return
        self.with_liveid.withWiteLiveId(ROOMIDS)







