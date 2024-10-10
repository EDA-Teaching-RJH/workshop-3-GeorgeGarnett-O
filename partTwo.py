import random 

secret_number = input(random.randint(1, 10))

guess = int(input("the corect number from the secret number randomizer"))


if guess > secret_number :

   print  ("too high")
elif guess < secret_number : 
   print  ("too low")
elif guess == secret_number: 
   print  ( "correct number")
