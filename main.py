#Introduction for user
print("Welcome")

# Entry of user's information
Name = input("What is your full name? ").title().strip()
Nickname = input("What would you prefer to be referred to as? ").title().strip()
Age = input("What is your age? ").strip()
print()
print(f"Welcome to the Interactive Music Tutor {Nickname}!")



# Menu selection
print ()
print ("Please select an option from the list below:")
print ("1. Learn major scales")
print ("2. Learn minor scales")
print ("3. Learn note intervals")
print ("4. Learn musical terminologies")
print ()

try :
    choice = int(input("State choice here: "))

    if choice == 1 :
        print ("You have selected to learn major scales")
    elif choice == 2 :   
         print ("You have selected to learn minor scales")
    elif choice == 3 :
        print ("You have selected to learn note intervals")

    elif choice == 4 :
        print ("You have selected to learn musical terminologies")
except ValueError :
        print ("Please choose a number from the list above")