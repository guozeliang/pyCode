
from aes_tool import aes_tool

def encrypyDec(func):
    ''' 加密装饰器 '''
    def wrapper(*args,**kwargs):
        enStr = 'http://app.gsfybjy.com/phpatient/app/appservice?querystr='+ aes_tool.encrypy(args[0]).decode('utf-8')
        args = (enStr,)
        return func(*args,**kwargs)
    return wrapper

def encrypyDecByTwo(func):
    ''' 加密装饰器 '''
    def wrapper(*args,**kwargs):
        print(args)
        enStr = aes_tool.encrypy(args[2]).decode('utf-8')
        args = (args[0],args[1],enStr,)
        return func(*args,**kwargs)
    return wrapper

def encrypy_decrator(*dargs, **dkargs):
     def wrapper(func):
         def _wrapper(*args, **kargs):
             # print(dargs[0])
             # print(args[1])
             enStr = dargs[0] + aes_tool.encrypy(args[1]).decode('utf-8')
             # print(enStr)
             args = (enStr,)
             return func(*args, **kargs)
         return _wrapper
     return wrapper

if __name__ == '__main__':
    '''
    http://app.gsfybjy.com/phpatient/app/appservice?querystr=
    '''
    # @encrypyDec
    @encrypy_decrator('http://app.gsfybjy.com/phpatient/app/appservice?querystr=')
    def foo(x):
        print('***')

    foo('/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435')
