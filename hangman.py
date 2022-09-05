# Write your code here
import random

choose = "play"
win_count = 0
lost_count = 0
print("H A N G M A N")   
while choose != "exit":
    choose = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if choose == "play":

        list_of_disguises = ["python", "java", "swift", "javascript"]
        disguise = str(random.choice(list_of_disguises))
        guess_line = list("-" * len(disguise))
        guessed_letters = list()
        lives = 8
        while lives > 0 and "".join(guess_line) != disguise:
            print()
            print("".join(guess_line))
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("Please, input a single letter.")
            elif not letter.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in guessed_letters:
                print("You've already guessed this letter.")
            elif letter in disguise:
                for index in range(len(disguise)):
                    if letter == disguise[index]:
                        guess_line.pop(index)
                        guess_line.insert(index, letter)
            else:
                print("That letter doesn't appear in the word.")
                lives -= 1
            guessed_letters.append(letter)

        if "".join(guess_line) == disguise:
            print("You guessed the word", disguise + "!")
            print("You survived!")
            win_count += 1
        else:
            print()
            print("You lost!")
            lost_count += 1
    elif choose == "results":
        print("You won:", win_count, "times.")
        print("You lost:", lost_count, "times.")
