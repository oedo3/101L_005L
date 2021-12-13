 ########################################################################
 ## CS 101 Lab
 ## Assignment 11
 ## Name: Osay E.
 ## Email: ooenw7@umsystem.edu
 ##
 ## PROBLEM : Create a clock class that keepstrack of time based of user input.   
 ## ALGORITHM :
 ## 
 ## ERROR HANDLING
 ##      N/A
 ##
 ########################################################################
import time
class Clock:
    def __init__(self, hour=0, minute=0, second=0, am_or_pm=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.am_or_pm = am_or_pm
        self.no_am_or_pm = ''
    def __str__(self):
        if self.am_or_pm == 0:
            return "{:02}:{:02}:{:02}{:<2}".format(self.hour, self.minute, self.second, self.no_am_or_pm)
        else:
            if self.hour > 11:
                self.no_am_or_pm = ' pm'
            else:
                self.no_am_or_pm = ' am'
            return "{:02}:{:02}:{:02}{:<2}".format(self.hour, self.minute, self.second, self.no_am_or_pm)
    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.second = self.second - 60
            self.minute += 1
        elif self.minute >= 60:
            self.minute = self.minute - 60
            self.hour += 1
        elif self.hour > 23:
            self.hour = self.hour - 24
if __name__ == "__main__":
    hours = int(input('What is the current hour ==> '))
    minutes = int(input('What is the current minute ==> '))
    seconds = int(input('What is the current second ==> '))
    clock = Clock(hours, minutes, seconds, 1)
    while True:
        print()
        print(clock)
        clock.tick()
        time.sleep(1)