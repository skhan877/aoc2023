
def part_one(input_game): 
    """
    The Elf would first like to know which games would have been possible 
    if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
    """

    allowed = {'red': 12, 'green': 13, 'blue': 14}

    valid_games = set()

    for line in input_game:
        # print(line)
        game_id = line.split(":")[0].replace("Game ", "")
        # print(game_id)
        if game_id != "":
            valid_games.add(int(game_id))
        # print(valid_games)

        tosses = line.split(": ")[1]
        result = True
        for toss in tosses.split('; '):
            colours = [(col.split(' ')) for col in toss.split(', ') if len(col)]
            for colour in colours:
                check = {colour[1] : colour[0]}
                if int(colour[0]) > allowed[colour[1]]:
                    result = False 
                    try:
                        valid_games.remove(int(game_id))
                    except:
                        pass
                    break
        # print('')

    return sum(valid_games)


def part_two(input_game): 
    """
    For each game, find the minimum set of cubes that must have been present. 
    What is the sum of the power of these sets?
    """

    # max_cols = {'red': 1, 'green': 1, 'blue': 1}

    all_games = [line.split(": ")[1].split("; ") for line in input_game]

    for game in all_games:
        print(f"game: {game}")

        max_cols = {'red': 1, 'green': 1, 'blue': 1}
        cur_prod = 1
    
        for selection in game:
            print(f"selection: {selection}")
            print(f"selection split: {selection.split(', ')}")
            # colours = {col.split(" ")[1]: col.split(" ")[0] for col in t}
            # print(colours)
            # for colour in colours:
            #     # print(colour)
            #     ball_colour = colour[1].replace(",", "")
            #     ball_count = int(colour[0])
            #     # print(ball_colour, ball_count)
            #     if ball_count > max_cols[ball_colour]:
            #         cur_prod *= ball_count
            #         # print(f"yep, {ball_count} is greater than {max_cols[ball_colour]}")
        
                # print(max_cols)
        # print(cur_prod)
            # print(" ")

        print("-----------------------")
    # print("")
        # print(tosses)

    return -1 



def main(): 
    
    input_file = '..//inputs//two.txt'

    with open(input_file, 'r') as f:
        lines = [] 
        for line in f: 
            lines.append(line.rstrip('\n')) 
        lines = lines[:-1]
    
    
    sample = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
    # print(part_one(sample))
    print(part_two(sample))

    # print(part_one(lines))
    # print(part_two(lines))


if __name__ == "__main__": 
    main()