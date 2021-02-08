# n = int(input("n: "))
# res = 0
# for i in range(1,n+1):
#     res+=i
# print("The sum of N nums: "+str(res))
# res = 1
# for z in range(1,n+1):
#     res*=z
# print("The multiply of N nums: "+str(res))
from array import array
A = array('i', [2,2,4,5,4,3,1,1,6,4,5,8,4,6])
B = [2,6,8,2,1,5,1,2,3,1,2,7,4,3]
import time
start_time = time.time()
flag = False
while True:
    flag = True
    for i in range(13):
        if A[i] > A[i+1]:
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
            flag = False
    if flag == True:
        break
print(A)
print(time.time()-start_time)
