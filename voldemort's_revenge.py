import pyfiglet
import time
import random
import sys
import os
import inflect
import textwrap
import cmd
import pygame
import json

with open('game-text.json', 'r') as f:
    data = json.load(f)

p = inflect.engine()

player = {'attack': 10, 'heal': 20, 'health': 100}
monster = {'name': 'Voldemort', 'attack': 12, 'health': 100, 'heal': 5, 'attack1': 10}

WOOD_MAPPING = {
    'a': data['opts_a'],
    'b': data['opts_b'],
    'c': data['opts_c'],
    'd': data['opts_d'],
    'e': data['opts_e'],
    'f': data['opts_f'],
    'g': data['opts_g']
}

HOUSE_LIST =['a. Benevolence','b. Courageousness', 'c. Knavishness', 'd. Intelligence']

HOUSE_MAPPING = {
    "a": "Hufflepuff",
    "b": "Gryffindor",
    "c": "Slythrin",
    "d": "Ravenclaw"
}

def title_screen_selection():
    """
    This function helps player to decide whether you want to play,need help with the moves or quit the game.
    The function is taking input from the player and based on that conditional loops will work.
    If user types other command than play, help and quit, it will show a error message asking player to
    type valid command.
    """
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please Enter a valid command.")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def help_menu():
    """
    This function has help menu contents like how to play the game and are placed in json file.
    When player hits help from the title_screen_selection the json file will print the contents of help_menu.
    """
    print(data['help_menu']['text'])
    title_screen_selection()


def title_screen():
    """
    This function is use for displaying the title screen with the three menus - play,help and quit.
    The contents of the function are placed in json file.
    """
    os.system('clear')
    print(data['title_menu']['text'])
    title_screen_selection()

### player creds
def setup_game():
    """
    This function is for setting up the player in the game.
    The function has used Input function to take input from the player by asking their names.
    """
    os.system('clear')
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")

### first stage of chambers of sceret
def movement_handler1():
    """
    This function is the first stage of the game loop.
    Input function is used to take input from the player what spells they want to cast.
    Conditional statements is used to decide what happens if they use these spells.
    And  while loop is used to provide another life to player if they answer incorrectly.
    """
    for statement in data['move1']:
        print(statement)
        time.sleep(1)
    ans = input("> ")

    if ans in ["Expelliarmus", "Incendio"]:
        print("You have disarmed the Troll, you need to cast the stronger spell to kill him.")

    while ans not in ["Stupefy", "Levicorpus"]:
        print("Try again one more time, you have last chance to kill him.")
        ans = input("> ")
        while ans not in ["Stupefy", "Levicorpus"]:
            print("Sorry! you have lost to Troll.")
            exit()
            break

    if ans in ["Stupefy", "Levicorpus"]:
        print("Phewww! you are able to kill the Troll.")
        movement_handler2()
    else:
        print("Sorry! you have lost to Troll.")
        exit()


def movement_handler2():
    """
    This function is second part of the first level of game.
    Random functionality is used to choose certain items in the level.
    Input function is used to take input from the player, if incorrect, While loop will help player to
    ask again for the correct item.
    """
    for statement in data['move2']:
        print(statement)
        time.sleep(1)

    correct_num = random.randint(1, 10)
    keep_guessing = True
    while keep_guessing:
        guess = int(input("Enter the number key:"))
        if guess == correct_num:
            print("Sweet! You have amazingly figured the correct key.")
            level2()
            break
        else:
            print("Try again with another key.")


def movement_handler3():
    """
    This function is second stage of the game, player reaches this function after successfully completing the
    first stage of game.
    Input function is used to ask player if they want to continue the game and moving ahead for the second stage tasks.
    Conditional statements are used for users to give answer to the riddle, if incorrect, it will take you
    out of the game.
    """
    for statement in data['move3']:
        print(statement)
        time.sleep(1)

    first_ans = input("> ")
    if first_ans == "yes":
        print("Woman's Voice - answer this riddle and you are through to the next level!\n")
        time.sleep(2)
        print("I roam the woods of Hogwarts school.\n And my coat is a lovely white,\n But don't you dare,\
try to drink my blood,\n Or you'll be cursed for life.\n Who am I?\n")
        print("- A white animal\n")
        ans = input("> ")
        if ans == 'unicorn':
            print("Wicked! You have successfully solve the riddle.")
        else:
            print("Sorry..that is not a correct answer, you lost!")
            exit()
    else:
        print("You were very close to rescue Harry!")
        exit()


def movement_handler4():
    """
    This function is used for second part of second stage of the game.
    Input function used to ask if they want to continue the game or not, if not they will be out of the game and
    if in then another input will be taken to ask what action they want to perform.
    Conditional statements is used to decide what happens if they use these spells.
    And  while loop is used to provide another life to player if they answer incorrectly.
    """
    for statement in data['move4']:
        print(statement)
        time.sleep(1)

    ans = input("> ")
    if ans == 'yes':
        print("You try to hide to attack her...")
        time.sleep(2)
        print("Which spell you would like to cast?\n")
        print("You can choose spells :Expectopatronum, Crucio, Imperio, Sectumsempra\n")
        spell = input("> ")
        if spell in ["Imperio","Crucio"]:
            print("You are only able to disarm her, cast some stronger spell to kill her.\n")
        while spell not in ["Expectopatronum", "Sectumsempra"]:
            print("Try again one more time!")
            spell = input("> ")
            while spell not in ["Expectopatronum", "Sectumsempra"]:
                print("Tough! you did your best but you didnt survive.")
                exit()
                break
        else:
            print("Wicked! You have killed Bellatrix Lestrange.")
            time.sleep(2)
            movement_handler5()
    else:
        print("Well, you are losing a battle.")
        exit()


