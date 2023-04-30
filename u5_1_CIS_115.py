# Mark Bulmer - CIS 115 - 6-23-2021
# Obtain distance in kilometers and convert to miles.

def main():
    # display intro
    intro()
    # obtain distance in km
    userkm=int(input('Distance in kilometers: '))
    # convert to miles
    km_to_miles(userkm)

# Intro displays intro screen.
def intro():
    print('Convert kilometers to miles.')
    print('1 kilometer = 0.6214 miles')

# Obtain kilometers and display equivalent in miles.
def km_to_miles(km):
    miles=km*0.6214
    print('Distance in miles: ', miles)

# Call main function.
main()
