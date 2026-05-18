# sum to n 
def func(sum, n):
    if n==1: return sum+1
    return func(sum+n, n-1)
a=int(input('enter a number: '))
print(func(0,a))