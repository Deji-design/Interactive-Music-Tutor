

from Lessons.major_scales import major_scales
from Lessons.musical_terminologies import musical_terminologies
from Lessons.minor_scales import minor_scales
from Lessons.note_intervals import note_intervals

# All predefined functions 

def main() :
# Introduction for user
    print("Welcome")

# Entry of user's information
    name = input("What is your full name? ").title().strip()
    nickname = input("What would you prefer to be referred to as? ").title().strip()
    age = int(input("What is your age? "))
    print()
    print(f"Welcome to the Interactive Music Tutor {nickname}!")


# Menu selection

    print ()
    print ("Please select a number from the list below:")
    print ("1. Learn major scales")
    print ("2. Learn minor scales")
    print ("3. Learn note intervals")
    print ("4. Learn musical terminologies")
    print ()
# Validates the user's choice
    try :
        choice = int(input("State choice here: "))

        if choice == 1 :
            print ("You have selected to learn major scales")
            print ()
            print ("Welcome to the major scales lesson")
            print ()
            major_scales ()
            
        elif choice == 2 :   
            print ("You have selected to learn minor scales")
            minor_scales()
        elif choice == 3 :
            print ("You have selected to learn note intervals")
            note_intervals ()
        elif choice == 4 :
            print ("You have selected to learn musical terminologies")
            musical_terminologies ()
        else :
            print(" Kindly pick a number from 1 to 4")
    except ValueError :
            print ("Please choose a number from the list above")
    

main ()




