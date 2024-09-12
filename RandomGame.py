import random
won = 0
loss = 0
total = 0
num = 0

print('Enter -1 to exit')
while num != -1:
    guess = random.randint(1,9)
    print('________________________Guessing game________________________')
    num = int(input('Enter a number(from 1 to 9): '))
    if num == guess:
        print('Congratulation you won!!')
        won = won + 1
    elif num == -1:
        print('Thanks for playing')
        total = total + 1
    else:
        print('You have guessed wrong please try again')
        print(f'The number is {guess}')
        loss = loss + 1
        total = total + 1

print(f'You have won {won} games out of {total} games')
print(f'You have lost {loss} games out of {total} games')