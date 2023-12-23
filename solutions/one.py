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


def is_num_str(strng, nums_dict, reversed=False):
    
    if not reversed:
        print('running front to back. string is now: '+ strng)
        for char in list(strng):
            for k, v in nums_dict.items():
                if char == k[0]:
                    # print(char, k)
                    new_strng = strng.replace(k, str(v))
                    if new_strng != strng: # replacement successful
                        print(f'success! old: {strng}, new: {new_strng}. Now reverse it.')
                        is_num_str(new_strng, nums_dict, reversed=True)
            break
        # break
                    # print(strng)
                    # print('')
    
    else: 
        print('running back to front. string is now: '+ strng)
        for char in list(strng)[::-1]:
            for k, v in nums_dict.items():
                if char == k[-1]:
                    # print(char, k)
                    new_strng = strng.replace(k, str(v))
                    print('---- doing reverse stuff -----')
                    print(f'checking {char}, trying {k} because of {k[-1]}, old: {strng}, new: {new_strng}')
                    print('---------------------')
                    if new_strng != strng: # replacement successful
                        break
            break
                    # print(strng)
                    # print('')


    return new_strng


def main(): 

    input_file = '../inputs/one.txt'

    with open(input_file, 'r') as f:
        lines = []
        for line in f:
            lines.append(line.rstrip('\n'))
    
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
    
    sample = ['two4oneight', 'two1nine']#,'eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

    
    result = 0
    for line in sample: #lines:
        print(f'original read of line: {line}')
        converted_line = is_num_str(line, nums_dict)
        # result += solution(converted_line)
        print(converted_line)
        print(f'num to be summed: {solution(converted_line)}')
        print('')

    print(result) 



if __name__ == '__main__':
    main() 