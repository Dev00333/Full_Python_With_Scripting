# standard approach to find factorial of a number using recursion
def fact(n):
    if n==0 or n==1: return 1
    return n*fact(n-1)
print(fact(5))
print(fact.__name__.lower())

# tail recursion approach to find the factorial
def fact_tail(n, acc=1):
    if n==0 or n==1: return acc
    return fact_tail(n-1, acc*n)
print(fact_tail(5))
print(fact_tail.__name__.lower())

# head recursion approach to find the factorial
def fact_head(n):
    if n==0 or n==1: return 1
    result = fact_head(n-1)
    return n*result
print(fact_head(5))
print(fact_head.__name__.lower())