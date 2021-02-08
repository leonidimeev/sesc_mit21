import time 
from array import array
inb = [ int(input()) for i in range(10)]
start_time = time.time()
a=inb
a = [i * 5 for i in a]
print(a)
start_time1 = time.time()
b=array("i",inb)
for i in range(10):
    b[i]*=5
print(b)
print(float(time.time() - start_time), "Прошло Секунд")
print(float(time.time() - start_time1), "Прошло Секунд")
