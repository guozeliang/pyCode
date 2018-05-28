'''
asyncio学习
1、协程的定义---aysnc def 或 @coroutine   判断 是否是协程函数可以用 asyncio.iscoroutinefunction()来验证
2、await / yield from 可以等待一个协程。
3、协程的运行：
    调用协程函数返回协程对象 可以通过asyncio.iscoroutine来验证
    asyncio.ensure_future()生成futures
    asyncio.gather与asyncio.wait的区别。
4、回调  添加future对象上
    futu.add_done_callback(dosome())

'''