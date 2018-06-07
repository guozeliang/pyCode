
from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex

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
    endUrl = '/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435'
    enStr = aes_tool.encrypy(endUrl)
    print(enStr)
    '''解密'''
    deStr = aes_tool.decrypt(enStr).decode('utf-8')
    print(deStr)


# app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435


