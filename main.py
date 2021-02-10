rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_rps=[rock,paper,scissors]
our_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if our_choice>=3 or our_choice<0:
  print("You typed an invalid number,You lose.")

else:
  computer_choice=random.randint(0,2)
  print(game_rps[our_choice])
  print(f"computer chose {computer_choice}")
  print(game_rps[computer_choice])

  if our_choice==0 and computer_choice==2:
    print("You win!")
  elif computer_choice==0 and our_choice==2:
    print("You lose")
  elif computer_choice > our_choice:
    print("You lose")
  elif our_choice>computer_choice:
    print("You win!")
  elif our_choice==computer_choice:
    print("Draw")

