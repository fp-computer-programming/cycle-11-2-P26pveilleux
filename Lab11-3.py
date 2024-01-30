import random 

def number_guess():
    target_number = random.randiant(0,100)

    while true:
        guess = int(input("guess the number (between 0,100)"))

        if guess == target_number:
            print("Correct")  
            break
        elif guess < target_number:
            print("incorrect")



