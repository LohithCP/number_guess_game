import random
a=random.randint(1,100)
num_of_chance=5
chance=1
print("Welcome to the Number Guessing Game")
print(f"The Number of guesses is:{num_of_chance}")
while(chance<=num_of_chance):
    print("Enter the Number")
    guess=int(input())
    if guess<a:
        print("Your Number is Small")
    elif guess>a:
        print("Your Number is Big")
    else:
        print("You Won the Game")
        print(f"Number to chances you took to complete:{chance}")
        break

    print(f"Number of chance remaining :{num_of_chance-chance}")
    chance += 1

if chance>num_of_chance:
    print("Game Over")