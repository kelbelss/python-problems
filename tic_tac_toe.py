print("\033[0;34m" "TIC-TAC-TOE" "\033[0;m")

grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]

O = ("\033[0;36m" "O" "\033[0;m") 
X = ("\033[0;35m" "X" "\033[0;m")

print("\033[0;36m" "User 1 is O" "\033[0;m")
print("\033[0;35m" "User 2 is X" "\033[0;m")

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])


def turns1(_grid):

    while True:
        user1 = input("\033[0;36m" "User 1: " "\033[0;m")
        place = int(user1) - 1
        if (_grid[place] != "X" and _grid[place] != "O"):
            O = ("\033[0;36m" "O" "\033[0;m") 
            _grid[place] = O
            return True
        

def turns2(_grid):
    while True:
        user2 = input("\033[0;35m" "User 2: " "\033[0;m")
        place = int(user2) - 1
        if (_grid[place] != "X" and _grid[place] != "O"):
            X = ("\033[0;35m" "X" "\033[0;m")
            _grid[place] = X
            return True
        

round = 0

while round <= 8:
   
    turns1(grid)
    round += 1

    print(grid[0], grid[1], grid[2])
    print(grid[3], grid[4], grid[5])
    print(grid[6], grid[7], grid[8])


    if (grid[0] == O and grid[1] == O and grid[2] == O) or (grid[0] == O and grid[3] == O and grid[6] == O) or (grid[0] == O and grid[4] == O and grid[8] == O) or (grid[1] == O and grid[4] == O and grid[7] == O) or (grid[2] == O and grid[5] == O and grid[8] == O) or (grid[2] == O and grid[4] == O and grid[6] == O) or (grid[3] == O and grid[4] == O and grid[5] == O) or (grid[6] == O and grid[7] == O and grid[8] == O):
        print("\033[0;32m" "Player 1 WINS" "\033[0;m")
        break

    if round == 9:
        break

    turns2(grid)
    round += 1

    print(grid[0], grid[1], grid[2])
    print(grid[3], grid[4], grid[5])
    print(grid[6], grid[7], grid[8])

    if (grid[0] == X and grid[1] == X and grid[2] == X) or (grid[0] == X and grid[3] == X and grid[6] == X) or (grid[0] == X and grid[4] == X and grid[8] == X) or (grid[1] == X and grid[4] == X and grid[7] == X) or (grid[2] == X and grid[5] == X and grid[8] == X) or (grid[2] == X and grid[4] == X and grid[6] == X) or (grid[3] == X and grid[4] == X and grid[5] == X) or (grid[6] == X and grid[7] == X and grid[8] == X):
        print("\033[0;32m" "Player 2 WINS" "\033[0;m")
        break




# TODO: 

# winner = 3 in a row (1, 2, 3) (1, 4, 7) (1, 5, 9) (2, 5, 8) (3, 6, 9) (3, 5, 7) (4, 5, 6) (7, 8, 9)
# no winner = no 3 in a row

# each player takes turns
# cannot play where other already has


# purple = "\033[0;35m"
# cyan = "\033[0;36m"
# blue = "\033[0;34m"
# back = "\033[0;m"