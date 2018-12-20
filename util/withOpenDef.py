


class WithOpenDef(object):
    try:
        def withWriteRoomId(self,roomid):
            with open('./data/roomId_list.txt','a',newline='\n',encoding='utf-8') as f:
                f.write(roomid + '\n')

        def withWiteLiveId(self,liveid):
            with open('./data/liveId_data.txt','w',encoding='utf-8') as f:
                f.write(liveid)

        def withWriteDocId(self,docid):
            with open('./data/docId.txt', 'w', encoding='utf-8') as f:
                f.write(docid)

    except Exception as e:
        print(ellipsis)

