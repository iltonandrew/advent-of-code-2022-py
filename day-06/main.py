def main():
    file = open("input.txt", "r")
    char_list = []
    char_count = 0
    for line in file.readlines():
        for char in line:
            char_count += 1
            if char not in char_list:
                char_list.append(char)
                print(char_list)
            else:
                char_list = char_list[char_list.index(char)+1:]
                char_list.append(char)
            if len(set(char_list)) == 14:
                print(char_list)
                print(char_count)
                break
            
    print(char_count)

    return

if __name__ == "__main__":
    main()