def convert_char_to_int(char: str):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96

def main():
    file = open("input.txt", "r")
    priority_sum = 0
    badge_priority_sum = 0
    line_count = 0
    list_of_lines = []
    for line in file.readlines():

        l, r = line[:int((len(line)-1)//2)], line[int((len(line)-1)//2):]
        common = list(set(l) & set(r))
        priority_sum = priority_sum + sum([convert_char_to_int(char) for char in common])
        list_of_lines.append(line[:-1])
        line_count = line_count + 1
        if line_count == 3:
            badge_letter = list(set(list_of_lines[0]) & set(list_of_lines[1]) & set(list_of_lines[2]))
            print(badge_letter)
            badge_priority_sum = badge_priority_sum + sum([convert_char_to_int(char) for char in badge_letter])
            list_of_lines = []
            line_count = 0

        
    print(priority_sum)
    print(badge_priority_sum)


if __name__ == "__main__":
    main()