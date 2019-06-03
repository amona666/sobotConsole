import logging
import time
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#判断日志文件夹是否存在
logPath = os.path.join(os.getcwd(),"log")
print("输出日志文件路径:",logPath)


if os.path.exists("log"):
    logPath = os.path.join(os.getcwd(), "log")
else:
    os.mkdir("log")
    logPath = os.path.join(os.getcwd(), "log")

#创建handler，输出到文件
logTime = time.strftime("%Y-%m-%d",time.localtime())
print("输出日志时间：",logTime)
handler = logging.FileHandler(logPath +"/"+"log_%s.log"%logTime,mode="wb")
print("输出handler：",handler)
handler.setLevel(logging.INFO)

#创建handler，输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#创建logging format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
ch.setFormatter(formatter)

#添加handler到logger
logger.addFilter(handler)
logger.addFilter(ch)

logger.info("info logging")
logger.debug("debug logging")
logger.warning("warning logging")
logger.error("error logging")
logger.critical("critical logging")





