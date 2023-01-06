import time

def help():
    print("                                                                  \n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n"
    "                            < COMMANDS >                              \n\n"
    "examine  \tObserve an object in more detail. \n"
    "take  \t\tAdd an object to your INVENTORY. \n"
    "drop  \t\tRemove an object from your INVENTORY. \n"
    "open  \t\tOpen something. \n"
    "push  \t\tPush an object. \n"
    "pull  \t\tPull an object. \n"
    "turn  \t\tRotate an object. \n"
    "feel  \t\tTouch an object to determine an its texture. \n"
    "smell  \t\tSmell object. \n"
    "wait  \t\tDo not do anything. \n"
    "talk to  \tCoverse with someone.\n"
    "inventory \tOpen your inventory. \n"
    "\n"
    "help \t\tDisplay the Help Menu. \n"
    "quit \t\tLeave the game at any point and return to the menu."
    "\n\n"
    "Make sure to use lowercase for commands. "
    "\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

def about():
    print("Techno World is a text-based adventure game or interactive fiction \n"
    "(if) that was created by Kishan Kumaran Thanikasalam in 2020. It is a fun\n"
    "and exciting adventure that is entertaining and breathtaking. People of  \n"
    "all ages will find it exhilerating and be amazed at the wonders concealed\n"
    " in the game.                                                            \n")

query_help = ["help", "Help", "HELP"]
query_about = ["about", "About", "ABOUT"]
query_play = ["play", "Play", "PLAY"]
query_ok = ["ok", "Ok", "OK"]
query_yes = ["yes", "Yes", "YES", "y", "Y"]
query_no = ["no", "No", "NO", "n", "N"]
query_quit = ["quit", "Quit", "QUIT"]
query_inventory = ["inventory", "Inventory", "INVENTORY"]

option_a = ["A", "a"]
option_b = ["B", "b"]
option_c = ["C", "c"]
option_d = ["D", "d"]

inventory = []

def intro():
    print("                                                                     \n"
    "    __________    _____     ______   ___________   _________     _________ \n"
    "   /___   ___/   /     \   /     /  /___   ____/  /  __    /    /  ____  / \n"
    "      /  /      /       \ /     /      /  /      /  /_/   /    /  /   / /  \n"
    "     /  /      /    /\         /      /  /      /      __/    /  /   / /   \n"
    "  __/  /__    /    /  \       /      /  /      /   /\  \_    /  /___/ /    \n"
    " /_______/   /____/    \_____/      /__/      /__ /  \__/   /________/     \n")
    time.sleep(2)
    print("You find yourself inside a small room with an overhead light and a \n"
    "window. There is also a table and a poster. Try to interact with the     \n"
    "objects around you.                                                      \n")

commands = {}
commands["examine_it"] = "examine"
commands["take_it"] = "take"
commands["drop_it"] = "drop"
commands["open_it"] = "open"
commands["push_it"] = "push"
commands["pull_it"] = "pull"
commands["turn_it"] = "turn"
commands["feel_it"] = "feel"
commands["smell_it"] = "smell"
commands["wait_for_it"] = "wait"
commands["talk_to_it"] = "talk"

objects_intro = {}
objects_intro["light"] = "light"
objects_intro["floor"] = "floor"
objects_intro["ceiling"] = "ceiling"
objects_intro["wall"] = "wall"
objects_intro["window"] = "window"
objects_intro["door"] = "door"
objects_intro["poster"] = "poster"
objects_intro["table"] = "table"

def table_intro():
    print("Do you wish to take the key?")
    time.sleep(1)
    key = input(">>> ")
    if key in query_no:
        print("OK")
    elif key in query_yes:
        inventory.append("key")
        print("The key has been added to your inventory.")
    else:
        print("You cannot do that")

def command_identifier_intro():
    while True:
        answer = input(">>> ")
        words = answer.split()
        if "examine" in words:
            if "light" in words:
                print("A perfectly normal filament light bulb.")
                time.sleep(1)
                continue
            elif "floor" in words:
                print("A soft patterned carpet.")
                time.sleep(1)
                continue
            elif "ceiling" in words:
                print("A plain ceiling.")
                time.sleep(1)
                continue
            elif "wall" in words:
                print("White, unassuming walls.")
                time.sleep(1)
                continue
            elif "window" in words:
                print("A rectangular glass window.")
                time.sleep(1)
                continue
            elif "door" in words:
                print("A large wooden door.")
                time.sleep(1)
                continue
            elif "poster" in words:
                print("                                                       \n"
                " ___________________________________________________________ \n"
                "|                                                           |\n"
                "| Welcome to the introductory stage of Techno World!        |\n"
                "| Here you will learn how to use basic commands to discover |\n"
                "| new places and items. Try to interact with the objects    |\n"
                "| around you. Once you are ready, go through the door.      |\n"
                "|                                                           |\n"
                "|                                                           |\n"
                "|                                        ~ Techno Wizard    |\n"
                "|___________________________________________________________|\n")
                time.sleep(1)
                continue
            elif "table" in words:
                if "key" in inventory:
                    print("A large wooden table.")
                elif "key" not in inventory:
                    print("A large wooden table with a small metal key gleaming on it.")
                    table_intro()
                time.sleep(1)
            else:
                print("You cannot examine that!")
                time.sleep(1)
                continue
        elif "take" in words:
            if "light" in words:
                print("You tried taking the light, but it was too hot. OUCH!")
                time.sleep(1)
                continue
            elif "floor" in words:
                print("You cannot take the floor!")
                time.sleep(1)
                continue
            elif "ceiling" in words:
                print("You cannot take the ceiling!")
                time.sleep(1)
                continue
            elif "wall" in words:
                print("Walls are not for taking, unfortunately.")
                time.sleep(1)
                continue
            elif "window" in words:
                print("You tried taking the window, but it was securely held.")
                time.sleep(1)
                continue
            elif "door" in words:
                print("You tried taking the door off its hinges, but alas to no "
                "avail.")
                time.sleep(1)
                continue
            elif "poster" in words:
                print("A valiant attempt, but to no use.")
                time.sleep(1)
                continue
            elif "table" in words:
                print("The table is too large and too heavy to take.")
                time.sleep(1)
                continue
            else:
                print("You cannot take that!")
                time.sleep(1)
                continue
        elif "drop" in words:
            if "key" in inventory:
                print("Are you sure you want to drop the key on the table?")
                key_drop = input(">>> ")
                if key_drop in query_no:
                    print("OK")
                elif key_drop in query_yes:
                    inventory.remove("key")
                    print("The key has been removed from your inventory.")
                else:
                    print("You cannot do that")
            else:
                print("You currently have no items in your inventory to drop.")
            continue
        elif "open" in words:
            if "light" in words:
                print("A light is not something that you open.")
                time.sleep(1)
                continue
            elif "floor" in words:
                print("You cannot open floors!")
                time.sleep(1)
                print("Well, at least not yet.")
                time.sleep(1)
                continue
            elif "ceiling" in words:
                print("The ceiling cannot be opened.")
                time.sleep(1)
                continue
            elif "wall" in words:
                print("No matter how many times you tried to open the wall, it did "
                "not budge.")
                time.sleep(1)
                continue
            elif "window" in words:
                print("You opened the window and felt a gust of cool air in your "
                "face.")
                time.sleep(1)
                continue
            elif "door" in words:
                if "key" in inventory:
                    print("You have unlocked the door!")
                    time.sleep(1)
                    print("Do you wish to leave the introduction?")
                    leave = input("Y/N: ")
                    if leave in query_yes:
                        inventory.remove("key")
                        time.sleep(1)
                        door_intro()
                    elif leave in query_no:
                        print("OK")
                        continue
                    else:
                        print("OK")
                        continue
                else:
                    print("The door is locked.")
            elif "poster" in words:
                print("The poster is already open on the wall.")
                time.sleep(1)
                continue
            elif "table" in words:
                print("Tables are not for opening.")
                time.sleep(1)
                continue
            else:
                print("You cannot open that.")
                time.sleep(1)
                continue
        elif "push" in words:
            if "light" in words:
                print("You cannot push the light.")
                time.sleep(1)
                continue
            elif "floor" in words:
                print("Pushing the floor does not seem to yield any outcome.")
                time.sleep(1)
                continue
            elif "ceiling" in words:
                print("The ceiling cannot be pushed.")
                time.sleep(1)
                continue
            elif "wall" in words:
                print("Pushing the wall does not seem to be worthwhile")
                time.sleep(1)
                continue
            elif "window" in words:
                print("You pushed the window and felt a gust of cool air in your "
                "face.")
                time.sleep(1)
                continue
            elif "door" in words:
                print("You cannot push the door, try pulling it.")
                time.sleep(1)
                continue
            elif "poster" in words:
                print("Pushing the poster is not an effective use of your time.")
                time.sleep(1)
                continue
            elif "table" in words:
                print("Pushing the table has no implication on the game.")
                time.sleep(1)
                continue
            else:
                print("You cannot push that.")
                time.sleep(1)
                continue
        elif "pull" in words:
            if "light" in words:
                print("You tried pulling the light, but nothing happened.")
                time.sleep(1)
                continue
            elif "floor" in words:
                print("Floor are not designed to be pulled.")
                time.sleep(1)
                continue
            elif "ceiling" in words:
                print("You cannot pull the ceiling.")
                time.sleep(1)
                continue
            elif "wall" in words:
                print("Pulling walls is not possible.")
                time.sleep(1)
                continue
            elif "window" in words:
                print("The window cannot be pulled, try pushing it.")
                time.sleep(1)
                continue
            elif "door" in words:
                if "key" in inventory:
                    print("You have unlocked the door!")
                    time.sleep(1)
                    print("Do you wish to leave the introduction?")
                    leave = input("Y/N: ")
                    if leave in query_yes:
                        inventory.remove("key")
                        time.sleep(1)
                        door_intro()
                    elif leave in query_no:
                        print("OK")
                        continue
                    else:
                        print("OK")
                        continue
                else:
                    print("The door is locked.")
            elif "poster" in words:
                print("Pulling the poster had no effect.")
                time.sleep(1)
                continue
            elif "table" in words:
                print("The table is too heavy to pull.")
                time.sleep(1)
                continue
            else:
                print("You cannot pull that.")
                time.sleep(1)
                continue
        elif "turn" in words:
            if "light" in words:
                print("You tried turning the light, but nothing happened.")
                time.sleep(1)
                continue
            elif "floor" in words:
                print("The floor cannot be turned.")
                time.sleep(1)
                continue
            elif "ceiling" in words:
                print("The ceiling is not something that you turn.")
                time.sleep(1)
                continue
            elif "wall" in words:
                print("Turning walls will not be in any way useful.")
                time.sleep(1)
                continue
            elif "window" in words:
                print("The window cannot be turned, try pushing it")
                time.sleep(1)
                continue
            elif "door" in words:
                print("The door cannot be turned, try opening it.")
                time.sleep(1)
                continue
            elif "poster" in words:
                print("You tried turning the poster, but nothing happened.")
                time.sleep(1)
                continue
            elif "table" in words:
                print("The table is too heavy to turn.")
                time.sleep(1)
                continue
            else:
                print("You cannot turn that.")
                time.sleep(1)
                continue
        elif "feel" in words:
            if "light" in words:
                print("HOT!")
                time.sleep(1)
                continue
            elif "floor" in words:
                print("A soft, cushioning carpet.")
                time.sleep(1)
                continue
            elif "ceiling" in words:
                print("You cannot reach the ceiling, unfortunately.")
                time.sleep(1)
                continue
            elif "wall" in words:
                print("Smooth and cold, like any normal wall should be.")
                time.sleep(1)
                continue
            elif "window" in words:
                print("Cool glass.")
                time.sleep(1)
                continue
            elif "door" in words:
                print("Smooth, wooden door.")
                time.sleep(1)
                continue
            elif "poster" in words:
                print("A glossy sheen on the poster.")
                time.sleep(1)
                continue
            elif "table" in words:
                print("A heavy sleek table.")
                time.sleep(1)
                continue
            else:
                print("You cannot feel that.")
                time.sleep(1)
                continue
        elif "smell" in words:
            if "light" in words:
                print("You cannot smell the light")
                time.sleep(1)
                continue
            elif "floor" in words:
                print("You took long lungfulls of the carpet's aroma.")
                time.sleep(1)
                continue
            elif "ceiling" in words:
                print("You cannot reach the ceiling.")
                time.sleep(1)
                continue
            elif "wall" in words:
                print("You breathed in the musky scent of the walls.")
                time.sleep(1)
                continue
            elif "window" in words:
                print("As expected, there was no evident smell to the window.")
                time.sleep(1)
                continue
            elif "door" in words:
                print("You inhaled the sharp essence of the wooden door.")
                time.sleep(1)
                continue
            elif "poster" in words:
                print("You whiffed the heady tang of the poster.")
                time.sleep(1)
                continue
            elif "table" in words:
                print("You observed the distinct aroma of the table.")
                time.sleep(1)
                continue
            else:
                print("You cannot smell that.")
                time.sleep(1)
                continue
        elif "wait" in words:
            print("Time passes.")
            continue
        elif "talk" in words:
            print("You can only talk to animate beings.")
            continue
        elif answer in query_quit:
            quit_q = print("Are you sure you want to quit and return to the "
            "menu?")
            quit_a = input("Y/N: ")
            if quit_a in query_yes:
                print("Thank you for playing Techno World.")
                time.sleep(1)
                title_screen()
            elif quit_a in query_no:
                continue
            else:
                print("Invalid Input!")
                continue
        elif answer in query_inventory:
            print("                                                          \n"
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n"
            "                          INVENTORY                             \n")
            for item in inventory:
                print(item)
            print("                                                          \n"
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
            time.sleep(1)
        elif answer in query_help:
            help()
        else:
            print("You cannot do that.")
            continue

def door_intro():
    print("You opened the door... ")
    time.sleep(2)
    print(" ... and as you step over the threshold, you marvel at the scenes  \n"
    "all around you. You gaze above at the pristine blue skies and below at   \n"
    "the vast sloping valleys gliding off into the horizon. Turning around,   \n"
    "you see a wizened old man in a crumpled blue gown and a crooked pointed  \n"
    "hat.")
    time.sleep(5)
    act_i()

def act_i():
    print("                                                                   \n"
    "        ________     ________     _________          __________          \n"
    "       /  __   /    /   ____/    /___   __/         /___   ___/          \n"
    "      /  /_/  /    /   /            /  /               /  /              \n"
    "     /  __   /    /   /            /  /               /  /               \n"
    "    /  / /  /    /   /____        /  /             __/  /__              \n"
    "   /__/ /__/    /________/       /__/             /_______/              \n")
    time.sleep(2)
    command_identifier_act_i()

def techno_wizard_dialogue_1():
    print("Techno Wizard: Hello there adventurer! You must be new around here \n"
          "               My name is Techno Wizard and I will be your         \n"
          "               instructor and companion during your travels in the \n"
          "               vast landscapes within Techno World! I believe that \n"
          "               you received my message on the poster in the        \n"
          "               introduction. If you have any questions you can ask \n"
          "               me now.                                             \n")
    time.sleep(5)
    while True:
        print("A - 'Who are you?'                                                 \n"
              "B - 'What is this place?'                                          \n"
              "C - 'Is that your real name?'                                      \n"
              "D - 'Thanks, that's all for now'                                   \n")
        answer = input(">>> ")
        if answer in option_a:
            print("You: Who are you?                                              \n")
            time.sleep(1)
            print("Techno Wizard: I am the Guardian of Techno World and I help    \n"
                  "               those that need it. If ever you need any help,  \n"
                  "               do not hesitate to ask me.                      \n")
            continue
        elif answer in option_b:
            print("You: What is this place?                                       \n")
            time.sleep(1)
            print("Techno Wizard: This is the blissful land where I reside,       \n"
                  "               filled with plants and animals of all kinds. It \n"
                  "               truly is a remarkable place.                    \n")
            continue
        elif answer in option_c:
            print("You: Is that your real name?                                   \n")
            time.sleep(1)
            print("Techno Wizard: Why of course! ... ")
            time.sleep(2)
            print("Techno Wizard: ... although, it is quite a strange one is it   \n"
                  "               not. Perhaps, I ought to change it.             \n")
            continue
        elif answer in option_d:
            print("You: Thanks, that's all for now.                               \n")
            time.sleep(1)
            print("Techno Wizard: My pleasure! Now if you have not any further    \n"
                  "               questions, we ought to move along ...           \n"
                  "               ... I have a lot to tell you.                   \n")
            break
        else:
            print("Invalid Input!")
            continue

def techno_wizard_dialogue_2():
    print("Techno Wizard: We are going to my house; ")
    #crates and Creevey

def command_identifier_act_i():
    while True:
        answer = input(">>> ")
        words = answer.split()
        if "examine" in words:
            if "man" in words:
                print("An elderly man wearing a strange outfit.")
                continue
            elif "sky" in words or "skies" in words:
                print("A vast bright blue sky.")
                continue
            elif "valleys" in words or "valley" in words:
                print("Steep interlocking spurs of giant hills.")
                continue
            elif "floor" in words:
                print("Grass.")
            elif "gown" in words:
                print("An ancient blue gown weathered by long use.")
                continue
            elif "hat" in words:
                print("An odd pointed hat that looks almost as old as him if  \n"
                "not older.")
                continue
            else:
                print("You cannot examine that.")
                continue
        elif "take" in words:
            if "man" in words:
                print("You cannot take the man.")
                continue
            elif "sky" in words or "skies" in words:
                print("You canot take the sky.")
                continue
            elif "valleys" in words or "valley" in words:
                print("You are not able to take the valleys.")
                continue
            elif "floor" in words:
                print("You cannot take the floor.")
                continue
            elif "gown" in words:
                print("You cannot take the man's gown.")
                continue
            elif "hat" in words:
                print("You cannot take the man's hat.")
                continue
            else:
                print("You cannot take that.")
                continue
        elif "drop" in words:
            print("You have no items in your inventory.")
            continue
        elif "open" in words:
            print("You cannot open that.")
            continue
        elif "push" in words:
            print("You cannot push that.")
            continue
        elif "pull" in words:
            print("You cannot pull that.")
            continue
        elif "turn" in words:
            print("You cannot turn that.")
            continue
        elif "feel" in words:
            if "floor" in words:
                print("Soft grass.")
                continue
            else:
                print("You cannot feel that.")
                continue
        elif "smell" in words:
            if "grass" in words:
                print("Musty and deep.")
                continue
            else:
                print("You cannot smell that.")
                continue
        elif "wait" in words:
            print("Time passes.")
            continue
        elif "talk" in words:
            if "man" in words:
                print("You approach the strangely dressed man and he looks up \n"
                "at you...")
                time.sleep(1)
                techno_wizard_dialogue_1()
                time.sleep(2)
                print("                                                       \n"
                "The Techno Wizard abruptly walks away in the direction of a  \n"
                "small hut that you could have sworn was not there when you   \n"
                "first came here. He leaves you no choice but to follow him...\n")
                time.sleep(1)
                techno_wizard_dialogue_2()
            else:
                print("You can only talk to animate beings.")
        elif answer in query_quit:
            quit_q = print("Are you sure you want to quit and return to the "
            "menu?")
            quit_a = input("Y/N: ")
            if quit_a in query_yes:
                print("Thank you for playing Techno World.")
                time.sleep(1)
                title_screen()
            elif quit_a in query_no:
                continue
            else:
                print("Invalid Input!")
                continue
        elif answer in query_inventory:
            print("                                                          \n"
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n"
            "                          INVENTORY                             \n")
            for item in inventory:
                print(item)
            print("                                                          \n"
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
            time.sleep(1)
        elif answer in query_help:
            help()
        else:
            print("You cannot do that.")
            continue


def title_screen():
    print("                                                                   \n"
    "                  Welcome to ...                                         \n")
    time.sleep(2)
    print("                                                                   \n"
    "************************************************************************ \n"
    "   _______    ______     ______     ___  ___    ___    ____     _______  \n"
    "  /__  __/   /  ___/    /  ___/    /  / /  /   /   \  /   /    / ___  /  \n"
    "    / /     /  /___    /  /       /  /_/  /   /     \/   /    / /  / /   \n"
    "   / /     /   ___/   /  /       /  _    /   /  /\      /    / /  / /    \n"
    "  / /     /   /___   /  /___    /  / /  /   /  /  \    /    / /__/ /     \n"
    " /_/     /_______/  /______/   /__/ /__/   /_ /    \ _/    /______/      \n"
    "                                                                         \n"
    "        __  __  ___    _______    _________    ___       _____           \n"
    "       / / / / /  /   / ___  /   /  __    /   /  /      / _   \          \n"
    "      / /_/ /_/  /   / /  / /   /  /_/   /   /  /      / / \  /          \n"
    "     /   ___    /   / /  / /   /      __/   /  /      / /  / /           \n"
    "    /   /  /   /   / /__/ /   /   /\  \_   /  /___   / /__/ /            \n"
    "   /___/  /___/   /______/   /__ /  \__/  /______/  /______/             \n"
    "                                                                         \n"
    "************************************************************************ \n")
    time.sleep(1)
    print("                                                                   \n"
    "   ~~~~~~~~~~~~~~~~~~~~~ A game by Kishan K ~~~~~~~~~~~~~~~~~~~~~        \n")
    time.sleep(1)
    print("                                                                   \n"
    "                          -    Play    -                                 \n"
    "                          -    Help    -                                 \n"
    "                          -    About   -                                 \n"
    "                      Copyright Kishan K 2020                            \n")

def menu():
    while True:
        time.sleep(1)
        answer_menu = input(">>> ")
        if answer_menu in query_help:
            help()
            time.sleep(2)
            ok = input("Enter 'ok' to continue: ")
            if ok in query_ok:
                title_screen()
            else:
                ok2 = input("Enter 'ok' only: ")
                if ok2 in query_ok:
                    title_screen()
                else:
                    print("Automatic 'ok' initiated... ")
                    time.sleep(2)
                    print("Automatic 'ok' complete.")
                    title_screen()
        elif answer_menu in query_about:
            about()
            time.sleep(1)
            ok = input("Enter 'ok' to continue: ")
            if ok in query_ok:
                title_screen()
            else:
                ok2 = input("Enter 'ok' only: ")
                if ok2 in query_ok:
                    title_screen()
                else:
                    print("Automatic 'ok' initiated... ")
                    time.sleep(2)
                    print("Automatic 'ok' complete.")
                    title_screen()
        elif answer_menu in query_play:
            intro()
            time.sleep(2)
            command_identifier_intro()
        else:
            print("Invalid input!")
            title_screen()

title_screen()
menu()
