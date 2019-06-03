#coding:"utf-8"
import os
import unittest
import HTMLTestRunner_cn
import time
# 用例路径
case_path = os.path.join(os.getcwd(), "case")
print("用例存放路径：",case_path)
# 报告存放路径
if os.path.exists("report"):
    report_path = os.path.join(os.getcwd(), "report")
    print("报告存放路径：",report_path)
else:
    os.mkdir("report")
    report_path = os.path.join(os.getcwd(), "report")
    print("报告存放路径：", report_path)

#定义add_case函数，加载所有测试用例
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py",top_level_dir=None)
    print(discover)
    return discover

# html报告文件路径
resultTime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
print(type(resultTime))
report_abspath = os.path.join(report_path, "result_%s.html"%resultTime)
fp = open(report_abspath, "wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

# 调用all_case函数返回值
runner.run(all_case())
fp.close()

# if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    # # html报告文件路径
    # report_abspath = os.path.join(report_path, "result.html")
    # fp = open(report_abspath, "wb")
    # runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
    #                                        title=u'自动化测试报告,测试结果如下：',
    #                                        description=u'用例执行情况：')
    #
    # # 调用add_case函数返回值
    # runner.run(all_case())
    # fp.close()