from logger import Logger
import subprocess
import psutil
import os
from base_util import utilBase

class nginxutil(utilBase):
    # 初始化
    def __init__(self,serviceName,nginxPath):
        utilBase.__init__(self)
        self.base_path = nginxPath
        self.ng_name = serviceName
        self.logger = Logger(logger="nginx").getlog()

    # 清理nginx日志
    def clearLog(self):
        if self.killNginx() == False:
            return
        cmd_all = "del /f/s/q *.log "
        # retcode = subprocess.call(cmd_all, shell=True, cwd=self.base_path+ '\\logs\\')
        with subprocess.Popen(cmd_all, stdout=subprocess.PIPE, shell=True, cwd=self.base_path+ '\\logs\\') as p:
            try:
                retcode = p.wait(timeout=None)
                stdout, stderr = p.communicate()
                if stdout.strip() != '':
                    self.logger.info(str(stdout, encoding='gbk'))
                if stderr is not None:
                    self.logger.info(str(stderr, encoding='gbk'))
                if retcode == 0:
                    self.logger.info('服务名：%s 日志清理完成' % self.ng_name)
            except Exception as e:
                self.logger.error('服务名：%s 日志清理异常' % self.ng_name)
                p.kill()
                p.wait()
            finally:
                # 重启nginx
                self.startNginx()

    # 用杀进程的方式停止服务
    def killNginx(self):
        try:
            isSucc = self.taskkillService(self.ng_name)
            if isSucc == True:
                self.logger.info('服务名：%s 关闭成功' % self.ng_name)
                return True
            self.logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False
        except Exception as e:
            self.logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False

    # 启动nginx
    def startNginx(self):
        try:
            isSucc = self.startService(self.ng_name)
            if isSucc == True:
                self.logger.info('服务名：%s 启动成功' % self.ng_name)
                return True
            self.logger.info('服务名：%s 启动失败' % self.ng_name)
            return False
        except Exception as e:
            self.logger.info('服务名：%s 启动失败' % self.ng_name)
            return False

    # 关闭nginx
    def stopNginx(self):
        # retcode = subprocess.call("nginx -s stop", shell=True, cwd=self.base_path)
        with subprocess.Popen("nginx -s stop", stdout=subprocess.PIPE, shell=True, cwd=self.base_path) as p:
            try:
                retcode = p.wait(timeout=None)
                stdout, stderr = p.communicate()
            except Exception as e:
                self.logger.info('服务名：%s 关闭失败' % self.ng_name)
                p.kill()
                p.wait()
                return False
            if stdout.strip() != '':
                self.logger.info(str(stdout, encoding='gbk'))
            if stderr is not None:
                self.logger.info(str(stderr, encoding='gbk'))
            if retcode == 0:
                self.logger.info('服务名：%s 关闭成功' % self.ng_name)
                return True
            self.logger.info('服务名：%s 关闭失败' % self.ng_name)
            return False