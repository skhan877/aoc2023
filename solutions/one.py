input_file = '../inputs/one.txt'

with open(input_file, 'r') as f:
    lines = []
    for line in f:
        lines.append(line.rstrip('\n'))

print(lines[:10])