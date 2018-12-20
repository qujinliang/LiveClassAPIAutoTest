import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIVideoTest(unittest.TestCase):
    """关联视频接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/video/relate?"
        self.video_relate_data = LiveAPIData.videoRelateData(self)
        t = THQS.thqs()
        video_relate_data = t.get_thqs(self.video_relate_data)
        self.video_relate_url = url+video_relate_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''生成上传接口成功'''
        r = self.live.SendOut(self,self.video_relate_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("输入参数：%s" % self.video_relate_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')









