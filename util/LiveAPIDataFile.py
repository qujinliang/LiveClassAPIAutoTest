import time
from data.DataSQL import DataSQL

# 线上"180CDC15E4801E55"
USERID = "45E64C2178BABA69"
# 线上"E9664C1FFA9B08D09C33DC5901307461"
ROOMID = "42A8012C26122E399C33DC5901307461"
# 线上 "E0AADAB234FB6B3D"
RECORID = "BD6689A20F863100"
# 线上 "6AF2C2C15A524217"
LIVEID = "3DC85D781667C629"
# 线上 "830603017655784C9C33DC5901307461"
VIDEOID = "806FA30B438D98A6FC9558351D509E7C"

# http://view.csslcloud.net/api/view/index?roomid=E9664C1FFA9B08D09C33DC5901307461&userid=180CDC15E4801E55&autoLogin=true&viewername=123&viewertoken=123
global name
name = ""
class LiveAPIData(object):

    def urlData(self):
        url = "https://ccapi.csslcloud.net"
        # url = "https://ccapi-1.csslcloud.net"
        return url

    def withRoomIdData(self):
        # 读取存入的直播间ID
        with open('./data/roomId_data.txt','r',encoding='utf-8') as f:
            live_roomid = f.read()
        return live_roomid

    def withDocIdData(self):
        # 读取docId
        with open('./data/docId.txt','r',encoding='utf-8') as f:
            docId = f.read()
        return docId

    def insert_roomid(self,name='classtest.db',userid=USERID,roomid=None):
        # 操作数据库insert函数，把roomid存入ROOMIDS表中
        sql = "INSERT INTO ROOMIDS (ID,USERID,ROOMID)\
               VALUES(NULL ,:sql_userid,:sql_roomid)"
        insert_dict = {'sql_userid':userid,'sql_roomid':roomid}
        DataSQL.inster_data(self,name=name,insert_data=sql,insert_dict=insert_dict)

    def select_roomid(self,name='classtest.db'):
        sql = "SELECT ID,ROOMID,ADD_TIME from ROOMIDS"
        sql_data = DataSQL.select_data(self,name=name,select_data=sql)
        roomid = sql_data[-1][1]
        return roomid

    def startData(self):
        # roomid = LiveAPIData.withRoomIdData(self)
        roomid = LiveAPIData.select_roomid(self)
        start_data = {"userid":USERID,"roomid":ROOMID}
        nouserid_data = {"roomid":roomid}
        return start_data,nouserid_data

    def stopData(self):
        roomid = LiveAPIData.withRoomIdData(self)
        stop_data = {"userid":USERID,"roomid":ROOMID}
        nouserid_data = {"roomid":roomid}
        return stop_data,nouserid_data

    def createData(self):
        global name
        name = "autoTestCreate%s" % time.strftime("%Y-%m-%d %H_%M_%S")
        create_data = {"userid":USERID,"name":name,"room_type":2,"publisherpass":"123","audience_authtype":
                       2,"talker_authtype":2,"desc":"autoTestCreateRoom"}
        create_all_data = {"userid":USERID,"name":name,"room_type":2,"publisherpass":"123","audience_authtype":
                       2,"audience_pass":"321","talker_pass":"123","inspector_authtype":"2","talker_authtype":2,
                           "inspector_pass":"123","templatetype":"1","mergetype":"1","max_users":"15","max_streams":"1",
                           "desc":"autoTestCreateRoom","video_mode":"2","talker_bitrate":"500","publisher_bitrate":"500",
                           "classtype":"2","presenter_out":True,"light_mark":"1","show_exit":"0","ppt_support":True,
                           "screen_lock":"1","desktop_audio":"1","manual_record":"1","record_bitrate":"0","warm_open":"1"}
        create_white_data = {"userid":USERID,"name":name,"room_type":2,"publisherpass":"123","talker_authtype":3,
                            "white_list":"{'user':'123'}"}
        bat_create_data = {"userid":USERID,"name":name,"room_type":5,"publisherpass":"123","talker_authtype":2}
        return create_data,create_all_data,create_white_data,bat_create_data

    def updateData(self):
        name = "autoTestUpdate%s" % time.strftime("%Y-%m-%d %H_%M_%S")
        live_roomid = LiveAPIData.withRoomIdData(self)
        update_data = {"userid":USERID,"live_roomid":live_roomid,"name":name,"room_type":2,"publisherpass":"123","audience_authtype":
                       2,"talker_authtype":2,"desc":"autoTestUpdateRoom","allow_chat":True,"allow_audio":True,"allow_speak":True,}
        bat_pudata_data = {"userid":USERID,"live_roomid":live_roomid,"name":name,"room_type":2,"publisherpass":"123","audience_authtype":
                       5,"talker_authtype":5,"desc":"autoTestUpdateRoom","allow_chat":True,"allow_audio":True,"allow_speak":True,}
        return update_data,bat_pudata_data

    def closeData(self):

        live_roomid = LiveAPIData.withRoomIdData(self)
        close_data = {"userid":USERID,"roomid":live_roomid}
        return close_data

    def listData(self):
        global name
        roomid = LiveAPIData.withRoomIdData(self)
        list_data = {"userid":USERID}
        list_all_data = {"userid":USERID,"name":name,"status":10,"page":1,"lines":100,"roomid":roomid}
        list_bat_data = {"userid":USERID,"name":name,"status":30}
        return list_data,list_all_data,list_bat_data

    def detailData(self):
        live_roomid = LiveAPIData.withRoomIdData(self)
        close_data = {"userid":USERID,"roomid":live_roomid}
        return close_data

    def linkData(self):
        live_roomid = LiveAPIData.withRoomIdData(self)
        link_data = {"userid":USERID,"roomid":live_roomid}
        return link_data

    def set_singleData(self):
        live_roomid = LiveAPIData.withRoomIdData(self)
        setsingle_data = {"userid":USERID,"roomid":live_roomid,"status":2}
        return setsingle_data

    def sessionidData(self):
        live_roomid = LiveAPIData.withRoomIdData(self)

        # 如果教室有讲师登陆密码了，那么传的参数必须有password
        role0_data = {"name":"testauto","userid":USERID,"roomid":live_roomid,"password":"123","role":'0',
                      "client":'0'}
        role1_data = {"name":"testauto","userid":USERID,"roomid":live_roomid,"role":'1',"client":'0'}
        role2_data = {"name":"testauto","userid":USERID,"roomid":live_roomid,"role":'2',"client":'0'}
        client_data = {"name":"testauto","userid":USERID,"roomid":live_roomid,"role":'1',"client":'1'}
        bat_data = {"name":"testauto","userid":USERID,"roomid":live_roomid,"role":'4',"client":'1'}
        return role0_data,role1_data,role2_data,client_data,bat_data

    def chatmsgData(self):
        chatmsg_data = {"roomid":ROOMID,"userid":USERID,"liveid":LIVEID}
        return chatmsg_data

    def recordData(self):
        record_data = {"roomid":ROOMID,"userid":USERID}
        return record_data

    def searchData(self):
        # 实际userid必填
        search_data = {"userid":USERID,"recordid":RECORID}
        return search_data

    def addData(self):
        add_data = {"doc_name":"test","account_id":USERID,"doc_size":"11588"}
        return add_data

    def deleteData(self):
        doc_id = LiveAPIData.withDocIdData(self)
        delete_data = {"doc_id":doc_id,"account_id":USERID}
        return delete_data

    def docListData(self):
        doc_list = {"account_id":USERID}
        return doc_list

    def authListData(self):
        auth_list_data = {"account_id":USERID,"room_id":ROOMID}
        return auth_list_data

    def relateData(self):
        room_id = LiveAPIData.withRoomIdData(self)
        doc_id = LiveAPIData.withDocIdData(self)
        relate_data = {"account_id":USERID,"room_id":room_id,"doc_id":doc_id}
        return relate_data

    def unrelateData(self):
        room_id = LiveAPIData.withRoomIdData(self)
        doc_id = LiveAPIData.withDocIdData(self)
        unrelate_data = {"account_id":USERID,"room_id":room_id,"doc_id":doc_id}
        return unrelate_data

    def createuploadinfoData(self):
        createuploadinfo_data = {"account_id":USERID,"title":"autotest001","filename":"autotest001"}
        return createuploadinfo_data

    def videoRelateData(self):
        video_relate_data = {"account_id":USERID,"room_id":ROOMID,"video_id":VIDEOID}
        return video_relate_data

    def videoUnrelateData(self):
        video_unrelate_data = {"account_id":USERID,"room_id":ROOMID,"video_id":VIDEOID}
        return video_unrelate_data

    def warmSetData(self):
        warm_set_data = {"account_id":USERID,"room_id":ROOMID,"video_id":VIDEOID}
        return warm_set_data

    def warmUnsetData(self):
        warm_unset_data = {"account_id":USERID,"room_id":ROOMID,"video_id":VIDEOID}
        return warm_unset_data

    def onrelatedData(self):
        onrelate_data = {"account_id":USERID,"room_id":ROOMID}
        return onrelate_data