def movement_handler5():
    """
    The function is used for third part of second stage. This is a riddle stage where Input function
    will ask player for the correct answer to open the second stage door. If player didn't give the correct answer,
    While loop will help player to give another chance to correctly solve the riddle, if not, player will lose the game.
    """
    for statement in data['move5']:
        print(statement)
        time.sleep(1)
    ans = input("> ")
    if ans == 'onion':
        print("You are scared and door slowly opens....")
        last_level()
    while ans != 'onion':
        print("Incorrect answer, try again one more time!")
        ans = input("> ")
        while ans != 'onion':
            print("Hard Luck! you have lost it !")
            exit()
            break

### second stage of chambers of secrets
def level2():
    movement_handler3()
    time.sleep(2)
    prompt()
    time.sleep(2)
    movement_handler4()

###third stage of chambers of secrets
def last_level():
    """
    This function is last stage of the game, where voldemort encounter player.
    The Input function will help user to choose between the attack and healing potion.If player chooses attack
    voldemort's and players both health will be affected and displayed using print function.
    Player can choose heal potion to gain some health. While and Conditional statements are used for that for players
    to keep in loop.
    """
    for statement in data['last_level']:
        print(statement)
        time.sleep(1)
    game_running = True
    chances = 0
    while game_running:
        player_won, monster_won = False, False

        print("Select spell to cast :")
        print('1. Expecto-Patronum')
        print('2. Healing Potion')

        player_choice = input(">  ")
        if player_choice == "1":
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0:
                    monster_won = True
            print("Voldemort's Health - {0}\nYour Health - {1}".format(monster['health'], player['health']))

        elif player_choice == '2':
            if chances > 2:
                print("your 3 Healing Potions are over.")
            else:
                player['health'] = player['health'] + player['heal']
                monster['health'] = monster['health'] + monster['heal']
                player['health'] = player['health'] - monster['attack1']
                chances += 1
                print("You are healed")
        else:
            print("Invalid input")
        if player_won:
            game_running = False
            print("Congratulations! you have killed Voldemort and saved Harry!")
        elif monster_won:
            game_running = False
            print("Sorry Voldemort killed you, better luck next time!")


def player_move_level2():
    """
    This a general function used in second and third stage of the game.
    It takes input from the player using Input function and asks player which door they would like to go to.
    """
    ask = "Which door you would like to go to?(1,2 or 3)\n"
    dest = input(ask)
    print('You are moving towards Door number {0}'.format(p.number_to_words(dest)))


def player_move():
    """
    This function is used for first stage of the game. It takes input from the player using Input function
    and asks player which door they would like to go to. As per the selection it will directly takes player to
    the first stage's game task.
    """
    prompt()
    ask = "Which door you would like to go to?(1,2 or 3)\n"
    dest = input(ask)
    print('You are moving towards Door number {0}'.format(p.number_to_words(dest)))
    time.sleep(2)
    movement_handler1()



def prompt():
    """
    This function asks player what they want to do and for that it takes input from the player with Input function.
    It gives there options to player to choose, walk, move and quit.
    Quit helps player to immediately quit the game if they dont want to play anymore.
    Walk and move will let player continue the game.
    """
    print("What would you like to do? ( walk, quit)\n")
    action = input("> ")
    acceptable_actions = ['walk']
    while action.lower() in acceptable_actions:
        print("You are walking towards the doors...\n")
        time.sleep(2)
        print("Woman's Voice - You have only one chance to survive... choose wisely!!")
        time.sleep(2)
        break
    if action.lower() in ['quit']:
        sys.exit()
    elif action.lower() in ['run']:
        print("You are really running away...Voldemort wins! ")
        sys.exit()
    else:
        print(" ")

######set up of the game
def main():
    pyfiglet.figlet_format(data['game_name'])
    result = pyfiglet.figlet_format("Voldemort's\n Revenge")
    print(result)
    print(data['welcome_msg'])
    pygame.mixer.init()
    pygame.mixer.music.load("harry_potter_theme.mp3")
    pygame.mixer.music.play()
    title_screen()
    time.sleep(2)

    # WAND SELECTION
    print(data["print2"]["text"])
    time.sleep(2)
    print(data["welcome_opts"])
    wood = input(">>>")
    print(WOOD_MAPPING[wood.lower()])
    time.sleep(3)

    # SORTING HAT
    print(data['print3']['text'])
    time.sleep(3)

    print('Do you pride yourself on your-')
    print('\n'.join(str(k) for k in HOUSE_LIST))
    trait = input(" ").lower()
    house = HOUSE_MAPPING[trait.lower()]
    print('Congratulations on being sorted into {0}'.format(house))
    time.sleep(2)
    print(data['print4']['text'])
    time.sleep(5)

    answer = input("Would you like to play? (yes or no)")
    if answer == "yes":
        print(data['print5']['text'])
        player_move()
    else:
        print("You have missed the great chance to destroy you know who.")
        exit()


if __name__ == "__main__":
    main()
