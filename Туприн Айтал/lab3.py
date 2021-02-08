from array import array
import timeit
from random import randint
from time import time_ns


def check_time_t(f, k):
    r = range(1, k)
    start_t = time_ns()
    for i in r:
        f()

    return (time_ns() - start_t) / (k * 1000)


def check_time_tit(f):
    return timeit.timeit(f, number=1000000)


def m5_10_map(a):
    return map(lambda x: x * 5, a)


def m5_10_gen(a):
    return [s * 5 for s in a]


def m5_10_map_listed(a):
    return list(map(lambda x: x * 5, a))


print('All in MS')

row = [randint(-100000, 1000000) for _ in range(10)]

print(f"TIMEIT, MAP FUNCTION: {check_time_tit(lambda: m5_10_map(row))}")
print(f"TIMEIT, GEN FUNCTION: {check_time_tit(lambda: m5_10_gen(row))}")
print(f"TIMEIT, LISTED MAP FUNCTION: {check_time_tit(lambda: m5_10_map_listed(row))}")

print(f"TIME_NS, MAP FUNCTION: {check_time_t(lambda: m5_10_map(row), 1000000)}")
print(f"TIME_NS, GEN FUNCTION: {check_time_t(lambda: m5_10_gen(row), 1000000)}")
print(f"TIME_NS, LISTED MAP FUNCTION: {check_time_t(lambda: m5_10_map_listed(row), 1000000)}")
print(row, '\n')


row = array('i', row)

print(f"TIMEIT, MAP FUNCTION: {check_time_tit(lambda: m5_10_map(row))}")
print(f"TIMEIT, GEN FUNCTION: {check_time_tit(lambda: m5_10_gen(row))}")
print(f"TIMEIT, LISTED MAP FUNCTION: {check_time_tit(lambda: m5_10_map_listed(row))}")

print(f"TIME_NS, MAP FUNCTION: {check_time_t(lambda: m5_10_map(row), 1000000)}")
print(f"TIME_NS, GEN FUNCTION: {check_time_t(lambda: m5_10_gen(row), 1000000)}")
print(f"TIME_NS, LISTED MAP FUNCTION: {check_time_t(lambda: m5_10_map_listed(row), 1000000)}")
print(row)
