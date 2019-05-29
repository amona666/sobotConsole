#coding:utf-8
from urllib import parse

import requests
from common.fileTool import *
import unittest
import ddt
from apiPage.loginPage import *


@ddt.ddt
class Login(unittest.TestCase):
    @ddt.file_data("//home//amona//Dev/workspace//sobotConsole//conf//testConf.yaml")
    def test_login_suc(self,**kwargs):
        print(kwargs)
        host = kwargs.get("host","http://test.sobot.com")
        url = kwargs.get("url")
        detail = kwargs.get("detail","未编写用例描述")
        print(detail)
        #动态的用例描述
        self._testMethodName = detail
        method = kwargs.get("method","get")
        checkPoint = kwargs.get("checkPoint","000000")
        testData = kwargs.get("testData",{})

        #获取Yaml测试数据中密码数据
        loginPwd = testData["loginPwd"]
        print("未加密数据：",loginPwd)

        #密码加密处理
        loginMsg = loginPage()
        loginPwd_b64 = loginMsg.createLoginPwd(loginPwd)
        print("加密数据：",loginPwd_b64)

        #更新测试数据中的密码数据
        testData.update(loginPwd=loginPwd_b64)
        print("更新后的测试数据：",testData)

        try:
            if method == "get":
                res = requests.get(url= host+url,params=testData)
                result = res.json()
                print("输出测试结果：",result)
                self.assertEqual(result["retCode"],"000000",msg=result["msg"])
            else:
                res = requests.post(url= host+url,data=testData)
                result = res.json()
                print("输出测试结果：", result)
                print("retCode:",result["retCode"])
        except Exception as errorMsg:
            result = errorMsg

        for check in checkPoint:
             self.assertEqual(checkPoint,result["retCode"],msg="预期结果不符，预期结果【%s】，实际结果【%s】"%(checkPoint,result["retCode"]))
# #装载测试用例
# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Login))


if __name__ == "__main__":
    unittest.main()

