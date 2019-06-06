#conding:utf-8
import requests
from common.platformMsg import *
import random
import pymysql
import random


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
appId = "".join(tuple(appId_tuple))
print("查询appId数据信息：%s" %appId)

# 查询appKey数据信息
sql = "SELECT app_key FROM platform_open_info where company_id='99cab16ac91e456c9d67272e09f964c8'"
cursor.execute(sql)
appKey_tuple = cursor.fetchone()
appKey = "".join(tuple(appKey_tuple))
print("查询appKey数据信息：%s" %appKey)

# 关闭数据库连接
db.close()

createTime = str(round(time.time()))
print(createTime)

# expire = 24

p = PlatformMsg(appId,appKey,createTime)
sign = p.createSign()
print("sign:",sign)
access_token = p.getAccessToken(sign)
print("access_token:",access_token)
p.consultRobot(access_token)
print(p.consultRobot(access_token))
p.endSession(access_token)
url = "http://test.sobot.com/open/platform/api.json"
body = {
    "action":"chat_user_comment",
    "access_token":access_token,
    "data":{
        "sysNum":"99cab16ac91e456c9d67272e09f964c8",  #企业标识，公司id
        "partnerId":p.partnerId,  #企业自己的用户ID，
        "type":random.randint(0,1),  #0：机器人评价 1：人工评价
        "solved":random.randint(0,1),  #0：未解决 1：解决
        "score":random.randint(0,5), #人工评价分数（1、2、3、4、5）
        "tag":"",  #评价标签
        "remark":"hello world!!!"  #评价内容

    }

}

res = requests.post(url=url,json=body)
print(res.url)
print("打印请求参数：",body)
result = res.json()
print(result)
# a949d7abf9c640809b6cb9bc73a03702
print(res.status_code)
if res.status_code == 200:
    if result["data"]["cid"]:
        print("测试用例执行成功！！！")
    else:
        print("测试用例执行失败！！！")





if __name__ == "__main__":
    print(random.randint(0,999))