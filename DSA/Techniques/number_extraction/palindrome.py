# a palindrome is a number that is same even when read from forward or backward

# this code handles all the numbers either positive or nagative and checks for the palindrome eitherways but in output it keeps the sign and tell weather palindrome or not
def reverse(a):
    rev=0
    while(a>0):
        ld=a%10
        rev=rev*10+ld
        a=a//10
    print(rev)
    return rev

def palindrome(a):
    return reverse(a)==a

c=int(input("enter a number for palindrome check:"))
if(c<0):
    print(f"the given number {c} is negative but after doing absoulute operation the paindrome state is {palindrome(abs(c))}")
else:
    print(f"the given number {c} palindrome case is {palindrome(c)}")