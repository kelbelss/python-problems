import random
import os, time

print("Character Builder")

print()
time.sleep(2)

again = "yes"


def character():
  name = input("Name your Legend: ")
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  print(name, "the", type)


def roll(sides):
  result = random.randint(1, sides)
  return result


def health():
  roll6 = roll(6)
  roll8 = roll(8)
  health = (roll6 * roll8) / 2 + 10
  roundHealth = round(health)
  # return health
  print("HEALTH: ", roundHealth)


def strength():
  roll6 = roll(6)
  roll8 = roll(8)
  strength = round((roll6 * roll8) / 2 + 12)
  # return strength
  print("STRENGTH: ", strength)


while again == "yes":
  character()
  time.sleep(2)
  health()
  strength()
  time.sleep(4)
  os.system("clear")
  again = input("Create a new character? ")