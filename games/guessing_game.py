import random as r

class GuessingGame:
    def __init__(self):
        # Default values
        self.chances = 0
        self.play_again = 'y'



    # This defines the entry for the menu
    def main_menu(self):
        print('Hello, I want to play a guessing game.')
        print('Do you want to hear the rules?')
        print('press y for yes or n for no.')
        entry = str.lower(input())
        rules = ('For this game, you will guess a number between 1 and 100 of which I will randomly select. If you\n' 
                 f'guess wrong, I will tell you higher or lower. You will have a number of guesses to get the\n' 
                 'correct answer. The number of guesses will be set by you once the game begins.')

        outer_control = False
        inner_control = False
        while outer_control == False:
            if entry == 'y':
                print(rules)
                print('Please set your difficulty. How many guesses would you like? Enter a number (1-10).')
                while inner_control == False:
                    try:
                        self.chances = int(input())
                        if self.chances > 0 and self.chances < 11:
                            outer_control = True
                            inner_control = True
                        else:
                            gg.response_invalid()
                    except Exception as e:
                        gg.response_invalid()
            elif entry == 'n':
                print('OK, let\'s start the game.')
                print('Please set your difficulty. How many guesses would you like? Enter a number (1-10).')
                while inner_control == False:
                    try:
                        self.chances = int(input())
                        if self.chances > 0 and self.chances < 11:
                            outer_control = True
                            inner_control = True
                        else:
                            gg.response_invalid()
                    except Exception as e:
                        gg.response_invalid()
            else:
                self.response_invalid()
                entry = str.lower(input())


    # Function to avoid repeating the same print statement
    def response_invalid(self):
        print('That is not a valid entry. Please try again.')


    # Triggers a replay if the user instructs the program to play again
    def replay(self):
        print('Do you want to play again?')
        print('Enter y to play again. Press any other key to exit.')
        self.play_again = str.lower(str(input()))


    # Takes responses from the user and determines the interactive responses to give back
    def interactive_counter(self):
        self.winner = False
        self.number = r.randrange(1, 101, 1)
        counter_values = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh',
                          8: 'eighth', 9: 'ninth', 10: 'tenth'}
        self.counter = 1
        while self.counter <= self.chances:
            if self.winner == False:
                print(f'Please enter your {counter_values[self.counter]} guess.')
                if self.counter == self.chances:
                    try:
                        guess = int(input())
                        self.guess_logic(guess)
                        if self.winner == True:
                            return gg.replay()
                        else:
                            print(f'Sorry, that was your last guess. The number I was thinking of was {self.number}.')
                            return gg.replay()
                    except Exception as e:
                        self.response_invalid()
                else:
                    try:
                        guess = int(input())
                        self.guess_logic(guess)
                        self.counter += 1
                    except Exception as e:
                        self.response_invalid()
            else:
                return gg.replay()


    # Logic that determines the accuracy of the user's guess. Called by the interactive_counter function within a loop
    def guess_logic(self, guess):
        guess_control = False
        while guess_control == False:
            if type(guess) == int:
                if (guess >= 1) & (guess <= 100):
                    if guess == self.number:
                        print('You guessed the number correctly! Great job!')
                        guess_control = True
                        self.winner = True
                    elif guess <= self.number:
                        print('That guess is too low.')
                        print(f'You have {self.chances - self.counter} guesses left.')
                        guess_control = True
                    else:
                        print('That guess is too high.')
                        print(f'You have {self.chances - self.counter} guesses left.')
                        guess_control = True
                else:
                    self.response_invalid()
                    try:
                        guess = int(input())
                    except Exception as e:
                        self.response_invalid()
            else:
                self.response_invalid()
                try:
                    guess = int(input())
                except Exception as e:
                    self.response_invalid()


gg = GuessingGame()

# Repeatable play loop
while gg.play_again == 'y':
    gg.main_menu()
    gg.interactive_counter()
else:
    exit(1)