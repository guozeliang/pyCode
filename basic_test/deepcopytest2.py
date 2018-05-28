import copy

'''
will = ['will',28,['python','C#','javascript']]
wilber = will #对象的赋值

print(id(will))
print(will)
print([id(ele) for ele in will])
print(id(wilber))
print(wilber)
print([id(ele) for ele in wilber])

will[0] = 'wilber'
will[2].append('CSS')

print(id(will))
print(will)
print([id(ele) for ele in will])
print(id(wilber))
print(wilber)
print([id(ele) for ele in wilber])

'''
#浅拷贝

will = ['will',28,['python','C#','javaScript']]
wilber = copy.copy(will)

print(id(will))
print(will)
print([id(ele) for ele in will])
print(id(wilber))
print(wilber)
print([id(ele) for ele in wilber])

will[0] = 'wilber'
will[2].append("CSS")
print(id(will))
print(will)
print([id(ele) for ele in will])
print(id(wilber))
print(wilber)
print([id(ele) for ele in wilber])









