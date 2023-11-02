from getpass import getpass as input

print("MORE EPIC 🪨 📄 ✂️ BATTLE")

player1win = 0
player2win = 0
round = 1
print("Select your move (R, P or S)")

while True:
  print("Round:", round)
  player1 = input("Player 1 - ")
  player2 = input("Player 2 - ")

  if player1 == "R" and player2 == "P":
    print("Player 1's Rock is smothered by Player 2's Paper")
    player2win += 1
    round += 1
  elif player1 == "P" and player2 == "S":
    print("Player 1's Paper is cut by Player 2's Scissors")
    player2win += 1
    round += 1
  elif player1 == "S" and player2 == "R":
    print("Player 1's Scissors are crushed by Player 2's Rock")
    player2win += 1
    round += 1
  elif player2 == "R" and player1 == "P":
    print("Player 2's Rock is smothered by Player 1's Paper")
    player1win += 1
    round += 1
  elif player2 == "P" and player1 == "S":
    print("Player 2's Paper is cut by Player 1's Scissors")
    player1win += 1
    round += 1
  elif player2 == "S" and player1 == "R":
    print("Player 2's Scissors are crushed by Player 1's Rock")
    player1win += 1
    round += 1
  elif (player1 == "S" and player2 == "S") or (player1 == "R" and player2 == "R") or (player1 == "P" and player2 == "P"):
    print("TIE!")
    round += 1
  else:
    print("Try again!")

  print("Current Score = ", player1win, "/", player2win)
  
  if player1win == 3:
    print("Player 1 wins!")
    exit()
  elif player2win == 3:
    print("Player 2 wins!")
    exit()
  else:
    continue
