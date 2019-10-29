import pyfiglet
import time
import random
import sys
import os
import textwrap
import cmd
import pygame
from pygame.locals import*
import json


with open('game-text.json', 'r') as f:
    data = json.load(f)

player ={'attack':10, 'heal': 20, 'health': 100}
monster = {'name': 'Voldemort','attack':12, 'health':100 }

def title_screen_selection():
    """
    This function helps player to decide whether you want to play,need help with the moves or quit the game.
    The function is taking input from the player and based on that conditional loops will work.
    If user types other command than play, help and quit, it will show a error message asking player to
    type valid command.
    """
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please Enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
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

result=pyfiglet.figlet_format("Voldemort's\n Revenge")
print(result)
print("Welcome to Voldemort's Revenge.")
pygame.mixer.init()
pygame.mixer.music.load("harry_potter_theme.mp3")
pygame.mixer.music.play()
print("")
title_screen()
time.sleep(2)

#WAND SELECTION
print(data["print2"]["text"])
time.sleep(2)
print("\n")
print("Welcome to Ollivander's!")
time.sleep(0.2)
print("")
print("Are you most:")
print("a: Kind and Generous")
print("b: Tenacious")
print("c: A good leader")
print("d: Full of life")
print("e: Knowledgeable")
print("f: Strong and flexible")
print("g: Confident and Optimistic")
print("")
wood=input(">>>")
print("")
if wood.lower() == "a":
    print("You recieve an Ash Wand, 13 4/17 inches, with a Unicorn Tail Hair core.")
    print("")
    print("Processing...")
    time.sleep(3)
elif wood.lower() == "b":
    print("You receive an Ivy Wand, 9 2/9 inches, with a Dragon Heartstring core.")
    print("")
    print("Processing...")
    time.sleep(3)
elif wood.lower() == "c":
    print("You receive a Holly Wand, 11 1/2 inches, with a Phoenix Feather core.")
    print("")
    print("Processing...")
    time.sleep(3)
elif wood.lower() =="d":
    print("You receive a Birch Wand, 10 3/4 inches, with a Dragon Heartstring core.")
    print("")
    print("Processing...")
    time.sleep(3)
elif wood.lower() == "e":
    print("You receive a Reed Wand, 9 9/10 inches, with a Phoenix Feather core.")
    print("")
    print("Processing...")
    time.sleep(3)
elif wood.lower() == "f":
    print("You receive a Willow Wand, 8 7/9 inches, with a Unicorn Tail Hair core")
    print("")
    print("Processing...")
    time.sleep(3)
elif wood.lower() == "g":
    print("You receive an Oak Wand, 16 inches, with a Unicorn Tail Hair core.")
    print("")
    print("Processing...")
    time.sleep(3)

#SORTING HAT
print(data['print3']['text'])
print("")
time.sleep(3)
house=["Benevolence","Courageousness","Knavishness","Intelligence"]
print('Do you pride yourself on your-')
print('a. Benevolence')
print('b. Courageousness')
print('c. Knavishness')
print('d. Intelligence')
trait=input(" ").lower()
if trait.lower()=="a":
    house="Hufflepuff!"
elif trait.lower()=="b":
    house="Gryffindor!"
elif trait.lower()=="c":
    house="Slythrin!"
elif trait.lower()=="d":
    house="Ravenclaw!"
print('Congratulations on being sorted into '+ house)

time.sleep(2)
print(data['print4']['text'])
print(" ")
time.sleep(5)

def movement_handler1():
    """
    This function is the first stage of the game loop.
    Input function is used to take input from the player what spells they want to cast.
    Conditional statements is used to decide what happens if they use these spells.
    And  while loop is used to provide another life to player if they answer incorrectly.
    """
    print("You head down the path")
    time.sleep(2)
    print("There is a Dark room and you see a giant man coming across you.")
    time.sleep(2)
    print("Your skin begins to tingle....")
    print()
    time.sleep(2)
    print("You have come across a Troll... What spell do you perform to save yourself?")
    time.sleep(1)
    print("You can choose spells :Expelliarmus, Stupefy, Incendio, Levicorpus\n")
    time.sleep(1)
    ans = input("> ")
    if ans in ["Expelliarmus", "Incendio"]:
        print("You have disarmed the Troll, you need to cast the stronger spell to kill him.")
    while ans not in ["Stupefy", "Levicorpus"]:
        print("Try again one more time, you have last chance to kill him.")
        ans = input("> ")
        while ans not in ["Stupefy","Levicorpus"]:
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
    time.sleep(2)
    print("After your survival from Troll, you are trying to unlock the door.\n")
    time.sleep(2)
    print("And you see bunch of keys flying in the room, select the appropriate key to go ahead.\n")
    print("Hint- There are 10 keys and you have to find the correct one.")
    correct_num=random.randint(1,10)
    keep_guessing='true'
    while keep_guessing == "true":
        guess = int(input("Enter the number key:"))
        if guess == correct_num:
            print("Sweet! You have amazingly figured the correct key.")
            level2()
            keep_guessing = 'false'
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
    time.sleep(2)
    print("After unlocking the mysterious door, you walk in to find Harry...")
    time.sleep(2)
    print("\nYou again hear woman's voice....")
    time.sleep(1)
    print("Congratulations! you have successfully opened first door...\n and you reached to second stage\
     of Chambers of secrets...")
    time.sleep(2)
    print("\nWould you like to continue? (yes or no)\n")
    answer= input("> ")
    if answer == "yes":
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
    time.sleep(2)
    print("As you are walking towards the next door.... you hear footsteps approaching...")
    time.sleep(2)
    print("\nThey're getting louder and louder.\n You can feel them almost beside you.")
    time.sleep(2)
    print("And suddenly you see Bellatrix Lestrange holding the prophecy.\n Would you like to continue?(yes or no)\n")
    answer= input("> ")
    if answer == 'yes':
        print("You try to hide to attack her...")
        time.sleep(2)
        print("Which spell you would like to cast?\n")
        print("You can choose spells :Expectopatronum, Crucio, Imperio, Sectumsempra\n")
        spell = input("> ")
        if spell in ["Imperio"]:
            print("You are only able to disarm her, cast some stronger spell to kill her.\n")
        while spell not in ["Expectopatronum", "Crucio","Sectumsempra"]:
            print("Try again one more time!")
            spell = input("> ")
            while spell not in ["Expectopatronum", "Crucio","Sectumsempra"]:
                print("Tough! you did your best but you didnt survive.")
                exit()
                break
        else:
            print("Wicked! You have killed Bellatrix Lestrange.")
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
    print("... after a long survival you see a prophecy lying there..")
    time.sleep(2)
    print("You begin to think what that must be......")
    time.sleep(2)
    print("the prophecy says - A son cruelly banished\nDespair of the daughter\nReturn, great avenger\nWith wings\
     from the water.")
    time.sleep(2)
    print("You gasped.........and start moving ahead")
    time.sleep(2)
    print("You approach the door, surprisingly, it's locked.")
    time.sleep(2)
    print("you hear a voice - Take off my skin - I won't cry, but you will! What am I?")
    answer = input("> ")
    if answer == 'onion':
        print("You are scared and door slowly opens....")
        last_level()
    while answer!= 'onion':
        print("Incorrect answer, try again one more time!")
        answer = input("> ")
        while answer != 'onion':
            print("Hard Luck! you have lost it !")
            exit()
            break
    else:
        print("goodbye! you lost...")
        exit()

