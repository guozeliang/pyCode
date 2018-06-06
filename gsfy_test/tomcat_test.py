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
    return tomcatDict,testUrl,nginxName,nginxPath

def clearNginxLog(nginx_log_path,nginx_path):
    cmd_all = "del /f/s/q *.log "
    try:
        retcode1 = subprocess.call("nginx -s stop", shell=True, cwd=nginx_path)
        retcode = subprocess.call(cmd_all, shell=True, cwd=nginx_log_path)
        # retcode1 = subprocess.call( 'nginx -s reload', shell=True, cwd=nginx_path)
        # child = subprocess.Popen("nginx",shell=True,cwd=nginx_path)
        child = subprocess.call("nginx",shell=True,cwd=nginx_path,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    # 获取配置信息
    tomcatDict, testUrl, nginxName, nginxPath = getConfig()
    #清Nginx日志
    nginxUtil = nginxutil(nginxName,nginxPath)
    nginxUtil.clearLog()
    # 重启tomcat
    tomcatUtil = tomcatutil()
    for serviceName, serviceLog_path in tomcatDict.items():
        # 关闭先tomcat
        isStopSucc = tomcatUtil.stopTomcat(serviceName)
        if isStopSucc== False:#true停止成功  false停止失败
            # 停止失败的处理
            pass
        # 清理tomcat日志
        tomcatUtil.clearLog(serviceLog_path,serviceName)
        # 启动tomcat
        isStartSucc = tomcatUtil.startTomcat(serviceName)
        if isStartSucc == True:
            pass
        # 检查tomcat启动是否成功
        isSucc = tomcatUtil.testUrl("http://localhost:8081/")
        if not isSucc:
            break