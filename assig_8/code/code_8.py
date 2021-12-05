#######################################################################
## CS 101 Lab
## Program 8
## Name: Osay Edo Ohonba
## Email: ooenw7@umsystem.edu
##
## PROBLEM : Create write a program to allow the user to enter 2 types of grades and calculate them.
## ALGORITHM :
##      import math and time
##      Define functions
##      logic
##      End display
## ERROR HANDLING:
##      N/A
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import math
import time
assignment_scores = []
test_scores = []

def grade_menu():
    print('           Grade Menu\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignments\n6 - Clear Assignments\nD - Display Scores\nQ - Quit')
def add_test():
    test = int(input('Enter the new Test score 0-100 ==> '))
    if test < 0 or test > 100:
        return
    else:
        test_scores.append(test)
def remove_test():
     assignment_scores.remove[-1]
def clear_tests():
    test_scores.clear()
def add_assignment():
    assig = int(input('Enter the new Test score 0-100 ==> '))
    if assig < 0 or assig > 100:
        return
    else:
        assignment_scores.append(assig)
def remove_assignment():
    assignment_scores.remove[-1]
def clear_assignment():
    assignment_scores.clear()
def display_scores():
    print(test_scores, assignment_scores)

if __name__ == '__main__':
    u_input = ''
    while u_input != 'Q' or u_input != 'q':
        grade_menu()
        u_input = input('\n==> ')
        if u_input == '1': add_test()
        if u_input == '2': remove_test()
        if u_input == '3': clear_tests()
        if u_input == '4': add_assignment()
        if u_input == '5': remove_assignment()
        if u_input == '6': clear_assignment()
        if u_input == 'D' or u_input == 'd': display_scores()
        if u_input == 'Q' or u_input == 'q': print('Thank you for using this service. THE END')
        










