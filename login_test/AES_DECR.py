
from aes_tool import aes_tool

def encrypyDec(func):
    ''' 加密装饰器 '''
    def wrapper(*args,**kwargs):
        print(args[0])
        enStr = 'http://1.85.3.154:13003/phpatient/app/appservice?querystr='+ aes_tool.encrypy(args[0]).decode('utf-8')
        print(aes_tool.encrypy(args[0]).decode('utf-8'))
        print(enStr)
        args = (enStr,)
        return func(*args,**kwargs)
    return wrapper

def encrypy_decrator(*dargs, **dkargs):
     def wrapper(func):
         def _wrapper(*args, **kargs):
             print(args[0])
             enStr = dargs[0] + aes_tool.encrypy(args[0]).decode('utf-8')
             print(aes_tool.encrypy(args[0]).decode('utf-8'))
             print(enStr)
             args = (enStr,)
             return func(*args, **kargs)
         return _wrapper
     return wrapper

@encrypy_decrator('http://app.gsfybjy.com/phpatient/app/appservice?querystr=')
def foo(x):
    # 开始请求
    response = requests.get(x)
    try:
        if response.status_code == 200:
            print(response.text)
            print('success')
    except Exception as e:
        print(e)
        print(response.text)
    print('***')

if __name__ == '__main__':
    # @encrypyDec
    foo('/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435')
