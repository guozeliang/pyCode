import asyncio
import random
# import concurrent
from concurrent import futures
from pprint import pprint

async def coro(tag,index):
    print(">",tag)
    await asyncio.sleep(random.uniform(1,3))
    # if index == 8:
    #     raise Exception
    print("<",tag)
    return tag

loop = asyncio.get_event_loop()
'''
group1 = asyncio.gather(*[coro("group 1.{}".format(i),i) for i in range(1, 6)])
group2 = asyncio.gather(*[coro("group 2.{}".format(i),i) for i in range(1,4)])
group3 = asyncio.gather(*[coro("group 3.{}".format(i),i) for i in range(1,10)])
all_groups = asyncio.gather(group1,group2,group3,return_exceptions=True)
results = loop.run_until_complete(all_groups)
loop.close()
pprint(results)

'''

tasks = [coro(i,i) for i in range(1,11)]

print('get first result')
finished,unfinished = loop.run_until_complete(asyncio.wait(tasks,return_when=asyncio.FIRST_COMPLETED))
for task in finished:
    print(task.result())
    print('unfinised:',len(unfinished))

print('get more results in seconds')

finished2,unfinished2 = loop.run_until_complete(asyncio.wait(unfinished,timeout=1))
for task2 in finished2:
    print(task2.result())
    print("unfinised2",len(unfinished2))

print("Get all other results:")
finished3,unfinished3 = loop.run_until_complete(asyncio.wait(unfinished2))

for task in finished3:
    print(task.result())

loop.close()



