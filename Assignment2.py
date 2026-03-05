import random

words_list = ["python", "attack", "tokyo", "college", "devil", "god", "japan","java","earth","space","nature","eminem","kiet"]

score = 0
play = 1

print("Welcome to the Word Scrambling Game")

while play ==1:

    word = random.choice(words_list)

    word_list = list(word)
    random.shuffle(word_list)
    scrambled = "".join(word_list)

    attempts = 3
    guessed = False

    while attempts > 0:
        guess = input("Guess the word: ")

        if guess == word:
            print("Correct!")
            score = score + 10
            guessed = True
            break
        else:
            attempts = attempts - 1
            print("Wrong guess")
            print ("Attempts left:", attempts)

    if guessed == False:
        print("The correct word was:", word)

    print("Current Score:", score)

    play = int(input("Do you want to play again? (1/0): "))

print("Game Over")
print("Final Score:", score)