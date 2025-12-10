import random

top_of_range = input('Type a number:' )

# cheking top_of_range conditions

if top_of_range.isdigit() or top_of_range.lstrip('-').isdigit() : # cheking the number is a digit in form of string
    top_of_range = int(top_of_range)
    if(top_of_range<=0):
        print('Please enter a number >0 . Next time🙏🏻')
        quit()

else :
    print('please enter a digit . Next time🙏🏻')
    quit()

random = random.randint(1 , top_of_range)

# now making guesses in a while loop 

trials = 0

while(1):

    trials+=1

    guess = input('Please guess a number: ')

    if guess.isdigit(): # cheking the number is a digit in form of string
        guess = int(guess)

    else :
        print('please enter a digit . Next time🙏🏻')
        continue 


    if guess==random:
        print('you got it!')
        break

    elif guess>random:
        print('lower your guess')
    elif guess<random:
        print('higher your guess')

if trials==1:
    print('you guessed in ' , 1 , 'guess')
else:
    print('you guessed in' , trials , 'guesses')

    



