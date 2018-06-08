from gevent import monkey; monkey.patch_all()
import gevent,requests
import time
from aes_tool import aes_tool
from logger import Logger

myLogger = Logger(logger="request").getlog()

def f(url):
    data = requests.get(url)
    if data.status_code == 200:
        myLogger.info("success")


start = time.time()
url_list = []
endUrl = '/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435'

for i in range(1000):
    enStr = 'http://app.gsfybjy.com/phpatient/app/appservice?querystr=' + aes_tool.encrypy(endUrl).decode('utf-8')
    url_list.append(gevent.spawn(f,enStr))
myLogger.info(enStr)
gevent.joinall(url_list)
myLogger.info(time.time() - start)
myLogger.info('---------end----------')