
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

if __name__ == '__main__':
    # @encrypyDec
    @encrypy_decrator('http://1.85.3.154:13003/phpatient/app/appservice?querystr=')
    def foo(x):
        print('***')

    foo('111111111111111111111111111111')
