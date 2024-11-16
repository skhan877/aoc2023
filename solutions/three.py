def parse_input(input_data): 
    arr = []
    with open(input_data, "r") as f:
        for row in f:
            arr.append(row.rstrip('\n'))
    return arr  

def part_one(inputs):
    
    """
    look for numbers: not periods, is numeric, while loop? 
    look for symbols: not alpha, not numeric, not period
    """

    nums = [] 
    is_num = True
    i = j = 0

    for x in inputs:
        # while x[j].isnumeric():
        #     j += 1
        # nums.append(x[i:j])
        # i = j 
        # j += 1
        x = x.replace(".", "-")
        # x = x.split(" ")
        print(x)




def part_two(inputs):
    pass 


def main():
    
    input_data = "..//inputs//three.txt"
    input_array = parse_input(input_data)
    # return input_array

    sample_data = [
        "467..114.." ,
        "...*......" ,
        "..35..633." ,
        "......#..." ,
        "617*......" ,
        ".....+.58.",
        "..592....." ,
        "......755." ,
        "...$.*...." ,
        ".664.598.."]

    print(part_one(sample_data))

if __name__ == "__main__":
    main()
