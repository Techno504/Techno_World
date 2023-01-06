import time
python3 -m pip install -U pygame --user

def about():
    print("Techno World is a text-based adventure game or interactive fiction \n"
    "(if). You can choose how to continue the story and make it yours! There \n"
    "are a few basic commands that you may need to use: \n"
    "\n\n"
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
    "\n"
    "quit \t\tleave the game at any point and return to the menu."
    "\n\n"
    "Make sure to use lowercase for commands. "
    "\n")

query_about = ["about", "About", "ABOUT"]
query_play = ["play", "Play", "PLAY"]
query_ok = ["ok", "Ok", "OK"]
query_yes = ["yes", "Yes", "YES", "y", "Y"]
query_no = ["no", "No", "NO", "n", "N"]
query_quit = ["quit", "Quit", "QUIT"]

def intro():
    print("You find yourself inside a small room with an overhead light and a \n"
    "window. There is also a table and a poster. Try to interact with the \n"
    "objects around you. Remember, when in doubt, examine more. \n")

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
                print("Welcome to the introductory stage of Techno World! \n"
                "Here you will learn how to use basic commands to discover \n"
                "new places and items. Try to interact with the objects around you. \n"
                "Once you are ready, go through the door. \n")
                time.sleep(1)
                continue
            elif "table" in words:
                print("A large wooden table.")
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
                print("You opened the window and felt a gust of hot wind in your "
                "face.")
                time.sleep(1)
                continue
            elif "door" in words:
                print("Do you wish to leave the introduction?")
                leave = input("Y/N: ")
                if leave in query_yes:
                    time.sleep(1)
                    door_intro()
                elif leave in query_no:
                    print("OK")
                    continue
                else:
                    print("OK")
                    continue
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
                print("You pushed the window and felt a gust of hot wind in your "
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
                print("Do you wish to leave the introduction?")
                leave = input("Y/N: ")
                if leave in query_yes:
                    time.sleep(1)
                    door_intro()
                elif leave in query_no:
                    print("OK")
                    continue
                else:
                    print("OK")
                    continue
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
                title_screen()
            elif quit_a in query_no:
                continue
            else:
                print("Invalid Input!")
                continue
        else:
            print("You cannot do that.")
            continue

def door_intro():
    print("You opened the door ")

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
    "                          -    About   -                                 \n"
    "                          -   Credits  -                                 \n")

def menu():
    while True:
        time.sleep(1)
        answer_menu = input(">>> ")
        if answer_menu in query_about:
            about()
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
        elif answer_menu in query_play:
            intro()
            time.sleep(2)
            command_identifier_intro()
        else:
            print("Invalid input!")
            title_screen()

title_screen()
menu()
