from logger import Logger
import subprocess
import psutil
import os
from base_util import utilBase

logger = Logger(logger="nginx").getlog()

class nginxutil(utilBase):
    # 初始化
    def __init__(self,serviceName,nginxPath):
        utilBase.__init__(self)
        self.base_path = nginxPath
        self.ng_name = serviceName

    # 清理nginx日志
    def clearLog(self):
        if self.killNginx() == False:
            return
        cmd_all = "del /f/s/q *.log "
        try:
            retcode = subprocess.call(cmd_all, shell=True, cwd=self.base_path+ '\\logs\\')
            if retcode == 0:
                logger.info('服务名：%s 日志清理完成' % self.ng_name)
            else:
                logger.info('服务名：%s 日志清理失败' % self.ng_name)
        except Exception as e:
            print(e)
        finally:
            # 重启nginx
            self.startNginx()

    # 用杀进程的方式停止服务
    def killNginx(self):
        try:
            isSucc = self.taskkillService(self.ng_name)
            if isSucc == True:
                logger.info('服务名：%s 关闭成功' % self.ng_name)
                return True
            logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False
        except Exception as e:
            logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False

    # 启动nginx
    def startNginx(self):
        try:
            isSucc = self.startService(self.ng_name)
            if isSucc == True:
                logger.info('服务名：%s 启动成功' % self.ng_name)
                return True
            logger.info('服务名：%s 启动失败' % self.ng_name)
            return False
        except Exception as e:
            logger.info('服务名：%s 启动失败' % self.ng_name)
            return False

    # 关闭nginx
    def stopNginx(self):
        try:
            retcode = subprocess.call("nginx -s stop", shell=True, cwd=self.base_path)
            if retcode == 0:
                logger.info('服务名：%s 关闭成功' % self.ng_name)
                return True
            logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False
        except Exception as e:
            logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False
