#异步IO例子：适配Python3.4，使用asyncio库
import asyncio
# import threading
import requests
from AES_DECR import encrypy_decrator
from aes_tool import aes_tool
import aiohttp

# 异步IO例子：适配Python3.5，使用async和await关键字
# @encrypy_decrator('http://app.gsfybjy.com/phpatient/app/appservice?querystr=')
# async def hello(url):       # 通过关键字async定义协程
#     await requests.get(url) as resp:
#         print(url, resp.status_code)
#         print('666666666666')

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

@asyncio.coroutine
def print_page(url):
    response = yield from aiohttp.request('GET', url)
    body = yield from response.read_and_close(decode=True)
    print(body)

if __name__ == "__main__":
        tasks = []
        url = '/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435'
        for i in range(0, 3):
            enStr = 'http://app.gsfybjy.com/phpatient/app/appservice?querystr=' + aes_tool.encrypy(url).decode('utf-8')
            print(enStr)
            tasks.append(print_page(url))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()


















