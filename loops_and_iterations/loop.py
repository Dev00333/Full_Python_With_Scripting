a = [1,2,3,4,5]
for num in a:
    for alp in 'abcde':
        print(num, alp)
        # this is a nested loop, the inner loop will run completely for each iteration of the outer loop

b= a[4]
while b < 10:
    print(b)
    b += 1
    # this is a while loop, it will continue to run until the condition is no longer true