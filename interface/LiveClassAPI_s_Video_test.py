import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIVideoTest(unittest.TestCase):
    """上传视频接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/video/createuploadinfo?"
        self.create_upload_info_data = LiveAPIData.createuploadinfoData(self)
        t = THQS.thqs()
        create_upload_info_data = t.get_thqs(self.create_upload_info_data)
        self.create_info_url = url+create_upload_info_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_list(self):
        '''生成上传接口成功'''
        r = self.live.SendOut(self,self.create_info_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.create_info_url)
        print("输入参数：%s" % self.create_upload_info_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['success'],'true')









