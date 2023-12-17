input_file = '../inputs/one.txt'

def solution(strng):

    finished = False
    p, q = 0, len(strng) - 1
    new_num = []

    while not finished:
        left = strng[p]
        
        if left.isalpha():
            p += 1
        else:
            new_num.append(left)
            finished = True 

    finished = False 
    while not finished:
        right = strng[q]

        if right.isalpha(): 
            q -= 1
        else:
            new_num.append(right)
            finished = True

    new_num = int(''.join(new_num))
    return new_num 

with open(input_file, 'r') as f:
    lines = []
    for line in f:
        lines.append(line.rstrip('\n'))

result = 0
for line in lines:
    result += solution(line)

print(result) 