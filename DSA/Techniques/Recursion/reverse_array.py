def reverse_arr(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_arr(arr, start + 1, end - 1)

a=input("enter the array:")
b=list(a)
print("original array:",b)
reverse_arr(b, 0, len(b) - 1)
print("reversed array:",b)


def head_rev(a):
    if len(a)==0:
        return
    head_rev(a[1:])
    print(a[0],end="")

head_rev(a)