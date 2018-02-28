
# def lazy_range(up_to):
#     index = 0
#     def gratuitous_refactor():
#         while index < up_to:
#             yield index
#             index +=1
#     yield from gratuitous_refactor()

def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()

gen = lazy_range(10)
gen.send(None)
print(gen.send(2))
# print(next(gen))

'''
def htest():
    i = 1
    while i < 4:
        n = yield i
        if i == 3:
            return 100
        i += 1

def itest():
    val = yield from htest()
    print(val)

t = itest()
t.send(None)
j = 0
while j < 3:
    j += 1
    try:
        t.send(j)
    except StopIteration as e:
        print('异常了')

'''


