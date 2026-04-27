import csv
with open('file_handeling/csv_files/sorted.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)