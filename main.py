from hangman import Hangman
from randomWord import random_word

def main():
    
    game = Hangman(random_word())

    while game.hangman_over():
        game.game()
        letterChose = input("Choose a letter: ")
        game.guess(letterChose)

    game.game()

    print("\nGood Game!\n")

main()