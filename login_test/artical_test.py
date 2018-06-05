import requests
import gevent
from gevent import monkey
from aes_tool import aes_tool
# monkey.patch_all()
# @encrypy_decrator('http://app.gsfybjy.com/phpatient/app/appservice?querystr=')
def reqServer(url):
    tmpUrl = 'http://app.gsfybjy.com/phpatient/app/appservice?querystr='
    enStr = aes_tool.encrypy('/app/phpatientmain/login?aUserName=17737166928&aPassword=E10ADC3949BA59ABBE56E057F20F883E&aVersionNo=1.2.625&aClientType=0')
    print("{}{}".format(tmpUrl,enStr))
    # 开始请求
    response = requests.get("{}{}".format(tmpUrl,enStr))
    try:
        if response.status_code == 200:
            print(response.text)
            print('success')
    except Exception as e:
        print(e)
        print(response.text)

def queryArtical():
    list = []  ## 空列表
    for x in range[0,10]:
        url = "/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435"
        list.append(gevent.spawn(reqServer(),url))
    gevent.joinall(list)

if __name__ == '__main__':
    # queryArtical()
    reqServer('/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435')



