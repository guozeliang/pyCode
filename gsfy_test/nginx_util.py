from logger import Logger
# import base_util
import subprocess
import psutil
import os

logger = Logger(logger="nginx").getlog()

class nginxutil(object):

    def __init__(self,serviceName,nginxPath):
        self.base_path = nginxPath
        self.ng_name = serviceName

    # 获取pid
    @classmethod
    def processinfo(cls, processName):
        try:
            service = psutil.win_service_get(processName)
            return service.as_dict()['pid']
        except psutil.NoSuchProcess as e:
            logger.info('没有找到服务名为：%s 的进程PID' % processName)
            return None

    # 清理nginx日志
    def clearLog(self):
        if self.stopNginx2() == False:
            return
        cmd_all = "del /f/s/q *.log "
        print(self.base_path+ '\\logs\\')
        try:
            retcode = subprocess.call(cmd_all, shell=True, cwd=self.base_path+ '\\logs\\')
            # 注意 如果启动失败 怎样处理
            self.startNginx()
        except Exception as e:
            print(e)
    # 关闭nginx
    def stopNginx(self):
        pid = self.processinfo(self.ng_name)
        if pid == None:
            return True
        # 用subprocess杀进程
        try:
            retcode = subprocess.call("taskkill /PID {} /F".format(pid))
            print(retcode)
            if retcode == 0:
                logger.info('服务名：%s 关闭成功' % self.ng_name)
                return True
            return False
        except Exception as e:
            logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False
    # 启动nginx
    def startNginx(self):
        call_cmd = "net start " + self.ng_name
        try:
            retcode = subprocess.call(call_cmd)
            if retcode == 0:
                logger.info('服务名：%s 启动成功' % self.ng_name)
                return True
            return False
        except Exception as e:
            logger.info('服务名：%s 启动失败' % self.ng_name)
            return False

    # 关闭nginx
    def stopNginx2(self):
        retcode1 = subprocess.call("nginx -s stop", shell=True, cwd=self.base_path)

    # 关闭nginx
    def stopNginx2(self):
        call_cmd = "net stop " + self.ng_name
        pid = self.processinfo(self.ng_name)
        if pid == None:
            return True
        # 用subprocess杀进程
        try:
            retcode = subprocess.call(call_cmd)
            if retcode == 0:
                logger.info('服务名：%s 关闭成功' % self.ng_name)
                return True
            return False
        except Exception as e:
            logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False

    # def checkNginx(self):
