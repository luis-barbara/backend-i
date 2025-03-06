# Create a generator that reads lines from a large text file 
# (simulate with a list of strings), uses enumerate to show line numbers, 
# strips whitespace, and filters out empty lines.


file_name = 'example.txt'

texto = "Este é um texto repetido várias vezes para criar um arquivo grande.\n"

with open(file_name, 'w') as file:
    for i in range(100000):  
        file.write(texto)


with open('example.txt', 'r') as file:
    count = sum(1 for line in file)

    print(f"O número total de linhas é: {count}")


def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            stripped_line = line.strip()  
            if stripped_line:  
                yield line_number, stripped_line

for line_number, line in read_large_file(file_name):
    print(f"Line {line_number}: {line}")