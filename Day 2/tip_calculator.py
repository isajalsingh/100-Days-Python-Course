#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
total_amount = input ("What is the total bill? $")
tip_percentage = input("What percentage tip would you like to give? ")
number_of_people = input("Who many people to split the bill? ")

amount_after_tip = float(total_amount) / 100 * float(tip_percentage) + float(total_amount)
amount_per_person = amount_after_tip / int(number_of_people)
amount_per_person = round(amount_per_person, 2)
amount_per_person = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: ${amount_per_person}")