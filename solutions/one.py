def solution(strng):

    finished = False
    p, q = 0, len(strng) - 1
    new_num = []

    while not finished:
        left = strng[p]
        
        if left.isalpha():
            # function to check string here, otherwise p+= 1
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

def solution_part_two(strng, nums_dict):

    for k, v in nums_dict.items():
        strng = strng.replace(k, str(v))

    return solution(strng)


def is_num_str(str, nums_dict):
    pass




# with open(input_file, 'r') as f:
#     lines = []
#     for line in f:
#         lines.append(line.rstrip('\n'))

# result = 0
# # for line in lines:
# for line in sample:
#     # result += solution_part_two(line)
#     print(solution_part_two(line))

# print(result) 

# eightwo ... replacing in order for dict, so two before eight. FIX THIS 

def main(): 

    input_file = '../inputs/one.txt'

    nums_dict = {
            'one' : 1,
            'two' : 2,
            'three' : 3,
            'four' : 4,
            'five' : 5,
            'six' : 6,
            'seven' : 7,
            'eight' : 8,
            'nine' : 9
        }

    sample = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

    for s in sample:
        print(s)
        for k, v in nums_dict.items():
            s = s.replace(k, str(v))
        print(s)
        print('')


if __name__ == '__main__':
    main() 