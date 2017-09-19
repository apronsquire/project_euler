def problem_3():
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# 1. find all the factors
# 2. check all the factors for being prime
# 3. determine largest prime factor
    import math
    n = 600851475143
    i = 2
    j = 2
    # using square root because prime factor can't be greater
    while i < math.sqrt(n):
        if n % i == 0:
            for j in range(2,i):
                if i% j == 0:
                    print j
                next
        i = i+1

problem_3()
