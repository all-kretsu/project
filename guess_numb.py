import random


# the game about guess a number
random_num = random.randint(1, 100)
guess_num = True

# function with script
def input_num():
    print('\nHello, its a guess number game!\n')
    print('Try to guess a number from 1 to 100!\n')
    global guess_num
    global random_num
    # tries to play
    for chance in reversed(range(1, 4)):
        print(f'\nYou have {chance} attempts!')
        # the game
        while True:
            try:
                # if number is valid
                guess_num = int(input('\nWhat number is?\n'))
                # if number is more than 100 or less than 1
                while guess_num <= 1 or guess_num > 100:
                    print('\nNumber is more than 1 and less than 100!')
                    guess_num = int(input('\nWhat number is?\n'))
            # need to insert a number still is  value error
            except ValueError:
                print('You must enter a number!')
            else:
                break
        # result conditions
        answer = ('Yes, you are right!\n'
                if guess_num == random_num
                else '\nNo, its wrong!\n')
        if guess_num == random_num:
            print('\n\t\tYou win!\n')
            break
        print(answer)
        # if tries will be an 1, script will show a hint
        if chance == 2:
            print(('\nIts more than 50!\n{}'.format(16 * '*'))
                if random_num > 50
                else print ('\nIts less than 50\n{}'.format(16 * '*')))
    # the answer
    print(f'The answer is: {random_num}!\n')

# offer to play again
def play_again_func():
    while True:
        play_again = input('Do you want to play again?\n"y" or "n":')
        play_again.lower
        if play_again == 'y':
            input_num()
        elif play_again == 'n':
            print('\n\tGood bye!\n')
            break
        else:
            continue
        
if __name__ == '__main__':     
    input_num()
    play_again_func()
