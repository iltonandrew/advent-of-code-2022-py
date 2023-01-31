def main():
    path_stack = []
    dir_size_map = {}
    file = open("input.txt", "r")
    less_than_100000_sum = 0
    for line in file.readlines():
        if line.startswith("$ ls") or line.startswith("dir"):
            continue
        line=line.replace("\n", "")
        line = line.split(" ")

        if line[1] == "cd":
            if line[2] == "..":
                path_stack.pop()
            else:
                path_stack.append("_".join(path_stack) + "_" + line[2] if path_stack else line[2])
        else:
            for path in path_stack:
                if path in dir_size_map.keys():
                    dir_size_map[path] += int(line[0])
                else:
                    dir_size_map[path] = int(line[0])
    print("Answer one: ",sum(n for n in dir_size_map.values() if n <= 100_000))

    total_disk_space = dir_size_map["/"]
    space_needed = (total_disk_space + 30000000 - 70000000)
    for value in sorted(dir_size_map.values()):
        if value >= space_needed:
            print("Answer two: ", value)
            break
    return

if __name__ == "__main__":
    main()