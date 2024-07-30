print("Welcome to the GC Fruit Market!")

user_name = input("What is your name?\n")
apple_price = 2
grape_price = 1
orange_price = 3

apples = 0
grapes = 0
oranges = 0

user_fruit = input(f"Welcome {user_name}! Which fruit would you like to buy?\n"
                   f"1) Apples $2\n"
                   f"2) Grapes $1\n"
                   f"3) Oranges $3\n")

if user_fruit == "1":
    print("You bought 1 Apple for $2")
    apples += 1
elif user_fruit == "2":
    print("You bought 1 Grape for $1")
    grapes += 1
elif user_fruit == "3":
    print("You bought 1 Orange for $3")
    oranges += 1
else:
    print(f"{user_fruit} is an invalid option")


answer = input("Would you like to buy another fruit? y/n\n")
while answer == "y":
    user_fruit = input(f"Welcome {user_name}! Which fruit would you like to buy?\n"
                       f"1) Apples $2\n"
                       f"2) Grapes $1\n"
                       f"3) Oranges $3\n")

    if user_fruit == "1":
        print("You bought 1 Apple for $2")
        apples += 1
    elif user_fruit == "2":
        print("You bought 1 Grape for $1")
        grapes += 1
    elif user_fruit == "3":
        print("You bought 1 Orange for $3")
        oranges += 1
    answer = input("Would you like to buy another fruit? y/n\n")
    if answer == "n":
        break
print("Order for " + user_name)
print(f"{apples} apple(s) at ${apple_price} apiece")
print(f"{grapes} grape(s) at ${grape_price} apiece")
print(f"{oranges} orange(s) at ${orange_price} apiece")
sub_total = int(apples * (int(apple_price)) + int(grapes * (int(grape_price)) + int(oranges * int(orange_price))))
print(f"Subtotal: ${sub_total}")
tax = (5 * int(sub_total)) / 100
print(f"5% Tax: ${tax}")
total = sub_total + tax
print(f"Total: ${total}")
