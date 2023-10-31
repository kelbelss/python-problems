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
    for i in range(0,8):
        if i != "X" or i != "0":
            _grid[chosenGridBlockIndex] = "0"
        


def turns2(_grid):
    for i in range(0,8):
        if i != "X" or _grid != "0":
            _grid[chosenGridBlockIndex] = "X"


# def takeTurns():




user1 = input("User 1: ")
chosenGridBlockIndex = int(user1) - 1

turns1(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])

user2 = input("User 2: ")
chosenGridBlockIndex = int(user2) - 1

turns2(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])

user1 = input("User 1: ")
chosenGridBlockIndex = int(user1) - 1

turns1(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])

user2 = input("User 2: ")
chosenGridBlockIndex = int(user2) - 1

turns2(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])

user1 = input("User 1: ")
chosenGridBlockIndex = int(user1) - 1

turns1(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])

user2 = input("User 2: ")
chosenGridBlockIndex = int(user2) - 1

turns2(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])

user1 = input("User 1: ")
chosenGridBlockIndex = int(user1) - 1

turns1(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])

user2 = input("User 2: ")
chosenGridBlockIndex = int(user2) - 1

turns2(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])

user1 = input("User 1: ")
chosenGridBlockIndex = int(user1) - 1

turns1(grid)

print(grid[0], grid[1], grid[2])
print(grid[3], grid[4], grid[5])
print(grid[6], grid[7], grid[8])






# TODO: 

# winner = 3 in a row (1, 2, 3) (1, 4, 7) (1, 5, 9) (2, 5, 8) (3, 6, 9) (3, 5, 7) (4, 5, 6) (7, 8, 9)
# no winner = no 3 in a row

# each player takes turns
# cannot play where other already has


