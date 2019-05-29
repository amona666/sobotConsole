#coding:utf-8
import base64

class loginPage():

    '''base64加密登录密码'''
    def createLoginPwd(self,pwd="sobot123"):

        #密码转换为字节类型
        pwd_bytes = pwd.encode()
        print(type(pwd_bytes))

        #base64加密登录密码
        pwd_b64 = base64.b64encode(pwd_bytes)
        print(pwd_b64)

        #加密密码转换为字符串类型
        loginPwd = pwd_b64.decode()
        print(loginPwd)
        return loginPwd



if __name__ == "__main__":
    lg = loginPage()
    password = lg.createLoginPwd()



