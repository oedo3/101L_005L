def get_mpg():
    try:
        mpg = int(input('Enter the minimum mpg ==> '))
        if mpg <= 0:
            print('Fuel economy given must be graeter than 0')
            get_mpg()
        if mpg >= 100:
            print('Fuel economy given must be less than 100')
            get_mpg()
    except:
        print('You must enter a number for the fuel economy')

    