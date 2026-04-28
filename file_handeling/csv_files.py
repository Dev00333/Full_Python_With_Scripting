import csv
with open('file_handeling/csv_files/sorted.csv', 'r') as fx:
    csv_reader = csv.reader(fx)   # this line reads the csv fils first and give the line by line to the writer so that the mistake of adding delimiter after evert letter is avoided so that is why we use the reader before writing anything in the new file before: a-t-l-a-s after using this reader the response is normal as nn-atlas-xxxx-68685 so the delimiter is used properly 
    with open('file_handeling/csv_files/sorted1.csv', 'w') as output:
        writer = csv.writer(output, delimiter='\t') # this line is used to write the data in the new file and the delimiter is used to separate the data in the new file by tab space instead of comma
        for line in csv_reader:
            writer.writerow(line) # if we run this without the reader then output will be segemnted after each and every letter and confusing

# with open('file_handeling/csv_files/sorted1.csv', 'r') as fy:
#     reader = csv.reader(fy, delimiter='\t') # if we do not use a delimiter here then the output will have the \t instead of space as nn\tatlas\txxxx\t69875 so to avoid this we use the delimiter in the reader 
#     for line in reader:
#         print(line)
with open('file_handeling/csv_files/sorted1.csv', 'r') as fz:
    csv_reader = csv.DictReader(fz, delimiter='\t') # this line is used to read the csv file and give the data in the form of dictionary so that we can access the data by using the key instead of index
    with open('file_handeling/csv_files/sorted_dict.csv', 'w') as new_file:
        fieldnames = ['index', 'first_name', 'last_name', 'email'] # we have to make sure that the fieldnames we enter matches the fieldnames that are already present on tyhe orignal .csv file or else their will not be any result
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
with open('file_handeling/csv_files/sorted_dict.csv', 'r') as f1: # here f1 is the file we are using as input
    csv_reader = csv.DictReader(f1, delimiter='\t')
    with open('file_handeling/csv_files/sorted_removed.csv', 'w') as f2: #here f2 is alias for the output file we want
        fieldnames = ['index', 'first_name', 'last_name']
        csv_writer = csv.DictWriter(f2, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)