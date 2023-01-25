def get_numbers_in_range(start, end):
    numbers = []
    for number in range(start, end + 1):
        numbers.append(number)
    return numbers

def main():
    file = open("input.txt", "r")
    fully_overlaps = 0
    intersects = 0
    for line in file.readlines():
        elves_numbers=line.replace("\n", "").split(",")
        elf_one_numbers = get_numbers_in_range(int(elves_numbers[0].split("-")[0]), int(elves_numbers[0].split("-")[1]))
        elf_two_numbers = get_numbers_in_range(int(elves_numbers[1].split("-")[0]), int(elves_numbers[1].split("-")[1]))
        if set(elf_one_numbers).issubset(set(elf_two_numbers)) or set(elf_two_numbers).issubset(set(elf_one_numbers)):
            fully_overlaps += 1
        if len(set(elf_one_numbers).intersection(set(elf_two_numbers))) > 0:
            intersects += 1
        
    print("First Answer:", fully_overlaps)
    print("Second Answer:", intersects)

if __name__ == "__main__":
    main()