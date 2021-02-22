from time import time_ns


def m5(row):
    return map(lambda x: x * 5, row)


a = [int(s) for s in input().split()]
start_time = time_ns()

for _ in range(1000000):
    m5(a)

print((time_ns() - start_time) / 1000000)
print(a)
