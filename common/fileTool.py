#conding:utf-8
from apiPage.loginPage import *
import yaml
import os



class fileTool():

    #遍历yaml文件，处理json数据中的loginPwd的问题
    def operateYaml(self, data):
        for key in data.keys():
            value = data[key]
            if type(value) is str and len(value) > 8 and value.startswith("ENCODE("):
                data[key] = loginPage.createLoginPwd(value[7:-1])
        return data

    #读取yaml配置文件
    def readYamlConf(self,fileDir,fileName):
        scriptPath = os.path.abspath("..")
        print("输出脚本的父级路径：",scriptPath)
        casePath = scriptPath + "/" +fileDir
        print("输出yaml文件路径：",casePath)

        testData = open(casePath + "/" + fileName, "rb")
        data = yaml.load(testData, Loader=yaml.FullLoader)
        print("data:", data)
        print(type(data))
        return data


if __name__ == "__main__":
    t = fileTool()
    t.rendYamlConf("conf","testConf.yaml")
