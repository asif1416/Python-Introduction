print("Select your ride:")
print("1. Bike")
print("2. Car")

# Take input of number 1 or 2
# Select your ride
choice = int(input("Enter your choice: "))

# User entering option 1: condition 1 outer if statement
if choice == 1:
    print("What type of bike?")
    print("1. Scooty")
    print("2. Scooter")

    # Condition for selecting the type of bike
    choice2 = int(input("Enter your choice2: "))

    if choice2 == 1:  # Inner if statement
        print("You have selected scooty")
    else:
        print("You have selected scooter")

# User entering option 2: outer elif statement
elif choice == 2:
    print("What type of car?")
    print("1. Sedan")
    print("2. XUV")
    choice3 = int(input("Enter your choice3: "))

    if choice3 == 1:  # Inner if statement
        # Condition for selecting the type of car
        print("You have selected sedan")
    else:
        print("You have selected XUV")

else:
    print("Wrong place!")            