 ########################################################################
 ## CS 101 lab
 ## Assig_10
 ## Name: Osay E.
 ## Email: ooenw7@umsystem.edu
 ##
 ## PROBLEM : Write a program to read file and output
 ## ALGORITHM :
 ##      make dictionary and enumerate
 ##ERROR HANDLING
 ##      N/A
 ##
 ########################################################################
from string import punctuation
def get_file():
    user_file = input('Enter of the name of the file to open: ')
    while True:
        try:
            with open(user_file, 'r') as file:
                lines = file.readlines()
            return lines
        except:
            print('Could not open file {}'.format(user_file))
            print('Please try again')
            user_file = input('Enter of the name of the file to open: ')
if __name__ == "__main__" :
    word_dict = dict()
    file = get_file()
    for line in file:
        for n in line:
            if n in punctuation:
                line = line.replace(n, "")
    for line in file:
        for text in line.lower().strip().split(" "):
            text = text.strip(punctuation)
            if len(text) <= 3:
                continue
            else:
                if text in word_dict.keys():
                    word_dict[text] = word_dict[text] + 1
                else:
                    word_dict[text] = 1
    word_freq_dict = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
    only_once = 0
    for key in word_freq_dict:
        if word_freq_dict[key] == 1:
            only_once += 1
    print('\nMost frequently used words')
    print('{:<3}{:>20}{:>12}'.format('#', 'Word', 'Freq.'))
    print('=' * 35)
    for i, key in enumerate(word_freq_dict):
        print('{:<3}{:>20}{:>12}'.format(i + 1, key, word_freq_dict[key]))
    print('\nThere are {} words that occur only once'.format(only_once))
    print('There are {} unique words in the document'.format(len(word_freq_dict)))