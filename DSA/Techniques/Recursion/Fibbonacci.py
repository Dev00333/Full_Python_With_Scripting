# # Fibbonacci series using recursion
# def fibo(a):
#     if a==0: return 0
#     if a==1: return 1
#     return  fibo(a-1)+fibo(a-2)

# fibbonacci series using iteration
def fibo_itr(a):
    if a==0: return 0
    if a==1: return 1
    b=1
    c=1
    for i in range(2,a):
        d=b+c
        b=c
        c=d
    return c

while True:
    try:
        a=int(input("enter the term: "))
        # print(f"the {a}th term in fibbonacci series is {fibo(a)}")
        print(f"the {a}th term in fibbonacci series is {fibo_itr(a)}")
        break
    except ValueError:
        print("enter a valid term")