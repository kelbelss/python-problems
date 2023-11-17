import random
import os, time

print("⚔️ BATTLE TIME ⚔️")

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
  

while True:
  
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The Battle Begins!")
  
  dice1 = roll(6)
  dice2 = roll(6)

  different = round(strengthOne - strengthTwo) + 1
