from gevent import monkey; monkey.patch_all()
import gevent,requests
import time
from logger import Logger

myLogger = Logger(logger="request").getlog()

def f(url):
    # myLogger.info(url)
    data = requests.get(url)
    if data.status_code == 200:
        # myLogger.info("success")
        pass
    else:
        myLogger.info("fail")


# for i in range(10):
#     enStr = 'http://222.74.64.14:80/phpatient/app/introduce/hospital?hospitalId=106413A77D104A9A8F9E701D0AD50D1F'
#     url_list.append(gevent.spawn(f,enStr))
# myLogger.info(enStr)
# gevent.joinall(url_list)
# myLogger.info(time.time() - start)
# myLogger.info('---------end----------')

if __name__ == '__main__':
    for i in range(100):
        start = time.time()
        url_list = []
        for i in range(1000):
            enStr = 'http://222.74.64.14:80/phpatient/app/introduce/hospital?hospitalId=106413A77D104A9A8F9E701D0AD50D1F'
            url_list.append(gevent.spawn(f, enStr))
        gevent.joinall(url_list)
        myLogger.info(time.time() - start)
        myLogger.info('---------end----------')
