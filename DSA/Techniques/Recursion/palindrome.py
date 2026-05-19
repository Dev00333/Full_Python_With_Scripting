# approach 1 recursion
def pal(s,start,end):
    if start>=end: return True
    if s[start]!=s[end]: return False
    return pal(s, start+1, end-1)


# approach 2 recursion (head recursion)
def head_pal(a):
    if len(a)==0:
        return True
    if a[0]!=a[-1]:
        return False
    return head_pal(a[1:-1])

# approach 3 iteration
def palindrome(a):
    l=len(a)
    left=0
    right=l-1
    while left<=right:
        if a[left]!=a[right]:
            return False
        left+=1
        right-=1
    return True

a=input("enter the string:")
print(f"original string: {a}")
print(f"the statement that given starting {a} is palindrome is {pal(a,0,len(a)-1)}")