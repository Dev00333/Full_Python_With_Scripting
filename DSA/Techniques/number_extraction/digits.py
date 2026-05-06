from math import *
count=0
# normal count approach where the complexity is determined bt the loop 

def countDigits(a):
    while(a>0):
        global count
        a=a//10     # the // operation gets the floor of the number so that the decimal part is dropped
        count+=1
    print(count)

# in the standard count approach the TC is O(log10(n)) here the 10 decides the number of loops that we will run we can change it to 2 3 or any number depending upon the digit extraction we need accoring to the number system we are working on and n is the number we are working on


# this is the logarithmic approach that calculates the complexity directly

def logCountDigit(a):
    print(int(log10(a))+1)

# in the logarithmic approach we take the TC directly using the math module and using the log approach to determine which number system we are using we can choose the base accordingly here we did 10 for decimal but we can also do others as well like log2(a) here a is the number we will perform the operation on and to get the total number digits only we use this THIS MEATHOD DOES NOT EXTRACT THE DIGITS WE CAN ADD d=a%10 IN COUNT MEATHOD TO EXTRACT THE DIGITS 
# in this approach the TC is always O(1)


# outputs
b=int(input("enter a number: "))
countDigits(b)
logCountDigit(b)