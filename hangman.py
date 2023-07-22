#Hangman
import random

print("Welcome to the Word Games.")

#Wordbank
word_list = ["hello", "world", "computer", "code"]

#Chooses the word
def choose_word():                                  
    global word_choice
    word_choice = random.choice(word_list)

choose_word()

wrong_tries = 0
letters = 0

word_length = int(len(word_list))

#Sets the limit to 5 tries per word.
while wrong_tries <=4:

    letter = str(input("Please choose a letter. \n"))

    if letter in word_choice:
        print("Correct.")
        letters +=1

        if int(letters) == int(len(word_choice)):
            print("You got it! The word is " + word_choice)
            break
    else:
        print("Sorry, wrong guess.")
        wrong_tries +=1

if wrong_tries == 5:
    print("Sorry, you have run out of tries. The word was " + word_choice + ".")