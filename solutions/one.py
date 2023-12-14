input_file = '../inputs/one.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()
f.close()

print(len(lines))
