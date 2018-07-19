from gevent import monkey; monkey.patch_all()
import gevent,requests
import time
from aes_tool import aes_tool
from logger import Logger

myLogger = Logger(logger="testApi").getlog()

class testApi(object):
    url_list = []
    def requestUrl(self,url):
        data = requests.get(url)
        if data.status_code == 200:
            myLogger.info("success")

    def startTest(self,endUrl):
        for i in range(1000):
            enStr = 'http://app.gsfybjy.com/phpatient/app/appservice?querystr=' + aes_tool.encrypy(endUrl).decode(
                'utf-8')
            self.url_list.append(gevent.spawn(self.requestUrl, enStr))
        myLogger.info(enStr)
        gevent.joinall(self.url_list)