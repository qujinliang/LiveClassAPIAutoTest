import sqlite3
import os
import time
# 把当前目录切换到这里，应该统一卸载一个配置文件里
os.chdir('F:\\LiveClassAPIAutoTest')

class DataSQL(object):
    def create_database(self,name):
        conn = sqlite3.connect(r'./data/%s'%name)
        print("Opened datebase successfully")
        return conn

    def create_table(self,name,create_data):
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            c.execute(create_data)
        except sqlite3.OperationalError as e:
            print("重复，表已经存在%s"%e)
        finally:
            conn.commit()
            conn.close()
        print("Table created successfully")


    def inster_data(self,name,insert_data,insert_dict=None):
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            if insert_dict:
                c.execute(insert_data,insert_dict)
            else:
                c.execute(insert_data)
        except sqlite3.IntegrityError as e:
            print("插入新数据异常%s"%e)
        finally:
            conn.commit()
            conn.close()
        print("Operation done suceessfully")

    def select_data(self,name,select_data):
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            cursor = c.execute(select_data)
            # print(list(cursor))
            # for row in cursor:
            #     print ("ID = ", row[0])
            #     print ("USERID = ", row[1])
            #     print("ROOMID = ", row[2]),"\n"
            #     print('-'*50)
            return (cursor.fetchall())
        except Exception as e:
            print(e)
        finally:
            conn.close()
        print("Operation done suceessfully")

    def delete_data(self,name,delete_data):
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            c.execute(delete_data)
        except Exception as e:
            print((e))
        finally:
            conn.commit()
            conn.close()
        print("Operation done suceessfully")

    def delete_table(self,name,delete_table):
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            c.execute(delete_table)
        except Exception as e:
            print(e)
        finally:
            conn.commit()
            conn.close()
        print("delete table done")



if __name__ == '__main__':
    # pass
    # create_data = ('''CREATE TABLE ROOMIDS
    #           (ID INTEGER PRIMARY KEY  NOT NULL,
    #           USERID      CHAR(50)       NOT NULL,
    #           ROOMID      CHAR(50)       NOT NULL,
    #           ADD_TIME    TIMESTAMP     NOT NULL  DEFAULT (datetime('now','localtime')));''')

    # insert_data = ("INSERT INTO ROOMIDS (ID,USERID,ROOMID)\
    #                VALUES(NULL ,'testuserid2','testuserroomid3')")
    #
    # delete_data = "DELETE from COMPANY where ID=5;"
    # delete_table = "DROP TABLE ROOMIDS "
    # #
    select_data = "SELECT ID,ROOMID,ADD_TIME from ROOMIDS"
    #
    dat = DataSQL()

    # dat.create_table(name='classtest.db',create_data=create_data)
    # dat.inster_data(name='test.db',insert_data=insert_data)
    # dat.inster_data(name = 'classtest.db',insert_data=insert_data)
    # dat.delete_data(name='test.db',delete_data=delete_data)
    # dat.delete_table(name='classtest.db',delete_table=delete_table)
    resut = dat.select_data(name='classtest.db',select_data=select_data)
    print({'roomid':resut[-1][1]})