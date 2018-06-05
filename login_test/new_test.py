from gevent import monkey; monkey.patch_all()
import gevent,requests
import time
from aes_tool import aes_tool
count = 0

def f(url):
    data = requests.get(url)
    if data.status_code == 200:
        print("one")


start = time.time()
url_list = []
endUrl = '/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435'

for i in range(1000):
    enStr = 'http://app.gsfybjy.com/phpatient/app/appservice?querystr=' + aes_tool.encrypy(endUrl).decode('utf-8')
    url_list.append(gevent.spawn(f,enStr))
print(enStr)
gevent.joinall(url_list)
print (time.time() - start)
print('---------end----------')