import subprocess
from logger import Logger
import psutil
import requests
from AES_DECR import encrypyDecByTwo
from base_util import utilBase
import time
from aes_tool import aes_tool

myLogger = Logger(logger="tomcat").getlog()

class tomcatutil(utilBase):

    # 启动tomcat
    def startTomcat(self,serviceName):
        try:
            isSucc = self.startService(serviceName)
            if isSucc == True:
                myLogger.info('服务名：%s 服务启动中.....' % serviceName)
                return True
            myLogger.info('服务名：%s 服务启动失败' % serviceName)
            return False
        except Exception as e:
            myLogger.info('服务名：%s 服务启动异常 %s' % (serviceName,e))
            return False

    # 关闭tomcat
    def stopTomcat(self,serviceName):
        '''
           :param serviceName:服务名
           :return:
        '''
        try:
            isSucc = self.taskkillService(serviceName)
            if isSucc == True:
                myLogger.info('服务名：%s 关闭成功' % serviceName)
                time.sleep(10)
                return True
            myLogger.info('服务名：%s 关闭失败' % serviceName)
            return False
        except Exception as e:
            myLogger.info('服务名：%s 关闭失败 %s' % (serviceName,e))
            return False

    # 清空tomcat所有日志
    def clearLog(self,logs_path, serviceName):
        '''
            :param logs_path:
            :return:
        '''
        # cmd_all = "rd /s/q logs "
        cmd_all = "del /f/s/q *.log "
        try:
            retcode = subprocess.call(cmd_all, shell=True, cwd=logs_path)
            if retcode == 0:
                myLogger.info('服务名：%s 清理日志成功' % serviceName)
        except Exception as e:
            myLogger.info("服务名：%s 清理日志失败 %s" % (serviceName,e))

    #测试接口调用
    # @encrypyDecByTwo
    def testUrl(self,fisUrl,endUrl):
        url = fisUrl + endUrl
        try:
            request = requests.get(url,timeout=180)
            myLogger.info(request.status_code)
            if request.status_code == 200:
                myLogger.info('测试接口调用成功：%s' %url)
                return True
            myLogger.info('测试接口调用失败：%s' % request.content)
            return False
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            myLogger.error(url)
            myLogger.error('测试接口调用超时或连接异常--%s' % e)
            return False
        except Exception as e:
            myLogger.error(url)
            myLogger.error('测试接口调用异常--%s' % e)
            return False
