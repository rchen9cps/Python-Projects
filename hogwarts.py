#Raymond Chen
#hogwarts.py
#This program's function is to print the Hogwarts house a person belongs to

#Init
import time
import random

#Functions
def main(): #Main function
    print("Welcome to Hogwarts")
    nam = input("What is your name: ")
    name = nam.lower()
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print("......")
    print(house(name))
def house(name): #House checker
    if name == "harry" or name == "ron" or name == "hermione":
        return "Gryffindor!"
    elif name == "newt" or name == "nymphadora" or name == "pomona":
        return "Hufflepuff!"
    elif name == "luna" or name == "cho" or name == "filius":
        return "Ravenclaw!"
    elif name == "voldemort" or name == "draco" or name == "severus":
        return "Slytherin!"
    else:
        x = random.randint(1,4)
        if x == 1:
                return "Gryffindor!"
        if x == 2:
                return "Hufflepuff!"
        if x == 3:
                return "Ravenclaw!"
        if x == 4:
                return "Slytherin!"

#Main
main() #Runs function
while True:
    agai = input("Would you like to play again (yes/no)? ")
    again = agai.lower()
    if again == "yes":
        print("Restarting...")
        main()
    elif again == "no":
        print("Goodbye!")
        break
    else:
        print("Please try again (yes/no). ")
