import requests
import os
import time
import datetime
import subprocess
from configparser import ConfigParser

from nginx_util import nginxutil
from tomcat_util import tomcatutil

# tomcat名，对应路径中tomcat
# tomcats =['Tomcat7-test','Tomcat7-test1']
# tomcats =['Tomcat7app1','Tomcat7app2','Tomcat7app3','Tomcat7app4',
#           'Tomcat7app5','Tomcat7app6','Tomcat7app7','Tomcat7app8']

#获取配置信息
def getConfig():
    config = ConfigParser()
    config.read("config.conf")
    tomcatDict = dict(config.items('tomcats_config'))
    testUrl = config.get('testurl_config', 'testurl')
    nginxName = config.get('nginx_config', 'nginxserivcename')
    nginxPath = config.get('nginx_config', 'nginxpath')
    tomcatUrlDict = dict(config.items('tomcats_url_config'))
    startTimeout = config.get('timout_config', 'tomcattimeout')
    titalTimeout = config.get('timout_config', 'titaltimeout')
    testurl = config.get('testurl_config', 'testurl')
    return tomcatDict,testUrl,nginxName,nginxPath,tomcatUrlDict,startTimeout,titalTimeout,testurl

def resTomcat(outTime):
    while True:
        curTime = datetime.datetime.now().timestamp()
        if curTime < outTime:
            # 关闭先tomcat
            isStopSucc = tomcatUtil.stopTomcat(serviceName)
            # 启动tomcat
            isStartSucc = tomcatUtil.startTomcat(serviceName)
            if isStartSucc == False:
                continue
            # 检查tomcat启动是否成功
            isSucc = tomcatUtil.testUrl(tomcatUrlDict[serviceName])
            if isSucc == True:
                return True
        else:
            return False

if __name__ == '__main__':
    # 获取配置信息
    tomcatDict, testUrl, nginxName, nginxPath,tomcatUrlDict,startTimeout,titalTimeout,testurl = getConfig()
    #清Nginx日志
    nginxUtil = nginxutil(nginxName,nginxPath)
    nginxUtil.clearLog()
    # 重启tomcat
    tomcatUtil = tomcatutil()
    titleOutTime = (datetime.datetime.now()+datetime.timedelta(minutes=float(titalTimeout))).timestamp()
    for serviceName, serviceLog_path in tomcatDict.items():
        curTime = datetime.datetime.now().timestamp()
        if curTime > titleOutTime:
            break
        # 关闭先tomcat
        isStopSucc = tomcatUtil.stopTomcat(serviceName)
        if isStopSucc== False:#true停止成功  false停止失败
            # 停止失败的处理
            break
        # 清理tomcat日志
        tomcatUtil.clearLog(serviceLog_path,serviceName)
        # 启动tomcat
        isStartSucc = tomcatUtil.startTomcat(serviceName)
        if isStartSucc == False:
            break
        # 检查tomcat启动是否成功
        isSucc = tomcatUtil.testUrl(tomcatUrlDict[serviceName],testurl)
        # isSucc = tomcatUtil.testGsfuUrl(tomcatUrlDict[serviceName],testurl)
        # 启动失败
        if isSucc == False:
            outTime = (datetime.datetime.now()+datetime.timedelta(minutes=float(startTimeout))).timestamp()
            isResSucc = resTomcat(outTime)
            if isResSucc == True:
                continue
            break