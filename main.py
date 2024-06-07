import math

with open('students.txt', 'r') as file:
    info = file.read()

students_dict = dict()

lines = info.strip().split('\n')

for line in lines:
    parts = line.split()
    name = parts[0]
    scores = list(map(int, parts[1:]))
    students_dict[name] = scores

with open('output.txt', 'w') as file:
    file.write(f'Average scores: \n')
    for name, score in students_dict.items():
        file.write(f'{name}: {math.floor(sum(score) / len(score))}\n')
