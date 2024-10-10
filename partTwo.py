import random 

secret_number = random.randint(1, 10)

loop = True 

while loop == True:

    guess = int(input("number from the secret number randomizer"))


    if guess > secret_number :

        print  ("too high")
    elif guess < secret_number : 
        print  ("too low")
    elif guess == secret_number: 
        print  ( "correct number") 
        loop = False 

