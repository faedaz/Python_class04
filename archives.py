import csv

path_file: str = "example.csv"

file_csv: list = []

with open(file=path_file, mode="r", encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    
    for row in csv_reader:
        file_csv.append(row)
print(file_csv)