import unittest
from pip._vendor import requests
from util import THQS
from util import withOpenDef
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


global ADDURL
ADDURL = ""
class LiveClassAPIAddTest(unittest.TestCase):
    """上传文档接口测试"""
    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/doc/add?"
        self.add_data = LiveAPIData.addData(self)
        t = THQS.thqs()
        add_data = t.get_thqs(self.add_data)
        self.add_url = url+add_data
        self.live = LiveAPIRequests.LiveAPIRequests
        self.with_docId = withOpenDef.WithOpenDef()

    def tearDown(self):
        pass

    def test_a_add(self):
        '''获取文档上传信息表成功'''
        global ADDURL
        r = self.live.SendOut(self,self.add_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("输入参数：%s" % self.add_url)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')
        ADDURL = r['data']['upload_url']


    def test_b_add(self):
        '''文档上传成功'''
        global ADDURL
        files = {'file': open('F:/MyqWork/test.docx', 'rb')}
        response = requests.request("POST",ADDURL,files=files)
        files.clear()
        r = response.json()
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % ADDURL)
        print("上传文档操作:")
        print("返回数据: %s" % r)
        self.assertEqual(r['errorCode'],0)
        docId = r['datas']['docId']
        try:
            self.with_docId.withWriteDocId(docId)
        except Exception as e:
            print(e)












