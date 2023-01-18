import random

def random_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return random.choice(lines)

file_path = 'dk01.txt'
print(' \ ',' \n',  random_line(file_path), '/ ')
