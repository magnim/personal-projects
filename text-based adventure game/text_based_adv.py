print("Welcome to your adventure!")
ready = input("Are you ready! Y or N? : ").upper()
if ready == 'Y':
    game_on = True
else:
    game_on = False
sword = False
coins = 100
while game_on:
    enter_dungeon = input("Do you wish to enter the dungeon? :: Y or N : ").upper()
    if enter_dungeon == 'Y' and sword:
        print("you have entered the first level of the dungeon\n")
        print("You have walked for a while and came to a place which leads to two directions")
        direction = input("which way do you wish to go? TYPE 'Left' to go left or 'Right' to go right : ").lower()
        if direction == 'left':
            print("You have walked for a while")
            print("You have encountered a dungeon monster and slayed it!")
            print("\n\nHooray!!!\nYou have got you first kill!!")
            game_on = False
        elif direction == 'right':
            print("You have encountered the floor boss and it defeated you.")
            game_on = False
    elif enter_dungeon == 'N':
        print("\n\nOk! see you another time")
        game_on = False
    elif not sword:
        print("please visit the shop to buy a sword")
        shop = input('\n Do you wish to enter the shop? Y or N : ').upper()
        if shop == 'Y':
            enter_shop = True
        else:
            enter_shop = False
            game_on = False
        if enter_shop:
            buy_sword = input("Do you wish to buy a sword? Y or N : ").upper()
            if buy_sword == 'Y' and coins > 10:
                sword = True
                print("You got yourself a new sword")
                coins -= 10
                print("You have ", coins , " coins")
            else:
                print("See you again")
            
