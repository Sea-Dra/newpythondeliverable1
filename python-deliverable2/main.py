print("Welcome to the GC Fruit Market!")

user_name = input("What is your name?\n")

user_fruit = input(f"Welcome {user_name}! Which fruit would you like to buy?\n"
                   f"1) Apples $2\n"
                   f"2) Grapes $1\n"
                   f"3) Oranges $3\n")

if user_fruit == 1:
    print("You bought 1 Apple for $2")
elif user_fruit == 2:
    print("You bought 1 Grape for $1")
elif user_fruit == 3:
    print("You bought 1 Orange for $3")
answer = input("Would you like to buy another fruit? y/n\n")
while answer == ["y", "yes", "yup"]:
    user_fruit = input(f"Welcome {user_name}! Which fruit would you like to buy?\n"
                       f"1) Apples $2\n"
                       f"2) Grapes $1\n"
                       f"3) Oranges $3\n")
    if user_fruit == 1:
        print("You bought 1 Apple for $2")
    elif user_fruit == 2:
        print("You bought 1 Grape for $1")
    elif user_fruit == 3:
        print("You bought 1 Orange for $3")
    answer = input("Would you like to buy another fruit? y/n\n")
    if answer == ["n", "no", "nope"]:
        break
subtotal = user_fruit