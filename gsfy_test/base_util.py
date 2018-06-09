import psutil
import subprocess
from logger import Logger

logger = Logger(logger="utilBase").getlog()

class utilBase(object):
    # 通过服务名获取pid
    def processinfo(self, processName):
        try:
            service = psutil.win_service_get(processName)
            return service.as_dict()['pid']
        except psutil.NoSuchProcess as e:
            logger.info('没有找到服务名为：%s 的进程PID' % processName)
            return None

    # 用服务名方式启动
    def startService(self,serviceName):
        call_cmd = "net start " + serviceName
        try:
            retcode = subprocess.call(call_cmd)
            if retcode == 0:
                return True
            return False
        except Exception as e:
            raise e

    # 用服务名方式启动
    def stopService(self, serviceName):
        call_cmd = "net stop " + serviceName
        pid = self.processinfo(serviceName)
        if pid == None:
            return True
        try:
            retcode = subprocess.call(call_cmd)
            if retcode == 0:
                return True
            return False
        except Exception as e:
            raise e

    # 发杀进程的方式停止服务
    def taskkillService(self,serviceName):
        pid = self.processinfo(serviceName)
        if pid == None:
            return True
        # 用subprocess杀进程
        try:
            retcode = subprocess.call("taskkill /PID {} /F /T".format(pid))
            print(retcode)
            if retcode == 0:
                return True
            return False
        except Exception as e:
            raise e
    #获取任务列表
    def findTasks(self,taskName):
        pidlist = []
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
                if pinfo['name'] == taskName:
                    pidlist.append(pinfo['pid'])
            except psutil.NoSuchProcess:
                pass
        return pidlist

if __name__ == '__main__':
    tutilBase = utilBase()
    tutilBase.findTasks('nginx.exe')