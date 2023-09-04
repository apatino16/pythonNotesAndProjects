# high-low.py: a simple guess the number game
import random

#500 is the maximum secret number
secret = random.randint(1, 501)
count = 0

#Game asks your name at the beginning, your inputed name will be used throught the instructions and hints
name = str(input(f"What is your name? Type your name : "))

#General game instructions
print(f"To start playing type a valid number as your guess. If you desire to exit the game type 'quit'. Enjoy the Game {name}!") 

# while True makes the loop run indefinitively until the correct guess is made
while True:
    
    count += 1
    
    guess = input(f"{name}'s guess #{count}. Enter your guess (1-500): ")
    
    #The game ends when the players inputs "quit"
    if guess.lower() == "quit":
        print(f"Thank you for playing {name}! The secret number was {secret}.")
        break
    
    #Makes sure that the player can only type a number or the word quit and raises a Value error otherwise
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number or 'quit'.")
        continue
    
    if guess == secret:
        print(f"Correct! That's the right number {name}.")
        break
    
    #When your guess is within 10 digits of the secret number the game provides a hint that you are getting closer to the answer    
    elif abs(guess - secret) <=10:
        print(f"{name} you are getting close.")
    elif guess < secret:
        print(f"{name} your guess is too low.")
    elif guess > secret:
        print(f"{name} your guess is too high.")
   
print(f"Game over!")