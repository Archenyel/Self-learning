import random

choice = input("guess a number between 1 and 100, choose dificult. \"write\" easy or \"hard\"")

def dificult_selector(choice):
    choice = choice.lower()
    if choice == "easy":
        return 10
    elif choice == "hard":
        return 5
    else:
        print("invalid dificult") 
        return 0


attemps = int(dificult_selector(choice))
guessing_number = random.randint(1,100)

while attemps > 0 :

    guess = int(input("write a number \n"))

    if guess > guessing_number : print("too high")
    if guess < guessing_number : print ("to low")
    if guess == guessing_number:
        print("correct")
        attemps = 0
        break
    attemps -= 1
    print(f"attemps remaining {attemps}")

print("game over")