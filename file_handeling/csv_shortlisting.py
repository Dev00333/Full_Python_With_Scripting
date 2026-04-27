import os
os.chdir('./file_handeling')
print(os.getcwd())
csv_counter = 0
with open ('./csv_files/sorted.csv', 'w')as output_file:
    for file in os.listdir('csv_files'):
        if file.endswith('.csv') and (file != 'sorted.csv') and (csv_counter<1):
            csv_counter += 1
            with open(os.path.join('csv_files', file), 'r') as input_file:
                lines = input_file.readlines()
                for line in lines[0:50]:
                    cols = line.strip().split(',')
                    if len(cols)>=6:
                        filtered_line = f"{cols[0]},{cols[2]},{cols[3]},{cols[5]}\n"
                        output_file.write(filtered_line)