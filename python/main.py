from numpy import random
# Some cool modules to help me cheat
from hashlib import sha1
from getpass import getpass
#To punish the bad player
from time import sleep

MIN_NUMBER = 0
MAX_NUMBER = 100

def game():
    #The game in itself
    print("Welcome to the guessing game! Try to guess the number I have in mind...\n")

    # The random number to guess
    r = random.randint(MIN_NUMBER,MAX_NUMBER)
    found = False

    # To help me cheat
    secret_key = getpass("If you wrote this code, please enter secret key to unlock answer. Otherwise, just hit enter ").encode()
    if sha1(secret_key).hexdigest() == "05bd553d0ddaac955dcc8d61986b02578b6f2b87":
        print("Hey Gautham, here's the number: " + str(r) + "\n")
        game()
    else:
        print("You're not Gautham! Please continue...\n")
    
    #A small hint
    halfway = (MAX_NUMBER - MIN_NUMBER) // 2
    if r > halfway:
        print("Pssst! Hint - It's probably more than halfway between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER))
    elif r < halfway:
        print("Pssst! Hint -  It's probably less than halfway between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER))
    else:
        print("Pssst! Hint -  It's probably halfway between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER))
    
    # (Truly eternal) loop
    while not found:
        entry = input("\nEnter a number between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER)+": ")
        while not entry.isdigit():
            print("Please input a number")
            entry = input("\nEnter a number between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER)+": ")
        entry = int(entry)

        #Condition to punish the player
        if (entry < MIN_NUMBER) or (entry > MAX_NUMBER):
            print("With great power comes great responsibility. Stay within the range mate. The game will pause for 10 seconds\n")
            sleep(10)
            continue

        # Condition on what to do
        if entry == r:
            print("\n\nGood job, it was "+str(r)+"!!!\n\n")
            found=True
            game()
        elif entry>r:
            print("A bit less?")
        else:
            print("A bit more?")

game()