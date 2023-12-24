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


def is_num_str(strng, nums_dict):
    
    # for char in list(strng):
    for k, v in nums_dict.items():
        strng = strng.replace(k, v)
    return strng

    # finished = False
    # reversed = False
    # new_strngs = []

    # while not reversed:
    #     for char in list(strng):
    #         for k, v in nums_dict.items():
    #             if char == k[0]:
    #                 new_strng = strng.replace(k, str(v))
    #                 if new_strng != strng: # replacement successful
    #                     new_strngs.append(new_strng)
    #                     reversed = True 
    #                     break
    #         if reversed:
    #             break
    #     break

    # if len(new_strngs) == 0:
    #     new_strng = strng 

    # while not finished:
    #     for char in list(new_strng)[::-1]:
    #         for k, v in nums_dict.items():
    #             if char == k[-1]:
    #                 new_new_strng = new_strng.replace(k, str(v))
    #                 if new_new_strng != new_strng: # replacement successful
    #                     new_strngs.append(new_new_strng)
    #                     finished = True
    #                     break
    #         if finished:
    #             break
    #     break

    # return new_strngs[-1] if len(new_strngs) > 0 else strng


def main(): 

    input_file = '../inputs/one.txt'

    with open(input_file, 'r') as f:
        lines = []
        for line in f:
            lines.append(line.rstrip('\n'))
    
    nums_dict = {
            'one' : 'o1e',
            'two' : 't2o',
            'three' : 'th3ee',
            'four' : 'fo4r',
            'five' : 'fi5ve',
            'six' : 'si6x',
            'seven' : 'se7en',
            'eight' : 'ei8ght',
            'nine' : 'ni9ne'
        }
    
    sample = ['sndk8', '1111', 'eightwothree', 'eightwo', 'two1nine','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

    
    result = 0
    for line in sample:
        print(f'original line: {line}')
        converted_line = is_num_str(line, nums_dict)
        print(f'converted line: {converted_line}')
        # result += solution(converted_line)
        # print(f'num to be summed: {solution(converted_line)}')
        print('')

    # print(result) 



if __name__ == '__main__':
    main() 