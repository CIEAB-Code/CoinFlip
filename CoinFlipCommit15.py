import random

'''Valid Input Functions'''

def validguess():
  ''' checks that guess is valid'''
  validguess = False
  guess = input("Heads or Tails?:")
  if (guess != "Heads") and (guess != "Tails"):
    validguess == False
  while validguess == False:
    if (guess != "Heads") and (guess != "Tails"):
      guess = input("Please enter 'Heads' or 'Tails': ")
    else:
      validguess = True
  if validguess == True:
    return guess

def validbet():
  '''checks that bet is valid'''
  validbet=False
  bet = input("How much would you like to bet? 2, 5 or 10 pounds?: ")
  while validbet == False:
    if (bet != "2") and (bet != "5") and (bet != "10"):
      bet = input("Please enter 2, 5 or 10: ")
    if bet == "2" or bet == "5" or bet == "10":
      validbet = True

  if validbet == True:
    return int(bet)

def validchoice():
  '''checks choice to play is a valid input'''
  validchoice = False
  choice = input("Would you like to play again, y/n?: ")
  if (choice != "y") and (choice != "n"):
    validchoice == False
  while validchoice == False:
    if (choice != "y") and (choice != "n"):
      choice = input("Please enter 'y' or 'n': ")
    if (choice == "y") or (choice == "n"):
      validchoice = True
  if validchoice == True:
    return choice


def coin_flip_game(guess, bet):
  '''coin flip function'''
  money_won = 0
  money_won += bet
  money_lost= 0
  side = random.randint(1, 2)
  result=""
  timesplayed = 0

  if side ==1:
    result = "Heads"
  if side ==2:
    result = "Tails"
  
  if result == guess:
    money_won += bet
    print("{}! Congradulations you WON {}!".format(guess, str(bet)))
  elif result != guess:
    money_lost += bet
    print("{}! Oh no, you lost {} this time!".format(result, str(bet)))

  money = money_won - money_lost
  if (money > 0):
    print("Your total money is {}.".format(money_won - money_lost))
  if (money == 0):
    print("No money left!")

  return  money


if __name__ == "__main__":
    choice = "y"
    money_won = 0
    timesplayed = 0
    while choice == "y":
      bet = validbet()
      guess = validguess()
      money_won += coin_flip_game(guess,bet)
      choice = validchoice()
      timesplayed = timesplayed + 1
    if choice == "n":
      print("Okay see you next time!")

              
