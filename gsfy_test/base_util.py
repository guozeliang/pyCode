import psutil

class utilBase(object):
    # 获取pid
    @classmethod
    def processinfo(cls, processName):
        try:
            service = psutil.win_service_get(processName)
            return service.as_dict()['pid']
        except psutil.NoSuchProcess as e:
            # myLogger.info('没有找到服务名为：%s 的进程PID' % processName)
            return None
