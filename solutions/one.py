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


def is_num_str(strng, nums_dict):
    
    for k, v in nums_dict.items():
        strng = strng.replace(k, v)
    return strng



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
    
    # sample = ['eightwothree', 'two1nine','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

    result = 0
    for line in lines:
        converted_line = is_num_str(line, nums_dict)
        result += solution(converted_line)

    print(result) 



if __name__ == '__main__':
    main() 