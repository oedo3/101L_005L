##########################################################################
## CS 101 Lab
## Program #lab 5
## Osay E.
## ooenw7@umsystem.edu
## PROBLEM : Describe the problem
##
## ALGORITHM :
##      1. Write out the algorithm
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
## 
## OTHER COMMENTS:
##      Any special comments
##
##########################################################################
import string
def character_value(char : str) -> int:
    alphabet = {
        'a': 1, 'b': 2, 'c':3,
        'd': 4, 'e': 5, 'f':6,
        'g': 7, 'h': 8, 'i':9,
        'j': 10, 'k': 11, 'l':12,
        'm': 13, 'n': 14, 'o':15,
        'p': 16, 'q': 17, 'r':18,
        's': 19, 't': 20, 'u':21,
        'v': 22, 'w': 23, 'x':24,
        'y': 25, 'z': 26}
    return alphabet[(char).lower]
def get_check_digit(idnumber : str) -> int:    
    ''' Returns the check digit for the name and sid. '''
    
def is_valid(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
def verify_check_digit(idnumber : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
def get_grade(idnumber : str) -> str:
    '''Returns the grade for index 6'''
    if __name__ == "__main__":
        print("{:^60}".format("Linda Hall"))
        print("{:^60}".format("Library Card Check"))
        print("="*60)

        while True:

            print()
            card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
            if card_num == "": 
                break
            result, error = verify_check_digit(card_num)
            if result == True:
                print("Library card is valid.")
                print("The card belongs to a student in {}".format(get_school(card_num)))
                print("The card belongs to a {}".format(get_grade(card_num)))
            else:
                print("Libary card is invalid.")
                print(error)