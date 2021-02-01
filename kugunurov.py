n = int(input("n: "))
res = 0
for i in range(1,n+1):
    res+=i
print("The sum of N nums: "+str(res))
res = 1
for z in range(1,n+1):
    res*=z
print("The multiply of N nums: "+str(res))