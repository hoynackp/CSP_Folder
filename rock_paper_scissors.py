import random
loop_is_running = True
computer_score = 0
player1_score = 0
while loop_is_running:
    player1 = (input('Enter rock, paper, or scissors: ')).lower()
    print(' ')
    computer = random.choice(['rock', 'paper', 'scissors'])
    print('You chose', player1)
    print('The computer chose', computer)
    if player1 == 'rock':
        if computer == 'scissors':
            print(' ')
            print('You win')
            player1_score += 1
            loop_is_running = False
        elif computer == 'paper':
            print(' ')
            print('You lose')
            computer_score += 1
            loop_is_running = False
        else:
            print('You tied, play again')
            print(' ')
    elif player1 == 'paper':
        if computer == 'rock':
            print(' ')
            print('You win')
            player1_score += 1
            loop_is_running = False
        elif computer == 'scissors':
            print(' ')
            print('You lose')
            computer_score += 1
            loop_is_running = False
        else:
            print('You tied, play again')
            print(' ')
    elif player1 == 'scissors':
        if computer == 'paper':
            print(' ')
            print('You win')
            player1_score += 1
            loop_is_running = False
        elif computer == 'rock':
            print(' ')
            print('You lose')
            computer_score += 1
            loop_is_running = False
        else:
            print('You tied, play again')
            print(' ')
    else:
        print(player1, 'is not a valid input')
    if loop_is_running == False:
        print(' ')
        y = (input('Do you want to play again? ')).lower()
        if y == 'yes':
            loop_is_running = True
            print(' ')
        else:
            loop_is_running = False
            print(' ')
            if player1_score > computer_score:
                print('You scored', player1_score)
                print('The computer scored', computer_score)
                print('You beat the computer! Congratulations!')
                print(' ')
            elif player1_score < computer_score:
                print('You scored', player1_score)
                print('The computer scored', computer_score)
                print('Sorry, the computer beat you.')
                print(' ')
            else:
                print('You scored', player1_score)
                print('The computer scored', computer_score)
                print('You tied with the computer')
                print(' ')