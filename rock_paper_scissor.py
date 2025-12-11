import random

user_wins = 0
computer_wins = 0
options = ['rock' , 'paper'  , 'scissor'] ## all lowercase
while True:

    user_pick = input('Type: Rock / Paper / Scissor or Press Q to quit : ').lower()
    # confirming what he picked is correct
    if user_pick=='q':
        break 
    if user_pick not in options:
        continue 

    computer_pick = random.randint(0,2) 
    computer_pick = options[computer_pick]

    # now conditions for wining or loosing
    print('computers pick----->', computer_pick.upper())

    if user_pick == 'rock':
        if computer_pick == 'rock':
            print('tie')
        elif computer_pick == 'paper':
            print('you loose')
            computer_wins+=1
        else :
            print('you won')
            user_wins+=1
        

    elif user_pick == 'paper':
        if computer_pick == 'rock':
            print('you won')
            user_wins+=1
        elif computer_pick == 'paper':
            print('tie')
        else :
            print('you loose')
            computer_wins+=1
    
    else: ## u picked scissor
        if computer_pick == 'paper':
            print('you won')
            user_wins+=1
        elif computer_pick == 'scissor':
            print('tie')
        else :
            print('you loose')
            computer_wins+=1

print('you scored' , user_wins )
print('computer scored' , computer_wins )



    
    







