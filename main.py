import numpy as np

start = 3
stop = 3

def mersenne(a=0, b=8, c=1):
    mrange = 2 ** np.arange(a, b, c, dtype=object) - 1
    print(mrange)
    return mrange

def prime(num):
    for d in range(2, num):
        if num % d == 0:
            return False
    return True

def check(numbers):
    print(2)
    for n in numbers:
        if prime(n):
            print(n)
        print('Checked '+str(n))

check(mersenne(a=16, b=31, c=1))
