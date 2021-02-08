from array import array
from time import time
def mir (a):
    for i in range(10):
        a[i] *= 5
a, b, c, d, e, f, g, h, i, j = map(int, input().split())
starttime = time()
b1 = [a, b, c, d, e, f, g, h, i, j]
mir(b1)

print(b1)
print(time() - starttime)
starttime = time()
b1 = [a, b, c, d, e, f, g, h, i, j]
b2 = array("i",b1)
mir (b2)
print(b2)
print(time() - starttime)