import os
import time
import datetime
from logger import Logger
from nginx_util import nginxutil
from tomcat_util import tomcatutil
from configs import configs
from alarm import alarm

myLogger = Logger(logger="main").getlog()

def restartTomcats(tomcatDict, testUrl,tomcatUrlDict,tomcatTimeout,titalTimeout):
    # 重启tomcat
    titalOutTime = (datetime.datetime.now() + datetime.timedelta(minutes=float(titalTimeout))).timestamp()
    for serviceName, serviceLog_path in tomcatDict.items():
        tomcatOutTime = (datetime.datetime.now() + datetime.timedelta(minutes=float(tomcatTimeout))).timestamp()
        myLogger.info('-----------------------------%s开始-------------------------------'%serviceName)
        while True:
            # 单个tomcat超时时间
            tomcatCurTime = datetime.datetime.now().timestamp()
            if tomcatCurTime > titalOutTime:
                #发送邮箱警报
                myalarm.sendMutiMail()
                myLogger.info('总体超出最大启动时间 此次重启操作结束')
                return False
            if tomcatCurTime > tomcatOutTime:
                # 单个tomcat超过了启动时间 结束本次重启任务
                # 并报警通知相关人员# 发送邮箱警报
                myalarm.sendMutiMail()
                myLogger.info('%s超出最大启动时间 此次重启操作结束' %serviceName)
                return False
            # 关闭先tomcat
            isStopSucc = tomcatUtil.stopTomcat(serviceName)
            if isStopSucc == False:  # true停止成功  false停止失败
                # 停止失败的处理 # 并报警通知相关人员# 发送邮箱警报
                myalarm.sendMutiMail()
                return False
            # 清理tomcat日志
            tomcatUtil.clearLog(serviceLog_path, serviceName)
            # 启动tomcat
            isStartSucc = tomcatUtil.startTomcat(serviceName)
            if isStartSucc == False:
                # 启动tomcat服务失败 报警通知相关人员
                myalarm.sendMutiMail()
                return False
            # 检查tomcat启动是否成功 超时时间默认180
            # isSucc = tomcatUtil.testUrl(tomcatUrlDict[serviceName], testUrl,timeout=180)
            isSucc = tomcatUtil.requestUrl(tomcatUrlDict[serviceName], testUrl,timeout=180)
            # 启动失败
            if isSucc == False:
                continue
            else:
                break
    return True


if __name__ == '__main__':
    # 获取配置信息
    config = configs()
    tomcatDict, testUrl, nginxName, nginxPath,tomcatUrlDict,tomcatTimeout,titalTimeout = config.getConfigs()
    #清Nginx日志
    nginxUtil = nginxutil(nginxName,nginxPath)
    nginxUtil.clearLog()
    # 重启tomcat
    tomcatUtil = tomcatutil()
    currentTime = datetime.datetime.now()
    myalarm = alarm()
    restartTomcats(tomcatDict, testUrl, tomcatUrlDict, tomcatTimeout, titalTimeout)
    myLogger.info('\n\n')
    myLogger.info(30 * '*******')
    myLogger.info('此次结束\n\n')
    '''
    while True:
        currentTime = datetime.datetime.now()
        restartTomcats(tomcatDict, testUrl,tomcatUrlDict,tomcatTimeout,titalTimeout)
        myLogger.info('\n\n\n\n')
        myLogger.info(30*'*******')
        myLogger.info('此次结束')
        time.sleep(1200)
    '''