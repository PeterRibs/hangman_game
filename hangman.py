from hangmanBoard import hangmanBoard

class Hangman():

    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []
        self.gameOn = True

    def guess(self, letter):
        if letter.lower() == "quit":
            self.gameOn = False
        elif len(letter) == 0:
            print("Choose a letter!")
        elif letter.lower()[0] in self.guessed_letters or letter.lower()[0] in self.missed_letters:
            print("You already choose this letter!")
        elif letter.lower()[0] in self.word and letter.lower()[0] not in self.guessed_letters:
            self.guessed_letters.append(letter.lower()[0])
        elif letter.lower()[0] not in self.word and letter.lower()[0] not in self.missed_letters:
            self.missed_letters.append(letter.lower()[0])
               
    def hangman_over(self):
        if self.gameOn == False:
            print("\n#### Bye bye! ####")
            return False
        else:
            if self.hangman_loose() == False:
                print("\n#### YOU LOOSE! ####")
                return False
            else:
                if self.hangman_won() == False:
                    print("\n#### YOU WON! ####")
                    return False
                else:
                    return True

    def hangman_won(self):
        if '_' not in self.hide_word():
            return False
        else:
            return True
    
    def hangman_loose(self):
        if len(self.missed_letters) == (len(hangmanBoard)-1):
            return False
        else:
            return True

    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += "_"
            else:
                rtn += letter
        return rtn

    def game(self):
        print(hangmanBoard[len(self.missed_letters)])
        print("Palavra: %s\n"%(self.hide_word()))
        print("Letras erradas:\n%s\n"%("\n".join(self.missed_letters)))
        print("Letras certas: \n%s\n"%("\n".join(self.guessed_letters)))