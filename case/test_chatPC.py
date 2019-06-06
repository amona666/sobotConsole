#coding:utf-8

import requests

url = "http://test.sobot.com/chat/user/init.action"
header = {
    "Cookie":"gr_user_id=2f97d3ef-939a-4f30-9daa-d966ede5d03a; 99cab16ac91e456c9d67272e09f964c8_u=b6378eaeb9d245ecb21ad0263db386db; tenant_cookie_adminId=XTpFyvfTO3IWOC2FtE5hXIs9hSFbFISB%2FBj26Vb7jObKmIIDJczXZPruMlkGUwnG; Hm_lvt_8abc47d589af6c5e062a2a368a4baff6=1558443999,1558927032,1558928076,1559619370; Hm_lpvt_8abc47d589af6c5e062a2a368a4baff6=1559619370; isLoadPage=loaded; gr_session_id_7e033ff9a65e12d8fd0333ce9e9ab0d2=8f1dea1e-8ed6-43ee-a47d-40e5cf007152; gr_session_id_7e033ff9a65e12d8fd0333ce9e9ab0d2_8f1dea1e-8ed6-43ee-a47d-40e5cf007152=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%224aa1f172619948588a3ef3443eb6446c%22%2C%22%24device_id%22%3A%2216af74ac651497-0291d4a45ced8a-5f1d3a17-2073600-16af74ac6524e3%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Ftest.sobot.com%2Fconsole%2Flogin%22%7D%2C%22first_id%22%3A%2216af74ac651497-0291d4a45ced8a-5f1d3a17-2073600-16af74ac6524e3%22%7D"
}
body = {
    "ack": "1",
    "sysNum": "99cab16ac91e456c9d67272e09f964c8",
    "source": "0",
    "tranFlag": "0",
    "partnerId": "hakga;",
    "isReComment": "1",
    "transferAction":"["
                     "{'actionType':'to_group','deciId':'xxx','optionId':'3','spillId':'4'},"
                     "{'actionType':'to_group','deciId':'xxx','optionId':'4'}]"

}

res = requests.get(url=url,params=body)
result = res.json()
print("打印请求参数：",res.url)
print("打印输出结果：",result)