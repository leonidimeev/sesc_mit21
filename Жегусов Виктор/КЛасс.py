#from array import array
#Массив
#A = array('1', [2,4,5,3,5,6,7,6,5,4,3,4,5,6,7,7,6,5,4,3,4,5,6,,5,6,4,3,4,5,6,7]))
#print(A)
#a1 = reduce(lambda x: x*5, b1)
#Список
#B = [2,4,4,6,6,6,4,7,3,6,8,7,5,4,5,7,8,6,5,4,3,5,6,7,8,9,9,7,6,5,5]
from functools import reduce
from array import array
from time import time

a, b, c, d, e, f, g, h, i, j = map(int, input().split())

starttime = time()

b1 = [a,b,c,d,e,f,g,h,i,j]

for i in range(10):
    b1[i] *= 5


print(b1)
print(time() - starttime)

starttime = time()
b1 = [a,b,c,d,e,f,g,h,i,j]
b2 = array("i", b1)

for i in range(10):
    b2[i] *= 5

print(b2)
print(time() - starttime)

