import requests
from AES_DECR import encrypy_decrator
import os
import time
import datetime
import subprocess

# tomcat名，对应路径中tomcat
tomcatDict={
    'Tomcat7-test':'C:\\Program Files\\Apache Software Foundation\\Tomcat 7.0_Tomcat7-test',
    'Tomcat7-test1':'C:\\Program Files\\Apache Software Foundation\\Tomcat 7.0_Tomcat7-test1'
}
# tomcats =['Tomcat7-test','Tomcat7-test1']
# tomcats =['Tomcat7app1','Tomcat7app2','Tomcat7app3','Tomcat7app4',
#           'Tomcat7app5','Tomcat7app6','Tomcat7app7','Tomcat7app8']

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
    call_cmd = "net start "+ serviceName
    retcode = subprocess.call(call_cmd)
    # mystr = os.popen("net start "+ serviceName)  # popen与system可以执行指令,popen可以接受返回对象
    # os.system()
    # mystr = mystr.read()  # 读取输出
    # print(mystr)

# 关闭tomcat
def stopTomcat(serviceName):
    '''
    :param serviceName:服务名
    :return:
        # mystr = os.popen("net stop " + serviceName)  # popen与system可以执行指令,popen可以接受返回对象
        # mystr = mystr.read()  # 读取输出
        # print(mystr)
        # pid = processinfo(serviceName)
        # os.popen("taskkill /PID {} /F".format(pid))
    '''
    pid = processinfo(serviceName)
    if pid == None:
        return True
    # 用subprocess杀进程
    try:
        retcode = subprocess.call("taskkill /PID {} /F".format(pid))
        print(retcode)
        if retcode == 0:
            return True
    except Exception as e:
        print('服务名：%s 关闭失败', serviceName)
        return False

import psutil
import re

def processinfo(processName):
    try:
        service = psutil.win_service_get(processName)
        return service.as_dict()['pid']
    except psutil.NoSuchProcess as e:
        print('没有找到服务名为：%s 的进程PID',processName)
        return None


# 清空tomcat所有日志
def clearLog(logs_path,serviceName):
    '''
    :param logs_path:
    :return:
        # os.chdir(logs_path)
        # os.popen("rd /s/q logs" )
        # os.popen("md logs")
    '''
    try:
        cmd_all = "rd /s/q logs "
        retcode = subprocess.call(cmd_all,shell=True,cwd=logs_path)
    except Exception as e:
        print(e)
        print("服务名：%s 清理日志失败",serviceName)


if __name__ == '__main__':
    for serviceName, serviceLog_path in tomcatDict.items():
        # 关闭先tomcat
        isStopSucc = stopTomcat(serviceName)
        if isStopSucc== False:#true停止成功  false停止失败
            # 停止失败的处理
            pass
        # 清理tomcat日志
        clearLog(serviceLog_path,serviceName)
        # 启动tomcat
        startTomcat(serviceName)
        # 检查tomcat启动是否成功
        isSucc = reqArticleInfo("http://localhost:8081/")
        if not isSucc:
            break