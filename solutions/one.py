input_file = '../inputs/one.txt'

with open(input_file, 'r') as f:
    lines = []
    for line in f:
        lines.append(line.rstrip('\n'))

# print(lines[:10])

strng = lines[0]

finished = False
p, q = 0, len(strng) - 1
sum = 0
nums = 0

# while p < q:
#     left, right = strng[p], strng[q]
    
#     if left.isalpha():
#         p += 1
#     else:
#         sum += left 
#         nums += 1

#     if right.isalpha(): 
#         q -= 1
#     else:
#         sum += right
#         nums += 1
