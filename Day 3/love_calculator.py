print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name1_lower = name1.lower()
name2 = input("What is their name? \n")
name2_lower = name2.lower()

combined_name = name1 + " " + name2

count_T = combined_name.count("t")
count_R = combined_name.count("r")
count_U = combined_name.count("u")
count_E = combined_name.count("e")
count_L = combined_name.count("l")
count_O = combined_name.count("o")
count_V = combined_name.count("v")

true = count_T + count_R + count_U + count_E
love = count_L + count_O + count_V + count_E

final_percentage = true * 10 + love

if final_percentage <10 or final_percentage >90:
    print(f"Your score is {final_percentage}, you go together like coke and mentos.")
elif 40 < final_percentage < 50:
    print(f"Your score is {final_percentage}, you are alright together.")
else:
    print(f"Your score is {final_percentage}")