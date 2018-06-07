import subprocess
from logger import Logger
import psutil
import requests
from AES_DECR import encrypy_decrator
from base_util import utilBase

myLogger = Logger(logger="tomcat").getlog()

class tomcatutil(utilBase):
    # 获取pid
    # @classmethod
    # def processinfo(cls,processName):
    #     try:
    #         service = psutil.win_service_get(processName)
    #         return service.as_dict()['pid']
    #     except psutil.NoSuchProcess as e:
    #         # print('没有找到服务名为：%s 的进程PID'% processName)
    #         myLogger.info('没有找到服务名为：%s 的进程PID' % processName)
    #         return None

    # 启动tomcat
    def startTomcat(self,serviceName):
        call_cmd = "net start " + serviceName
        try:
            retcode = subprocess.call(call_cmd)
            if retcode == 0:
                myLogger.info('服务名：%s 启动成功' % serviceName)
                return True
            return False
        except Exception as e:
            myLogger.info('服务名：%s 启动失败' % serviceName)
            return False

    # 关闭tomcat
    def stopTomcat(self,serviceName):
        '''
           :param serviceName:服务名
           :return:
        '''
        pid = self.processinfo(serviceName)
        if pid == None:
            return True
        # 用subprocess杀进程
        try:
            retcode = subprocess.call("taskkill /PID {} /F".format(pid))
            print(retcode)
            if retcode == 0:
                # print('服务名：%s 关闭成功' % serviceName)
                myLogger.info('服务名：%s 关闭成功' % serviceName)
                return True
            return False
        except Exception as e:
            # print('服务名：%s 关闭失败'% serviceName)
            myLogger.info('服务名：%s 关闭失败' % serviceName)
            return False

    # 清空tomcat所有日志
    def clearLog(self,logs_path, serviceName):
        '''
            :param logs_path:
            :return:
        '''
        try:
            cmd_all = "rd /s/q logs "
            retcode = subprocess.call(cmd_all, shell=True, cwd=logs_path)
            if retcode == 0:
                # print('服务名：%s 清理日志成功' % serviceName)
                myLogger.info('服务名：%s 清理日志成功' % serviceName)
        except Exception as e:
            print(e)
            # print("服务名：%s 清理日志失败" % serviceName)
            myLogger.info("服务名：%s 清理日志失败" % serviceName)

    #测试接口调用
    # @encrypy_decrator('http://app.gsfybjy.com/phpatient/app/appservice?querystr=')
    def testUrl(self,url):
        print(url)
        try:
            request = requests.get(url,timeout=2)
            print(request.status_code)
            if request.status_code == 200:
                myLogger.info('接口调用成功：%s' %url)
                return True
            else:
                return False
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            myLogger.error('接口调用超时或连接异常--%s' % e)
            return False
        except Exception as e:
            myLogger.error('接口调用异常--%s' % e)
            return False