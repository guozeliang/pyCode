import requests
import json
from pdbc_conn import oracleCon
import gevent
from gevent import monkey
monkey.patch_all()
from AES_DECR import encrypyDec
import random

def getUserInfo():
    # connect oracle database
    orclcnn = oracleCon('phpatient/phpatient@172.16.10.81:1521/apptest')
    #获取数据
    sql = "select a.username,a.password from (select t.username,t.password from t_member t order by username)a where rownum<=1000 order by rownum DESC "
    # sql = "select t.username,t.password from t_member t where t.username != '17737166928'"
    data = orclcnn.queryData(sql)
    return data

# @encrypyDec
def reqServer(url):
    # url = "http://172.16.40.193:8888/phpatient/app/phpatientmain/login?aUserName="+ userName+"&aPassword=" + password+ "&aVersionNo=1.2.625&aClientType=0"
    # url = 'http://1.85.3.154:13003/phpatient/app/appservice?querystr='
    # print(url)
    # 开始请求
    response = requests.get(url)
    try:
        tmpData = json.loads(response.text)
        print('----'+tmpData['data']['memLoginInfo']['username']+'----')
    except Exception as e:
        print(e)
        print(response.text)

# @encrypyDec
def reqServerByUserName(userName,password,version,clientType):
    url = "http://172.16.10.45:80/phpatient/app/phpatientmain/login?aUserName="+ userName+"&aPassword=" + password+ "&aVersionNo="+version+"&aClientType="+str(clientType)
    # url = "http://172.16.10.67:7777/phpatient/app/phpatientmain/login?aUserName="+ userName+"&aPassword=" + password+ "&aVersionNo=1.2.625&aClientType=0"
    print(url)
    # 开始请求
    response = requests.get(url)
    try:
        tmpData = json.loads(response.text)
        # print(tmpData)
        tmpPhone = tmpData['data']['memLoginInfo']['username']
        # print('前台传入：' + userName + '----' + '后台返回：' + tmpPhone + '---手机类型：' + str(clientType) + '---版本号：' + version )
        if tmpPhone != userName:
            print('前台传入：'+userName +'----'+ '后台返回：'+tmpPhone+'---手机类型：'+str(clientType) +'---版本号：'+version)
    except Exception as e:
        print(e)
        print(response.text)

if __name__ == '__main__':
    # 获取用户信息
    data = getUserInfo()

    list = []     ## 空列表
    '''
    for i, x in enumerate(data):
        # url = "http://172.16.10.45:80/phpatient/app/phpatientmain/login?aUserName=" + x[0] + "&aPassword=" + x[
        #     1] + "&aVersionNo=1.2.625&aClientType=0"
        # reqServer(url)
        reqServerByUserName(x[0],x[1])
    
    for x in data:
        url = "http://172.16.10.45:80/phpatient/app/phpatientmain/login?aUserName="+ x[0]+"&aPassword=" + x[1]+ "&aVersionNo=1.2.625&aClientType=0"
        # list.append(gevent.spawn(reqServer,url))
        list.append(gevent.spawn(reqServerByUserName,x[0]))
    gevent.joinall(list)
    '''
    for x in data:
        i = random.randint(0, 100)
        if i%2 == 0:
            clientType = 0
            version = '1.2.625'
        else:
            clientType = 1
            version = '1.1.293'
        # print('%s--%s--%s--%s'% (x[0],x[1],version,clientType))
        list.append(gevent.spawn(reqServerByUserName,x[0],x[1],version,clientType))
    gevent.joinall(list)




