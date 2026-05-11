import math
a=int(input("enter a number for prime factorisation:"))

# approach 1 this is the brute force approach to find prime factors
# this approach is not efficient for large numbers 
def brute_force(a):
    c=[]
    i=2
    while(i<=a):
        while(a%i==0):
            c.append(i)
            a=a//i
        i+=1
    print(f"brute force: the prime factors of the given number is {c}")

# approach 2 this is the optimised approach to find prime factors
# this approach is efficient for large numbers
def optimized(b):
    results=[]
    while b%2==0:
        results.append(2)
        b=b//2
    i=3
    while i*i<=b:
        while b%i==0:
            results.append(i)
            b=b//i
        i+=2
    if(b>1):
        results.append(b)
    print(f"optimized: the prime factors of the given number is {results}")

# brute_force(a)
# approach 3 their are also other optimized approaches like pollard's rho algorithm and trial division algorithm that can handle digits more than 24 to 50 digits easily
optimized(a)