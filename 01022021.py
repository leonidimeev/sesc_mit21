


from array import array
# массив
A = array('i', [2,4,4,5,7,2,4,1,5,7,2,3,1,2,0,123,13,1,2,3,1,3,13,2,31,23,1,31,2,1,1])

# список
B = [2,4,4,5,7,2,4,1,5,7,2,3,1,2,0,123,13,1,2,3,1,3,13,2,31,23,1,31,2,1,1]

import time 
start_time1 = time.time()
flag = False
while True:
	flag = False
	for i in range(14):
		if (A[i] > A[i+1]):
			temp = A[i]
			A[i] = A[i+1]
			A[i+1] = temp
			flag = True
	if (flag == False):
		break
print(time.time() - start_time1)
start_time2 = time.time()
flag = False
while True:
	flag = False
	for i in range(14):
		if (B[i] > B[i+1]):
			temp = B[i]
			B[i] = B[i+1]
			B[i+1] = temp
			flag = True
	if (flag == False):
		break
print(time.time() - start_time2)

C = [5,'j','j',True]
D = [i for i in range(10)]

C.append('k')
C.remove('j')
C.extend(D)



                                     






















