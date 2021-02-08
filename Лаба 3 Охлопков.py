from array import array
import time
start_time1 = time.time()
start_time2 = time.time()
N = int(input())
M = [0]*N
print(M)
for i in range(N):
    M[i] = int(input())
A = array('i', M)
for i in range(len(M)):
    A[i]*=5
    M[i]*=5
print(A, time.time() - start_time1)
print(M, time.time() - start_time2)
    

    

