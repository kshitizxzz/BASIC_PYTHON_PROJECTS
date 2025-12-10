# creating a welcome message

print('WELCOME TO MY QUIZ')
print('------------------')
playing = input('Do you wana play this quiz?' )

if(playing.lower()!='yes'):
    quit()

score = 0 
answer = input('What does CPU stands for ? ')
if answer.lower()=='central processing unit':
    print('Correct answer 🎉')
    score+=1
else :
    print('Incoreect')

answer = input('What does GPU stands for ? ')
if answer.lower()=='graphic processing unit':
    print('Correct answer 🎉')
    score+=1
else :
    print('Incoreect')

answer = input('What does PSU stands for ? ')
if answer.lower()=='power supply':
    print('Correct answer 🎉')
    score+=1
else :
    print('Incoreect')

answer = input('What does RAM stands for ? ')
if answer.lower()=='random access memory':
    print('Correct answer 🎉')
    score+=1
else :
    print('Incoreect')

print(f'you got {score} questions correct!')
print(f'you got {(score/4)*100}%')



