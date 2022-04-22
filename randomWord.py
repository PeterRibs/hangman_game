import random

def random_word():
    return random.choice(list(open("wordsBank.txt").read().split('\n')))