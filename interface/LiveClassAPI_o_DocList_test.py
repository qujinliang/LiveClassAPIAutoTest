import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveClassAPIDocListTest(unittest.TestCase):
    """查询文档接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = LiveAPIData.urlData(self)
        url = url+"/api/v1/doc/list?"
        self.doc_list_data = LiveAPIData.docListData(self)
        t = THQS.thqs()
        doc_list_data = t.get_thqs(self.doc_list_data)
        self.doc_list_url = url+doc_list_data
        self.live = LiveAPIRequests.LiveAPIRequests
        self.doc_id = LiveAPIData.withDocIdData(self)

    def tearDown(self):
        pass

    def test_a_list(self):
        '''获取共享文档列表成功'''
        r = self.live.SendOut(self,self.doc_list_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.doc_list_url)
        print("输入参数：%s" % self.doc_list_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')
        # self.assertEqual(r['docs']['id'])
        doc_id = r['docs']
        # 判断文档ID在这个文档列表中
        for i in doc_id:
            if i['id'] == str(self.doc_id):
                self.assertEqual(i['id'],self.doc_id)













