import sys
'''元组比较大小 可以以次来作版本号的比较
    
'''
tuple1 = (1,2,3,4)

tuple2 = (1,1,6,7,8)

print(sys.version_info)

if sys.version_info >= (3,):
    print("大于3")

if tuple1 < tuple2:
    print('1大于2')

class IntTuple(tuple):
    testNo = 1
    def __new__(cls, seq):
        g = (x for x in seq if isinstance(x,int))
        return super(IntTuple,cls).__new__(cls,g)

    def __init__(self,seq):
        print('self:{},seq:{}'.format(self,seq))
        super(IntTuple,self).__init__()
    @classmethod
    def get_no_of_instance(cls):
        return cls.testNo

t = IntTuple((1,-1,'a'))

print(t)
print(t.get_no_of_instance())

class IntTuple1(IntTuple):
    def __init__(self,seq):
        print('tuple')

t1 = IntTuple1((1,2,'a'))
print(t1.__dict__)
print(t1.get_no_of_instance())

class test(object):
    clsvar = 1
    def __init__(self):
        self.insvar = 2

ins1 = test()
ins2 = test()

ins1.clsvar = 20

print(test.clsvar)
print(ins1.clsvar)
print(ins2.clsvar)






























