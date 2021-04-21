start = 3
stop = 100000

def prime(num):
    for d in range(2, num):
        if num % d == 0:
            return False
    return True

print(2)
for n in range(start, stop, 2):
    if prime(n):
        print(n)
