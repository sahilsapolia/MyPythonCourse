import sys

#get the file name
program_name = sys.argv[0]
print('original name \t\t', program_name)
print('uppercase\t\t', program_name.upper())
print('original name \t\t', program_name)
program_name=program_name.replace('_',' ')
print('removed under\t\t', program_name)
program_name=program_name.replace('.\\','')
print('removed .\\\t\t', program_name)
program_name=program_name.replace('.py','')
print('removed .py\t\t', program_name)
#upper
program_name=program_name.upper()
print('upper\t\t\t', program_name)

welcome_message = 'welcome to {}'
welcome_message = welcome_message.format(program_name)
print(welcome_message)

#use the center to display of center width
print('length is', len(program_name))
welcome_message = welcome_message.center(len(welcome_message)*3,'*')
print(welcome_message)

movie = input("what is your favourite movie? ")
movie = movie.strip()

good_year = False
while not good_year:
    year = input("What year is your favourite movie from? ")

    if(year.isdecimal()):
        year = int(year)
        if year < 1900 or year > 2020:
            continue;
        else:
            good_year = True
    else:
        print('Please enter a valid year')

print(movie)

message = "In {}, the movie {} debuted"
print(message.format(year,movie))
