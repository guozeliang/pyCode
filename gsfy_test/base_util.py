import psutil
import subprocess
from logger import Logger

logger = Logger(logger="utilBase").getlog()

class utilBase(object):

    # def __init__(self):
    #     self.logger = Logger(logger="utilBase").getlog()

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
        with subprocess.Popen(call_cmd,stdout=subprocess.PIPE) as p:
            try:
                retcode = p.wait(timeout=None)
                stdout,stderr = p.communicate()
                if stdout.strip() != '':
                    logger.info(str(stdout, encoding='gbk'))
                if stderr is not None:
                    logger.info(str(stderr, encoding='gbk'))
            except:
                p.kill()
                p.wait()
                raise
        if retcode == 0:
            return True
        return False

    # 用服务名方式启动
    def stopService(self, serviceName):
        call_cmd = "net stop " + serviceName
        pid = self.processinfo(serviceName)
        if pid == None:
            return True
        with subprocess.Popen(call_cmd,stdout=subprocess.PIPE) as p:
            try:
                retcode = p.wait(timeout=None)
                stdout,stderr = p.communicate()
                if stdout.strip() != '':
                    logger.info(str(stdout, encoding='gbk'))
                if stderr is not None:
                    logger.info(str(stderr, encoding='gbk'))
            except:
                p.kill()
                p.wait()
                raise
            if retcode == 0:
                return True
            return False

    # 发杀进程的方式停止服务
    def taskkillService(self,serviceName):
        pid = self.processinfo(serviceName)
        if pid == None:
            return True
        call_cmd = "taskkill /PID {} /F /T".format(pid)
        # 用subprocess杀进程
        with subprocess.Popen(call_cmd,stdout=subprocess.PIPE) as p:
            try:
                retcode = p.wait(timeout=None)
                stdout,stderr = p.communicate()
                if stdout.strip() != '':
                    logger.info(str(stdout, encoding='gbk'))
                if stderr is not None:
                    logger.info(str(stderr, encoding='gbk'))
            except:
                p.kill()
                p.wait()
                raise
            if retcode == 0:
                return True
            return False

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
    # b'\xb3\xc9\xb9\xa6: \xd2\xd1\xd6\xd5\xd6\xb9 PID 5364 (\xca\xf4\xd3\xda PID 5592 \xd7\xd3\xbd\xf8\xb3\xcc)\xb5\xc4\xbd\xf8\xb3\xcc\xa1\xa3\r\n\xb3\xc9\xb9\xa6: \xd2\xd1\xd6\xd5\xd6\xb9 PID 5592 (\xca\xf4\xd3\xda PID 7044 \xd7\xd3\xbd\xf8\xb3\xcc)\xb5\xc4\xbd\xf8\xb3\xcc\xa1\xa3\r\n\xb3\xc9\xb9\xa6: \xd2\xd1\xd6\xd5\xd6\xb9 PID 7044 (\xca\xf4\xd3\xda PID 3292 \xd7\xd3\xbd\xf8\xb3\xcc)\xb5\xc4\xbd\xf8\xb3\xcc\xa1\xa3\r\n\xb3\xc9\xb9\xa6: \xd2\xd1\xd6\xd5\xd6\xb9 PID 3292 (\xca\xf4\xd3\xda PID 740 \xd7\xd3\xbd\xf8\xb3\xcc)\xb5\xc4\xbd\xf8\xb3\xcc\xa1\xa3\r\n'
    # bytestr = b'Nginx Service \xb7\xfe\xce\xf1\xd5\xfd\xd4\xda\xc6\xf4\xb6\xaf .\r\nNginx Service \xb7\xfe\xce\xf1\xd2\xd1\xbe\xad\xc6\xf4\xb6\xaf\xb3\xc9\xb9\xa6\xa1\xa3\r\n\r\n'
    # print(str(bytestr,encoding='gbk'))

    tutilBase = utilBase()
    tutilBase.findTasks('nginx.exe')