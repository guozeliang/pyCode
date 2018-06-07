import psutil

class utilBase(object):
    # 通过服务名获取pid
    def processinfo(self, processName):
        try:
            service = psutil.win_service_get(processName)
            return service.as_dict()['pid']
        except psutil.NoSuchProcess as e:
            # myLogger.info('没有找到服务名为：%s 的进程PID' % processName)
            return None
