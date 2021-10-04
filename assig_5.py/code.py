########################################################################
##
## CS 101 Lab
## Program #Slots Program
## Name Osayamen Edo-Ohonba
## Email Osayzone@gamil.com
##
## PROBLEM : make a slot machine
##
########################################################################
def game():
    chips, chipsw, mod7 = 'NULL', 'NULL', 'NULL'
    while chips == 'NULL':
        chips = int(input('How many chips do you wnat to start with? ==>'))
        if chips <= 0:
            print('Too low a value, you can only choose 1 -100 chips')
            chips = 'NULL'
        elif chips >= 100:
            print('Too high a value, you can only choose 1 -100 chips')
            chips = 'NULL'
    while chipsw == 'NULL':
        chipsw =  int(input('How many chips do you want to wager? ==>'))
        if chipsw <= 0:
            print('The wager amount must be greater than 0.\nPlease enter again.')
            chipsw = 'NULL'
        elif chipsw >= chips:
            print(f'The wager amount cannot be greater than how much you have.  {chips}')
            chipsw = 'NULL'
    print(f'Your spin {} {} {} You matched {} reels You won/lost {}')
    


cont = 'Y'
while cont == 'Y':
    print(f'Your number was {game()}')
    cont = input('How amazing is that?\n\nDo you want to play again?Y to continue, N to quit  ==>')

print('How many chips do you want to start with? ==> -1')

#Your spin 4 2 9You matched 0 reelsYou won/lost -5  Current bank 5  How many chips do you want to wager? ==> 1Your spin 9 6 6You matched 2 reelsYou won/lost 2Current bank 7How many chips do you want to wager? ==> 8The wager amount cannot be greater than how much you have.  7
