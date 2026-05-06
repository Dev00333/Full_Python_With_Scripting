# an armstrong is a number whose digits to the power of total number of digits in the numbers sum is equal to the number itself
from math import *
def check(a):
    if (a==0):
        return True
    s=0
    c=a
    power=len(str(c))
    while(a>0):
        ld=a%10
        a=a//10
        s=s+(ld ** power)
    return c==s

a=int(input("enter teh number to check for armstorng check:"))
while(a<0):
    print("enter a valid number.")
    a=int(input("enter a positive number:"))
print(f"the number {a} status for palindrome is {check(a)}")