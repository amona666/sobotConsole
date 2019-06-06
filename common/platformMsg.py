#coding:utf-8
import pymysql
import time
import hashlib
import requests
import random

class PlatformMsg():

    def __init__(self,appId,appKey,createTime):
        self.appId = appId
        self.appKey = appKey
        self.createTime = createTime
        self.expire = "24"
        self.host = "http://test.sobot.com/open/platform/"
        self.action = "chat_user_robot_ask"
        self.sysNum = "99cab16ac91e456c9d67272e09f964c8"
        self.partnerId = random.randint(0,999)

    def createSign(self):
        '''开放平台--获取签名（sign），appId、appKey、createTime以字符串方式拼接后经过MD5进行加密'''
        sign_str = self.appId + self.appKey + self.createTime
        sign_byte = sign_str.encode(encoding="utf-8")
        sign_md5 = hashlib.md5()
        sign_md5.update(sign_byte)
        sign = sign_md5.hexdigest()
        print("企业签名sign:", sign)
        return sign

    def getAccessToken(self,sign):
        '''通过企业签名sign获取access_token'''
        apiUrl = "getAccessToken.json"
        url = self.host + apiUrl
        data = {
            "appId":self.appId,
            "createTime":self.createTime,
            "sign":sign,
            "expire":self.expire
        }
        res =  requests.get(url,params=data)
        result =res.json()
        access_token = result["data"]["access_token"]
        return access_token

    def consultRobot(self,access_token):
        '''用户咨询机器人接口--可通过调用该接口实现以用户的身份咨询机器人并获取答案'''
        apiUrl = "api.json"
        url = self.host + apiUrl
        body = {
            "action":self.action,
            "access_token":access_token,
            "data":{
                "sysNum":self.sysNum,
                "partnerId":self.partnerId,
                "question":"question" + str(random.randint(0,999)),  #用户问题--必填
                "uname":"platform" + str(random.randint(0,999)),  #用户昵称--非必填
                "source":random.randint(0,4)  #用户渠道：0-pc,1-微信，2-app,3-微博，4-移动网站--非必填
                # "robotFlag":"",  #机器人编号--非必填
                # "questionFlag":"",  #问题类型：点击-1，输入-0--非必填
                # "requestText":""  #问题内容（questionFlag=0时，传入原问题；questionFlag=1时，传入docId）
            }
        }

        res = requests.post(url=url,json=body)
        print(res.url)
        print("咨询机器人请求参数：",body)
        result = res.json()
        print(result)
        return result


    def requestService(self):
        ''''''
        pass
    def consultService(self):
        pass
    def endSession(self,access_token,action="chat_user_out"):
        '''用户结束会话接口--可通过调用该接口来结束某个用户当前的会话'''
        apiUrl = "api.json"
        url = self.host + apiUrl
        body = {
            "action":action,
            "access_token":access_token,
            "data":{
                "sysNum":self.sysNum,
                "partnerId":self.partnerId
            }
        }
        res = requests.post(url=url,json=body)
        print("用户结束会话请求参数：",body)
        result = res.json()
        print(result)
        return result








if __name__ == "__main__":
    # 链接数据库
    # 打开数据库连接
    db = pymysql.connect("47.92.44.247", "sobot_basic", "SoboT321", "sobot_db")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)

    # 查询appId数据信息
    sql = "SELECT app_id FROM platform_open_info where company_id='99cab16ac91e456c9d67272e09f964c8'"
    cursor.execute(sql)
    appId_tuple = cursor.fetchone()
    # print(type(appId_tuple))

    # 元组转换字符串
    appId = "".join(tuple(appId_tuple))
    print("查询appId数据信息：%s" %appId)
    # print(type(appId))

    # 查询appKey数据信息
    sql = "SELECT app_key FROM platform_open_info where company_id='99cab16ac91e456c9d67272e09f964c8'"
    cursor.execute(sql)
    appKey_tuple = cursor.fetchone()
    # 元组转换字符串
    appKey = "".join(tuple(appKey_tuple))
    print("查询appKey数据信息：%s" %appKey)

    # 关闭数据库连接
    db.close()

    createTime = str(round(time.time()))
    print(createTime)

    p = PlatformMsg(appId,appKey,createTime)
    sign = p.createSign()
    expire = 24
    access_token = p.getAccessToken(sign)
    print("获取token：",access_token)
    result = p.consultRobot(access_token)
    print("输出咨询机器人结果：",result)
    result = p.endSession(access_token)
    print("输出用户结束会话结果：",result)

