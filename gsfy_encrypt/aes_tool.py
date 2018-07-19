
from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex
import sys

class aes_tool(object):
    # def __init__(self,aKey='36AAF0685AEF14641F1F54CC853B6323',aIv='5AEF14641F1F54CC'):
    #     key = aKey
    #     iv = aIv

    key = '36AAF0685AEF14641F1F54CC853B6323'
    iv = '5AEF14641F1F54CC'

    @classmethod
    def encrypy1(cls, message):
        aes = AES.new(cls.key, AES.MODE_CBC, cls.iv)
        return base64.b64encode(aes.encrypt(message))
    # 加密
    @classmethod
    def encrypy(cls,message):
        aes = AES.new(cls.key,AES.MODE_CBC,cls.iv)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 32
        count = len(message)
        if count < length:
            add = length - count
            message = message + ('\6' * add)
        elif count > length:
            add = (length - (count % length))
            message = message + ('\6' * add)
        # cls.ciphertext = aes.encrypt(message)
        return base64.b64encode(aes.encrypt(message))

    # 解密
    @classmethod
    def decrypt(cls,encrypted):
        aes = AES.new(cls.key, AES.MODE_CBC, cls.iv)
        return aes.decrypt(base64.b64decode(encrypted))

# aClientType=0\x06\x06\x06\x06\x06\x06
# aClientType=0\x00\x00\x00\x00\x00\x00
if __name__ == '__main__':
    '''加密'''
    deptUrl = '/app/member/appointment/apt_dept_scheduler.html?deptCode=2055&auplatform=wechat'
    enStr = aes_tool.encrypy(deptUrl)
    print(enStr)
    '''解密'''
    deStr = aes_tool.decrypt('H8P3JKfE0xZQ6AMhL/RyobiR8Itm5cBkzLet4qiL/liJ+p7x6UkkhiZLJ8ErCx+xqTRBJqE/k1pgqWply/A7QGxp/g7FWiHemAqZkrJMMEKQktQ2hSsbsU1eTnDz/Vsa')
    print(deStr)

    f = open(r'dept_code.txt')
    lines = f.readlines()
    for line in lines:
        # print(line.strip())
        tmpDeptUrl =  '/app/member/appointment/apt_dept_scheduler.html?deptCode='+ line.strip()+ '&auplatform=wechat'
        # print(tmpDeptUrl)
        tmpEnStr = 'http://app.gsfybjy.com/phpatient/app/appservice?querystr='+ aes_tool.encrypy(tmpDeptUrl).decode('utf-8')
        print("%s  %s" %(line.strip(),tmpEnStr))



