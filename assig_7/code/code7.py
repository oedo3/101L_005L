########################################################################
## CS 101 Lab
## Assignment 7
## Name: Osay E
## Email: ooenw7@umsystem.edu
##
## PROBLEM : Read and output information about cars in files
########################################################################
def get_minimum_mpg():
    while True:
        try:
            minimum_mpg = float(input("Enter the minimum mpg ==> "))
            if minimum_mpg < 0:
                print('Fuel economy given must be greater than 0')
            elif minimum_mpg > 100:
                print('Fuel economy must be less than 100')
            else:
                return minimum_mpg
        except:
            print('You must enter a number for the fuel economy')

def get_input_file():
    while True:
        user_file = input('Enter the name of the input vehicle file ==> ')
        try:
            with open(user_file,'r') as read_file:
                return [[data.strip() for data in line.strip().split('\t')] for line in read_file.readlines()]

        except:
            print('Could not open file',user_file)
def get_output_file(minimum_mpg,file_data):
    while True:
        try:
            user_file = input('Enter the name of the file to output to ==> ')
            with open(user_file, 'w') as write_file:
                for data in file_data:
                    try:
                        if minimum_mpg >= float(data[7]):
                            write_file.write('{0:<5}{1:<40}{2:<40}{3:>10}\n'.format(data[0], data[1], data[2], data[7]))
                    except:
                        print('Could not convert value invalid for vehicle', data[0], data[1], data[2])
            return
        except:
            print('There is an IO Error', user_file)
if __name__ == "__main__":
    minimum_mpg = get_minimum_mpg()
    file_data = get_input_file()
    get_output_file(minimum_mpg, file_data)
    

    