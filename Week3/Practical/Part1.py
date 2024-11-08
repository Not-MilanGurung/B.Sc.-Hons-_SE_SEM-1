import timeit
start_time = timeit.default_timer()

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    res = []
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            res += [p]
    return res

print(SieveOfEratosthenes(1_000))
print(timeit.default_timer()- start_time)

start_time = timeit.default_timer()

def prime(n):
    a = []
    for x in range(2,n+1):
        for y in a:
            if x%y == 0:
                break
        else:
            a+=[x]
    return a

print(prime(1_000))
print(timeit.default_timer()- start_time)