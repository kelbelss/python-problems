import random
import os, time

print("⚔️ BATTLE TIME -> CHARACTERS⚔️")

print()
time.sleep(2)


def roll(sides):
  result = random.randint(1, sides)
  return result


def health():
  health = round((roll(6) * roll(8)) / 2) + 10
  print("HEALTH: ", health)
  return health


def strength():
  strength = round((roll(6) * roll(8)) / 2) + 12
  print("STRENGTH: ", strength)
  return strength


# character1():
name1 = input("Name your Legend: ")
type1 = input("Character Type (Human, Elf, Wizard, Orc): ")
time.sleep(1)
print()
print("Player 1: ", name1, "the", type1)
healthOne = health()
strengthOne = strength()
  
time.sleep(4)
os.system("clear")
print("Who are they battling? ")
print()

# character2():
name2 = input("Name your Legend: ")
type2 = input("Character Type (Human, Elf, Wizard, Orc): ")
time.sleep(1)
print()
print("Player 2: ", name2, "the", type2)
healthTwo = health()
strengthTwo = strength()
  
time.sleep(4)
os.system("clear")


round = 1
winner = None

print("The Battle Begins!")
print()

time.sleep(2)
os.system("clear")

while True:
  
  print("Round:", round)
  print()
  print("Starting Health:")
  print()
  print(name1, "has", healthOne, "health")
  print(name2, "has", healthTwo, "health")
  print()

  time.sleep(4)
  os.system("clear")

  print("⚔️ BATTLE TIME ⚔️")
  print()
  
  dice1 = roll(6)
  dice2 = roll(6)
  print(name1, "rolled", dice1)
  print(name2, "rolled", dice2)
  
  time.sleep(4)
  print()

  difference = abs(strengthOne - strengthTwo) + 1
  
  if dice1 > dice2:
    healthTwo -= difference
    if round == 1:
      print(name1, "wins the first round")
    else:
      print(name1, "wins round", round)
  elif dice2 > dice1:
    healthOne -= difference
    if round == 1:
      print(name2, "wins the first round")
    else:
      print(name2, "wins round", round)
  else:
    print("It's a draw!")


  print()
  time.sleep(4)

  print(name1, "has", healthOne, "health")
  print(name2, "has", healthTwo, "health")
  print()
  
  time.sleep(4)

  if healthOne <= 0:
    print(name1, "has died")
    winner = name2
    break
  elif healthTwo <= 0:
    print(name2, "has died")
    winner = name1
    break
  else:
    print("Both still standing! Next round...")
    round += 1
    time.sleep(4)
    os.system("clear")
  
  time.sleep(4)

time.sleep(4)
os.system("clear")

print("⚔️ BATTLE TIME FINAL ⚔️")
print()
print(winner, "has won in", round, "rounds!")