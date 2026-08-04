# a simple program that prints what animal the user types into the terminal
animal = input('type either dog/cat')

# I added this line of code so that it is not case sensitive
animal = animal.upper()

if animal == 'DOG':
    print('bark')
elif animal == 'CAT':
    print('meow')
else:
    print('that was not a option')