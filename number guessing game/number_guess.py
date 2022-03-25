import random
print("you need to guess the number correctly in this game")
print("the numbers will be from 1 to 10 \nyou have three chances")
print("ready??")
ready = input("press y or n:").lower()
if ready == 'y':
    game_on = True
else:
    game_on = False

count = 1
num = random.randint(1,11)
while game_on:
    try:
        guess = int(input("\n\nguess the hidden number:"))
        if guess == num and count < 3:
            print("your guess is correct")
            break
        elif guess!=num and count < 3:
            print("nope you are wrong try again")
        elif count >= 3:
            print("You are out of chances")
            print('try it from start')
            break
        count += 1
    except ValueError:
        print("Please type in a number")
