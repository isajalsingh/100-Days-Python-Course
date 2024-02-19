print("Welcome to Python Pizza Deliveries!")

bill = 0
pizza_price = 0


size = input("What size of pizza do you want? S, M or L :")

if size == "S":
    pizza_price = 15
    print(f"Pizza Price = {pizza_price}")
elif size == "M":
    pizza_price = 20
    print(f"Pizza Price = {pizza_price}")
else:
    pizza_price = 25
    print(f"Pizza Price = {pizza_price}")

add_pepperoni = input("Do you want pepperoni? Y or N :")

if add_pepperoni == "Y" and size == "S":
    pizza_price += 2
    print(f"Pizza Price after Pepperoni = {pizza_price}")
elif add_pepperoni == "Y" and (size == "M" or "L"):
    pizza_price += 3
    print(f"Pizza Price after Pepperoni = {pizza_price}")

extra_cheese = input("Do you want extra cheese? Y or N :")

if extra_cheese == "Y":
    pizza_price += 1
    print(f"Pizza Price after Extra Cheese = {pizza_price}")

print(f"Final Bill = {pizza_price}")