print("TIC-TAC-TOE")

grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(grid[0], grid[1], grid[2])
# print(grid[3], grid[4], grid[5])
# print(grid[6], grid[7], grid[8])

# blocks = [[], [], [], [], [], [], [], [], []]

# print(blocks[0], blocks[1], blocks[2])
# print(blocks[3], blocks[4], blocks[5])
# print(blocks[6], blocks[7], blocks[8])

# user1 = 0
# user2 = X

def turns1(_grid):

    while True:
        user1 = input("User 1: ")
        place = int(user1) - 1
        if (_grid[place] != "X" and _grid[place] != "O"):
            _grid[place] = "O"
            return True
        

def turns2(_grid):
    while True:
        user2 = input("User 2: ")
        place = int(user2) - 1
        if (_grid[place] != "X" and _grid[place] != "O"):
            _grid[place] = "X"
            return True
        


round = 0

while round <= 8:
   
    turns1(grid)
    round += 1

    print(grid[0], grid[1], grid[2])
    print(grid[3], grid[4], grid[5])
    print(grid[6], grid[7], grid[8])

    if round == 9:
        break

    turns2(grid)
    round += 1

    print(grid[0], grid[1], grid[2])
    print(grid[3], grid[4], grid[5])
    print(grid[6], grid[7], grid[8])







# TODO: 

# winner = 3 in a row (1, 2, 3) (1, 4, 7) (1, 5, 9) (2, 5, 8) (3, 6, 9) (3, 5, 7) (4, 5, 6) (7, 8, 9)
# no winner = no 3 in a row

# each player takes turns
# cannot play where other already has


