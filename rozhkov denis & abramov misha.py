import time 
a = [ int(input()) for i in range(10)]
start_time1 = time.time()
b = [i * 5 for i in a]
print(b)
print(round(time.time() - start_time1,8), "Прошло Секунд")