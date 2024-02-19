import random

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

figure = [Rock, Paper, Scissors]

option_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

option_system = random.randint(0, 2)
print(f"{figure[option_system]}\n Computer chose:")

print(f"{figure[option_user]}\n You chose:")

if option_user == 0:
    if option_system == 0:
        print("draw")
    elif option_system == 1:
        print("You lose!")
    elif option_system == 2:
        print("You win!")
elif option_user == 1:
    if option_system == 0:
        print("You win!")
    elif option_system == 1:
        print("draw")
    elif option_system == 2:
        print("You lose!")
elif option_user == 2:
    if option_system == 0:
        print("You lose!")
    elif option_system == 1:
        print("You win!")
    elif option_system == 2:
        print("draw")
