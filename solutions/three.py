def parse_input(input_data): 
    arr = []
    with open(input_data, "r") as f:
        for row in f:
            arr.append(row.rstrip('\n'))
    return arr  

def part_one(inputs):
    pass 


def part_two(inputs):
    pass 


def main():
    
    input_data = "..//inputs//three.txt"
    input_array = parse_input(input_data)
    # return input_array

    sample_data = ["467..114.. " +
        "...*......" + 
        "..35..633." +
        "......#..." +
        "17*......" +
        ".....+.58." +
        "..592....." +
        "......755." +
        "...$.*...." +
        ".664.598.."]

    print(sample_data)

if __name__ == "__main__":
    main()
