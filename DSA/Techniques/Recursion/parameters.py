def func(x,n):
    if n==0: return
    print(x)
    func(x+1,n-1)
func(1,5)