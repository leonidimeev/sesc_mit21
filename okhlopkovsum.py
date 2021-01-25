n = int(input('Введите натуральное n = '))
s = 0
p = 0
i = 1
while i <= n:
    s = s + i
    i = i + 1
print('Сумма чисел до n =',s)
f = 1
while n > 1:
    f = f * n
    n -= 1
print('Произведение чисел до n =',f)
    
