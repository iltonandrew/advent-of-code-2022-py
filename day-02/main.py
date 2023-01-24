map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
map_win = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
map_lose = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}


def main():
    plan_A_result = 0
    plan_B_result = 0
    
    file = open("input.txt", "r")
    for line in file.readlines():
        opponent_shape = map_input[line[0]]
        our_shape = map_input[line[2]]
        if opponent_shape == our_shape:
            plan_A_result = plan_A_result + points_per_outcome['Draw'] + points_per_shape[our_shape]
        elif (opponent_shape, our_shape) in [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]:
            plan_A_result = plan_A_result + points_per_outcome['Lose'] + points_per_shape[our_shape]
        else :
            plan_A_result = plan_A_result + points_per_outcome['Win'] + points_per_shape[our_shape]
   
   
    file = open("input.txt", "r")
    for line in file.readlines():
        our_input = line[2]
        if our_input == "X":
            plan_B_result = plan_B_result + points_per_outcome['Lose'] + points_per_shape[map_win[map_input[line[0]]]]
        elif our_input == "Y":
            plan_B_result = plan_B_result + points_per_outcome['Draw'] + points_per_shape[map_input[line[0]]]
        else:
            plan_B_result = plan_B_result + points_per_outcome['Win'] + points_per_shape[map_lose[map_input[line[0]]]]


    print("First Answer: " + str(plan_A_result))
    print("Second Answer: " + str(plan_B_result))

    





if __name__ == "__main__":
    main()