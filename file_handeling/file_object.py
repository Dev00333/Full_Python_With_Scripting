f = open('random_data.txt', 'r') # this will create a new file called random_data.txt in the current directory and open it in read mode
print(f) # this will print the file object
print(f.mode) # this will print the name of the file
f.close() # this will close the file object
# this above way is not recommended because if we forget to close the file then it will cause memory leak and other issues so we use the with statement to handle the file object which will automatically close the file after we are done with it the with statement is also known as context manager in python


with open('random_data.txt', 'r') as f: # this will open the file in read mode and assign it to the variable f
    f_contetnts = f.readline() # this will read the contents of the file and assign it to the variable f_contents
    # print(f_contetnts) # this will print the contents of the file
    # for line in f: # this will iterate through the lines of the file and print them
    #     print(line)
    # print(f.read(100)) # if we run this again it will start from where it left off and read the next 100 characters of the file
    size_to_read = 100
    while len(f_contetnts) > 0: # this will keep reading the file until it reaches the end of the file
        print(f_contetnts, end='****') # this will print the contents of the file without adding a new line after each line
        f_contetnts = f.read(size_to_read) # this line makes sure that their is no infinite loop and only 100 characters are read at a time
    print(f.tell()) # this will tell us the current position of the file pointer in the file
    f.seek(0) # this will move the file pointer to the beginning of the file using this seek we can change to any location in file
    print(f.tell()) # this will tell us the current position of the file pointer in the file
    
with open('random_data2.txt', 'a') as w: # this will open the file in append mode and assign it to the variable w
    pass # this will do nothing and just move on to the next line of code
    # w.write('\n') # this will add a new line after the line we just wrote
    # w.write('this is a new line') # this will write a new line to the file
    # w.write('\n') # this will add a new line after the line we just wrote
    # w.write('this is another line') # this will append another line to the file