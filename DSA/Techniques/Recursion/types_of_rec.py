# their are 5 types of recursion that i know of namely

# Direct Recursion

def dir_rec(n_fact):
    if n_fact==0: return 1
    return n_fact*dir_rec(n_fact-1)


# indirect recursion

def is_even(n):
    if n==0: return True
    return is_odd(n-1)

def is_odd(n):
    if n==0: return False
    return is_even(n-1)


# tail recursion this recursion is also known as backtracking
# in this recursion we take a function variable that stores all the values moving from up to down

def tail_rec(n_fact, acc):
    if n_fact==0: return acc*1
    return tail_rec(n_fact-1, acc*n_fact)


# head recursion
# in this recursion we recurse firse then we do all the calculations so the order of result is reversed

def head_rec(user_data):
    a=len(user_data)
    result =[]
    head_rec_helper(user_data,a, result)
    return result

def head_rec_helper(n, l, result):
    if l==0: return
    head_rec_helper(n[1:],l-1, result)
    result.append(n[0])


# tree recursion
# in this recursion we parse the recursion using a b-tree structure

def fibo(n):
    if n==1: return 1
    if n==0: return 0
    return fibo(n-1)+fibo(n-2)

print(dir_rec(5))
print(is_even(4))
print(tail_rec(5,1))
print(head_rec('lola'))
print(fibo(4))