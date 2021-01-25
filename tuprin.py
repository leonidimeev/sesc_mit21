from functools import reduce

a = [int(s) for s in input().split()]

print(sum(a))
print(reduce(lambda x, y: x * y, a))