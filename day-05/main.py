def get_instructions(instruction: str) -> list[int]:
    instruction = instruction.replace("\n", "")
    split_result = instruction.split("from")
    to_result = split_result[1].split("to")
    qnt_to_move = split_result[0].replace("move", "").replace(" ", "")
    origin_pile = to_result[0].replace(" ", "")
    destination_pile = to_result[1].replace(" ", "")
    return [int(qnt_to_move), int(origin_pile), int(destination_pile)]

    

def main():
    file = open("input.txt", "r")
    pile_built = False
    piles_sorted = False
    piles = [[] for i in range(9)]

    for line in file.readlines():

        if not pile_built:
            if line[1] == "1":
                pile_built = True
                continue
            else:
                piles[0].append(line[1])
                piles[1].append(line[5])
                piles[2].append(line[9])
                piles[3].append(line[13])
                piles[4].append(line[17])
                piles[5].append(line[21])
                piles[6].append(line[25])
                piles[7].append(line[29])
                piles[8].append(line[33])
                continue
        if pile_built and not piles_sorted:
            piles = [piles[i][::-1] for i in range(9)]
            for pile in piles:
                if " " in pile:
                    while " " in pile:
                        pile.remove(" ")
            piles_sorted = True


        if(line.startswith("move")):
            move, origin, destination = get_instructions(line)
            i = 0
            piles[destination -1].extend(piles[origin-1][-move:])
            while i != move:
                # piles[destination -1].append(piles[origin-1].pop())
                piles[origin-1].pop()
                i += 1
    for pile in piles:
        print(pile[-1])
    return

if __name__ == "__main__":
    main()