import random

name_string = input("Enter everyone name, seperated by comma:\n")
names = name_string.split(", ")
print(names) 

no_of_names = len(names)

random_number = random.randint(0, no_of_names - 1)
person_to_pay_bill = names[random_number]

print("\n"+person_to_pay_bill +' will pay the bill today.\n')