# get user input
your_year =  input("Enter a year: ")

while your_year.isdigit == False:
    print('You need to enter a integer!')
    your_year =  input("Enter a year: ")
while your_year.isdigit == True and int(your_year) < 0:
    print('You need to enter a non-negative number!')
    your_year =  input("Enter a year: ")
    
dict_zodiac = {2000: 'Dragon', 2001: 'Snake', 2002: 'Horse', \
               2003: 'Sheep', 2004: 'Monkey', 2005: 'Rooster', \
               2006: 'Dog', 2007: 'Pig', 2008: 'Rat', 2009: '`Ox', \
               2010: 'Tiger', 2011: 'Hare'}
for i in dict_zodiac.keys():
    if (int(your_year) - i) % 12 == 0:
        print(your_year, 'is the year of', dict_zodiac[i] + '. ')
        break
    

## you code needs to do the following things:
## 1. check if it is a integer; if not, ask the user to re input 
## 2. check if it is non negative; if not, ask the user to re input 
## 3. print the user's animal of the year on the screen