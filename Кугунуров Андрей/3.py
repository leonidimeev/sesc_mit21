from array import array
import time 
start_time1 = time.time()
start_time2 = time.time()
n = int(input())
massiv = [0]*n
for i in range(n):
    massiv[i] = int(input())
# массив
A = array('i', massiv)

# список
B = massiv



for i in range(len(A)):
    A[i] *= 5

for i in range(len(B)):
    B[i] *= 5
print(A, time.time() - start_time1)
print(B, time.time() - start_time2)
