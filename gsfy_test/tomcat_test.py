import requests
from AES_DECR import encrypy_decrator
import os
import time
import datetime
import sched
import configparser
import re

# tomcat名，对应路径中tomcat
tomcats =['Tomcat7-test']
tomcats =['Tomcat7app1','Tomcat7app2','Tomcat7app3','Tomcat7app4',
          'Tomcat7app5','Tomcat7app6','Tomcat7app7','Tomcat7app8']

# 要检查的url
testUrl = "/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435"

#nginx路径
nginx_url = "D:\\nginx\\conf\\nginx.conf"

# @encrypy_decrator('http://app.gsfybjy.com/phpatient/app/appservice?querystr=')
def reqArticleInfo(url):
    print(url)
    try:
        request = requests.get(url)
        print(request.status_code)
        if request.status_code == 200:
            return True
        else:
            return False
    except (requests.exceptions.Timeout,requests.exceptions.ConnectionError) as e:
        print('超时或连接异常--%s',e)
        return False
    except Exception as e:
        print(e)
        return False

# 启动tomcat
def startTomcat(serviceName):
    mystr = os.popen("net start "+ serviceName)  # popen与system可以执行指令,popen可以接受返回对象
    mystr = mystr.read()  # 读取输出
    print(mystr)

# 关闭tomcat
def stopTomcat(serviceName):
    mystr = os.popen("net stop " + serviceName)  # popen与system可以执行指令,popen可以接受返回对象
    mystr = mystr.read()  # 读取输出
    print(mystr)

# 清空tomcat所有日志
def clearLog():
    pass

def readNginxConf(nginx_conf):
    config = configparser.ConfigParser()
    config.read_file(open('D:\\nginx\\conf\\nginx4.conf').read())
    # config.read("D:\\nginx\\conf\\nginx4.conf")
    # config.read()
    # sections = config.sections()
    # print(sections)

if __name__ == '__main__':
    # schedule = sched.scheduler(time.time, time.sleep)
    readNginxConf('nginx.conf')
    # for serviceName in tomcats:
    #     print(serviceName)
    #     startTomcat(serviceName)
    #     # 检查tomcat启动是否成功
    #     isSucc = reqArticleInfo("http://localhost:8081/")
'''
 while True:
        while True:
            now = datetime.datetime.now()
            print(now)
            print(now.hour)
            print(now.minute)
            if now.hour == 14 and now.minute == 52:
                break
            # 不到时间就等20秒之后再次检测
            time.sleep(20)
        for serviceName in tomcats:
            print(serviceName)
            startTomcat(serviceName)
            # 检查tomcat启动是否成功
            isSucc = reqArticleInfo("http://localhost:8081/")
            if not isSucc:
                break
            # time.sleep(20)
            # stopTomcat(serviceName)
'''