def level2():
    movement_handler3()
    prompt()
    movement_handler4()

def last_level():
    """
    This function is last stage of the game, where voldemort encounter player.
    The Input function will help user to choose between the attack and healing potion.If player chooses attack
    voldemort's and players both health will be affected and displayed using print function.
    Player can choose heal potion to gain some health. While and Conditional statements are used for that for players
    to keep in loop.
    """
    time.sleep(2)
    print("You start to move ahead through the door...")
    time.sleep(2)
    print("Woman's voice - You're about to face your final challenge.")
    time.sleep(2)
    print("As you entered the room it's trashed. Chunks of metal everywhere. You see Harry's body lying on the ground.")
    time.sleep(2)
    print("You run to him to wake him up... but he seemed cursed")
    time.sleep(2)
    print("Suddenly.. you hear footsteps approaching towards you")
    time.sleep(2)
    print("Voldemort - Well, well.. so you are here to save Harry")
    print("Voldemort - so are you ready to face your utmost fear?")
    time.sleep(2)
    print("..............what u did to harry?")
    time.sleep(2)
    print("Voldemort - well you dont worry about him by the time I finish with you I am going to kill him as well.")
    time.sleep(2)
    print("........ you cant.. I am going to kill you!!!")
    time.sleep(3)
    print("you put out your wand and start attacking Voldemort")
    game_running = True
    while game_running == True:
        player_won = False
        monster_won = False

        print("Select spell to cast :")
        print('1. Expecto-Patronum')
        print('2. Healing Potion')

        player_choice = input(">  ")
        if player_choice == "1":
            monster['health'] = monster['health'] - player['attack']
            if monster['health']<=0:
                player_won = True
                print("Congratulations! You have killed Voldemort and saved Harry!")
            else:
                player['health'] = player['health'] - monster['attack']
                if player['health']<=0:
                    monster_won = True
            print("Voldemort's Health -")
            print(monster['health'])
            print("Your Health -")
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            print("Heal player")
        else:
            print("Invalid input")
        if player_won == True or monster_won == True:
            game_running = False
            print("Congratulations!")


def player_move_level2():
    """
    This a general function used in second and third stage of the game.
    It takes input from the player using Input function and asks player which door they would like to go to.
    """
    ask = "Which door you would like to go to?(1,2 or 3)\n"
    dest = input(ask)
    if dest in ['3']:
        print("You are moving towards Door number three.\n")

    elif dest in ['1']:
        print("You are moving towards Door number one.\n")

    else:
        print("You are moving straight to Door number two.\n")

def player_move():
    """
    This function is used for first stage of the game. It takes input from the player using Input function
    and asks player which door they would like to go to. As per the selection it will directly takes player to
    the first stage's game task.
    """
    prompt()
    ask = "Which door you would like to go to?(1,2 or 3)\n"
    dest = input(ask)
    if dest in ['3']:
        print("You are moving towards Door number three.\n")
        movement_handler1()
    elif dest in ['1']:
        print("You are moving towards Door number one.\n")
        movement_handler1()
    else:
        print("You are moving straight to Door number two.\n")
        movement_handler1()

def prompt():
    """
    This function asks player what they want to do and for that it takes input from the player with Input function.
    It gives there options to player to choose, walk, move and quit.
    Quit helps player to immediately quit the game if they dont want to play anymore.
    Walk and move will let player continue the game.
    """
    print("What would you like to do? ( walk, move, quit)\n")
    action= input("> ")
    acceptable_actions = ['walk','move']
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




answer=input("Would you like to play? (yes or no)")
if answer == "yes":
    print(data['print5']['text'])
    player_move()
else:
    print("You have missed the great chance to destroy you know who.")
    exit()










