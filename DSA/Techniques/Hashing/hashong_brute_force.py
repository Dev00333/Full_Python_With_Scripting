import random
# n=random.sample(range(1,11),6)
# m=[random.randint(1,10) for i in range(101)]
# # while len(n)!=6:
# #     a=random.randint(1,10)
# #     if a not in n:
# #         n.append(a)
# # for num in range(1,101):
# #     b=random.randint(1,10)
# #     m.append(b)       this is the old way
# # creating the list of 100 random numbers between 1 to 10
# # present_keys={}
# # for number in n:
# #     present_keys[number]=0
# # for number in m:
# #     if number in present_keys:
# #         present_keys[number]+=1
# # print(f"Present keys: {present_keys}")          #this is the older meathod to generate the frequency of each element in the list

# frequency = {key:0 for key in n}
# for num in m:
#     if num in frequency:
#         frequency[num]+=1
# print(f"Frequency: {frequency}")
# a=int(input("enter a number to be searched in the list:"))
# if a in frequency:
#     print(f"The number {a} is present in the list and its frequency is {frequency[a]}")
# else:
#     print(f"The number {a} is not present in the list")

# character hashing now
while True:
    user_input = input("Enter the length of the string: ")
    try:
        length = int(user_input)
        if length >= 1:
            break
        else:
            print("Error: Length must be 1 or greater.")
    except ValueError:
        print("Error: Please enter a valid whole number.")
def string_gen(length):
    return "".join(chr(random.randint(97, 122)) for _ in range(length))
x=[0]*26
ch = string_gen(length)
print(f"Generated string: {ch}")
for i in range(length):
    x[ord(ch[i])-97]+=1
print(f"Frequency: {x}")
freq=input("enter the character whose frequency you want to find:")
while len(freq)!=1 or ord(freq)>122 or ord(freq)<97:
    freq=input("enter the correct character:")
print(f"the frequency for {freq} is {x[ord(freq)-97]}")


g=['a','f','r','u','a','d','u','j','k','l','p','q','o','i','u']
illist={}
for i in range (len(g)):
    illist[g[i]]=x[ord(g[i])-97]
print(illist)