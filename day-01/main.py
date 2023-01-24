import os

def main():
    calories_list = []
    elven_calories = 0
    file = open("input.txt", "r")
    for line in file.readlines():
        if line == "\n":
            calories_list.append(elven_calories)
            elven_calories = 0
        else:
            elven_calories = int(line) + elven_calories
        
    calories_list.sort()
    print("First Answer: " + str(calories_list[-1]))
    
    print("Second Answer: " + str(sum(calories_list[-3:])))


if __name__ == "__main__":
    main()