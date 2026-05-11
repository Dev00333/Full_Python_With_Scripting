import random
n=[]
m=[]
for num in range(1,10):
    n.append(random.randint(1,10))
for num in range(1,101):
    m.append(random.randint(1,10))
present_keys={}
for num in n:
    count=0
    for x in m:
        if num==x:
            count+=1
    present_keys[num]=count
print(f"Present keys: {present_keys}")

a=int(input("enter a number to be searched in the list:"))
if a in present_keys:
    print(f"The number {a} is present in the list and its frequency is {present_keys[a]}")
else:
    print(f"The number {a} is not present in the list")