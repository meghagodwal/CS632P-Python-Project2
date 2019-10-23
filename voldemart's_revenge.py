import pyfiglet
import time
import random
import sys
import os
import textwrap
import cmd

player ={'attack':10, 'heal': 20, 'health': 100}
monster = {'name': 'Voldemort','attack':12, 'health':100 }


############### Welcoming the player ################
def title_screen_selection():
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
    print('###################################')
    print('#  Welcome to Voldemorts Revenge! #')
    print('###################################')
    print('-Use walk,move to move             ')
    print('-Type your commands to do them     ')
    print('-Good luck and have fun!           ')
    title_screen_selection()

def title_screen():
    os.system('clear')
    print('#################################')
    print('            -Play-               ')
    print('            -Help-               ')
    print('            -Quit-               ')
    print('#################################')
    title_screen_selection()

def setup_game():
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
print("")
title_screen()
time.sleep(2)

print2 = "We are pleased to inform you that you have been accepted into Hogwarts School of Witchcraft and Wizardry.\n"
for character in print2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

time.sleep(2)

######################## Wand selection ###########################
print3= "You travel to Diagon Alley to do your school shopping.\n You reach to Ollivanders to get your wand."
for character in print3:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
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

print4 = "You leaves your home to catch the Hogwarts Express from King's Cross railway station's secret Hogwarts platform, Platform ​9 3⁄4."
for character in print4:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
print5 = "\nArriving at the station, you met with harry and then led by Hagrid onto boats which they sail to the castle of Hogwarts."
for character in print5:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
print6 = "\nThe new students are greeted at the castle door by Professor Minerva McGonagall, who tells them they will soon be sorted into their houses.\n  All Hogwarts students live in one of four residences: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin."
for character in print6:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
print7 = "\nYou have taken to the common hall for the Sorting Hat ceremony to deceide which house you are going to be a part of."
for character in print7:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
print("")


############################# Sorting Hat ########################################
time.sleep(3)
print('Professor McGonagall: Hello, and welcome to the sorting of Hogwarts School.')
time.sleep(3)
print8 = 'please come forward and place the hat onto your head.'
for character in print8:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(2)
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

############################voldemort's entry####################################

print9 = "You and Harry Potter have become good friends and you got to know how Lord Voldemort have killed Harry's parents."
for character in print9:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
print10 = "\nYou and Harry been observing weird things happeing around Hogwarts and you realise that Voldemort is alive."
for character in print10:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
print11 = "\nHarry and you have decided to kill him but while going ahead, Harry have been captured by Lord Voldemort! It's up to you to rescue him now."
for character in print11:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
print("")
time.sleep(5)

###################Level 1 of chambers of Sceret#################
def movement_handler1():
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

######################Level 2 of Chambers of Secret #######################
def movement_handler3():
    time.sleep(2)
    print("After unlocking the mysterious door, you walk in to find Harry...")
    time.sleep(2)
    print("\nYou again hear woman's voice....")
    time.sleep(1)
    print("Congratulations! you have successfully opened first door...\n and you reached to second stage of Chambers of secrets...")
    time.sleep(2)
    print("\nWould you like to continue? (yes or no)\n")
    answer= input("> ")
    if answer == "yes":
        print("Woman's Voice - answer this riddle and you are through to the next level!\n")
        time.sleep(2)
        print("I roam the woods of Hogwarts school.\n And my coat is a lovely white,\n But don't you dare, try to drink my blood,\n Or you'll be cursed for life.\n Who am I?\n")
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
    print("... after a long survival you see a prophecy lying there..")
    time.sleep(2)
    print("You begin to think what that must be......")
    time.sleep(2)
    print("the prophecy says - A son cruelly banished\nDespair of the daughter\nReturn, great avenger\nWith wings from the water.")
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


def player_move_level2():
    ask = "Which door you would like to go to?(1,2 or 3)\n"
    dest = input(ask)
    if dest in ['3']:
        print("You are moving towards Door number three.\n")

    elif dest in ['1']:
        print("You are moving towards Door number one.\n")

    else:
        print("You are moving straight to Door number two.\n")




######################players move for doors########################
def player_move():
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

######################first setup to build it#########################
def prompt():
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



####################extended story ans asking player if they wants to go along################
answer=input("Would you like to play? (yes or no)")
if answer == "yes":
    print("As Harry has gone, you are searching ways to start hunting Lord Voldemort.\n Your friend Neville suggested you to check with Hagrid as he might know something. ")
    print("")
    time.sleep(2)
    print("\nHagrid told you that he saw someone with a crooked face and asked him the about the directions for prophecy tower.\n You realise that you should go their and check if you get something.")
    print("")
    time.sleep(2)
    print("As you are walking towards the prophecy tower, your skin begins to tingle...\n")
    print("There is a pitch dark room and you hear a woman's voice to welcoming you in the chamber of secrets..\n")
    time.sleep(2)
    print("Woman's Voice: Hi, Welcome to the Chamber of Secrets.\n You have three doors in front of you to choose it inorder to proceed further.")
    time.sleep(2)
    player_move()
else:
    print("You have missed the great chance to destroy you know who.")
    exit()










