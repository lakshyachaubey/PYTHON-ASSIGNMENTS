import random
def guess_game():
    num = random.randint(1,100)
    guess = 0
    count=0

    while guess!=num:
        guess=int(input("Enter your number: "))
        count+=1

        if guess>num:
            print("Too high")
        elif guess<num:
            print("Too low")
        else:
            print("Correct!")

    print(f"you guessed it in {count} attempts.")
    
guess_game()