########################################################################
## CS 101 Lab
## Program #5
## Name: Osay E
## Email: ooenw7@umsystem.edu
##
## PROBLEM: Check library cards.
##      
## ALGORITHM : 
##      Check string in portions and return True or False
##
########################################################################
def get_school(card_id):
    if card_id[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif card_id[5] == '2':
        return 'School of Law'
    elif card_id[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return False

def get_grade(card_id):
    if card_id[6] == '1':
        return 'Freshman'
    elif card_id[6] == '2':
        return 'Sophomore'
    elif card_id[6] == '3':
        return 'Junior'
    elif card_id[6] == '4':
        return 'Senior'
    else:
        return False

def character_value(ch):
    return ord(ch) - 65
    
def get_check_digit(card_id):
    check_value = 0
    for i in range(0,4):
        check_value += character_value(card_id[i]) * (i + 1)
    for i in range(5,8):
        check_value += (int(card_id[i]) * (int(i)+1))
    return check_value % 10

def verify_check_digit(card_id):
    if len(card_id) != 10:
        return (False, 'The length of the number given must be 10')
    else:
        for i in card_id[0:5]:
            if character_value(i) < 0 or character_value(i) > 25:
                return (False, f'The first 5 characters must be A-Z, the invalid character is at {str(card_id.index(i))} is {i}')
        for i in card_id[7:10]:
            if i.isdigit() == False:
                return (False, f'The last 3 characters must be 0-9, the invalid character is at index is at {str(card_id.index(i))} is {i}')
        if get_school(card_id) == False:
            return (False, 'The sixth character must be 1 2 or 3')
        elif get_grade(card_id) == False:
            return (False, 'The seventh character must be 1 2 3 or 4')
        elif get_check_digit(card_id) != int(card_id[9]):
            return (False, f'Check Digit  {str(card_id[9])}  does not match calculated value {str(get_check_digit(card_id))}.')
        else:
            return (True, '')

if __name__ == '__main__':
    card_id = 'NULL'
    
    print('                    Linda Hall\n                   Library Check')
    print('=====================================================')
    print()

    while card_id != '':
        card_id = input('Enter library card. Press enter to exit: ')

        if card_id == '':
            print('The End')
        else:
            verify = verify_check_digit(card_id)
            if verify[0] == False:
                print('Library card is invalid.')
                print(verify[1])
                print()
            else:
                print('Library card is valid.')
                print('Card belongs to a student in the', get_school(card_id))
                print('Card belongs to a', get_grade(card_id))
                print()