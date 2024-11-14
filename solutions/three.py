def parse_input(input_data): 
    arr = []
    with open(input_data, "r") as f:
        for row in f:
            arr.append(row.rstrip('\n'))
    return arr  

def part_one(input_game):
    pass 


def part_two(input_game):
    pass 


def main():
    
    input_data = "..//inputs//three.txt"
    input_array = parse_input(input_data)
    return input_array, len(input_array)


if __name__ == "__main__":
    print(main())
