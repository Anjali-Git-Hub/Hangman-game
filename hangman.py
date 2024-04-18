import hangman_stages
import random

class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.blanks = ["_"] * len(word)
        self.points = 6
        self.guessed_letters = []

    @staticmethod
    def choose_word():
        word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach","car","light","motion","key"]
        return random.choice(word_list)

    def guess(self, letter):
        if letter in self.guessed_letters:
            print("You've already guessed that letter.")
            return

        self.guessed_letters.append(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.blanks[i] = letter
            if "_" not in self.blanks:
                print("Congratulations! You've guessed the word:", ''.join(self.blanks))
                return "win"
        else:
            self.points -= 1
            print("Incorrect guess. You have {} points left.".format(self.points))
            if self.points == 0:
                print("You've run out of points. The word was:", self.word)
                return "lose"

    def play(self):
        while self.points > 0 and "_" in self.blanks:
            print("Current Status:", ' '.join(self.blanks))
            letter = input("Guess a letter: ").lower()
            result = self.guess(letter)
            if result == "win" or result == "lose":
                break
            print(hangman_stages.stages[self.points])

# Usage
word = HangmanGame.choose_word()
game = HangmanGame(word)
game.play()
