import time
import random

'''
Fixed Log:
    Command fixed: Walking, checkHealth, checkWeapon, checkBag, collect_item, attack, run_away
    Menu_fixed: battle_menu

WIP log:
    navigation_menu
'''

# color chart
cRed = "\x1b[31m"
cGreen = "\x1b[32m"
cYellow = "\x1b[33m"
cBlue = "\x1b[34m"
cWhite = "\x1b[37m"
cEnd = "\x1b[0m"


start_item = ['Potion', 'Bread', 'Cookie']
special_item = ['Mega potion', 'Elixir', 'Bandage']
start_weapon = ['Fork', 'Cooking pan', 'Worn dagger']
special_weapon = ['Bow & Arrow', 'Spear', 'Axe', 'Excalibur']
# enemyHP = {'Dog': 10, 'Bandit': 30, 'Zombie': 60, 'Dragon': 80}
enemyHP = {'Dog': 1, 'Bandit': 1, 'Zombie': 1, 'Dragon': 1} # for debugging use only!
enemyAP = {'Dog': 5, 'Bandit': 10, 'Zombie': 15, 'Dragon': 15}
enemy_type = ['Dog', 'Dog', 'Dog', 'Dog', 'Dog', 'Dog', 'Bandit',
              'Bandit', 'Bandit', 'Bandit', 'Zombie', 'Zombie']

itemDict = {
    'Elixir': 50,
    'Mega potion': 10,
    'Bandage': 7,
    'Potion': 5,
    'Bread': 3,
    'Cookie': 2
    }

weaponDict = {
    'Fork': 2,
    'Cooking pan': 4,
    'Worn dagger': 5,
    'Bow & Arrow': 8,
    'Spear': 10,
    'Axe': 15,
    'Excalibur': 20
    }

hero = {
    'name': 'NoName',
    'hp': 0,
    'bag': 'empty',
    'weapon': 'empty',
    'story': 'intro',
    'option': 'empty',
    'turn': 0,
    'enter_counter': 0,
    'in_battle': 0,
    'enemy': 'empty',
    'enemy_health': 0,
    'kill': 0,
    'escape': 0,
    't_damage': 0,
    't_attack': 0,
    't_battle': 0,
    "sleep_counter": 0,
    'finish': ''
    }

hero['hp'] = random.randint(20, 80)
hero['bag'] = start_item[random.randint(0, len(start_item) - 1)]
hero['weapon'] = start_weapon[random.randint(0, len(start_weapon) - 1)]


def print_pause(message, delay, color):  # FIXED
    print(color, message, '\x1b[0m')
    time.sleep(delay - delay + 0.1)  # for debugging use only!
    # time.sleep(delay - delay + 0.5)


def print_option(hero):  # FIXED
    print_pause("What you decide to do, next?", 1, cBlue)
    print_pause("[1] Check your health stats | [2] Check weapon | [3] Check backpack", 0, cWhite)
    print_pause(f"{hero['option']}", 0, cWhite)


def invalid_selection():  # FIXED
    print_pause(f"\n >>> Invalid option selected. Please try again.\n", 0, cRed)


def checkHealth(hero):  # FIXED
    print(cGreen + "\n >>> Your current health is [" + cYellow + f"{hero['hp']}HP" + cGreen + f"].\n" + cEnd)
    print_option(hero)


def checkWeapon(hero):  # FOXED
    print(cGreen + f"\n >>> You are equiped with a [" + cYellow + f"{hero['weapon']} {weaponDict[hero['weapon']]}AP" + cGreen + "].\n" + cEnd)
    print_option(hero)


def checkBag(hero):  # FIXED
    if hero['bag'] == 'empty':
        print(cGreen + "\n >>> Your bag is empty. There is nothing you can use!\n" + cEnd)
    else:
        print(cGreen + f"\n >>> You have a [" + cYellow + f"{hero['bag']} +{itemDict[hero['bag']]}HP" + cGreen + f"], do you want to use?" + cEnd)
        print(cWhite + " [1] Yes | [2] No\n" + cEnd)
        print(cBlue + " (Choose option 1 or 2)" + cEnd)
        x = input(" > ")
        while x != '1' and x != '2':
            invalid_selection()
            print(cGreen + f" >>> You have a [" + cYellow + f"{hero['bag']} +{itemDict[hero['bag']]}HP" + cGreen + f"], do you want to use?" + cEnd)
            print(cWhite + "[1] Yes | [2] No\n" + cEnd)
            print(cBlue + "(Choose option 1 or 2)" + cEnd)
            x = input(" > ")
        if x == '1':
            print(cGreen + f"\n >>> You have used [" + cYellow + f"{hero['bag']} +{itemDict[hero['bag']]}HP" + cGreen + f"]. Your new HP is now [" + cYellow + f"{hero['hp'] + itemDict[hero['bag']]}HP" + cGreen + "].\n")
            hero['hp'] += itemDict[hero['bag']]
            hero['bag'] = 'empty'
        elif x == '2':
            print(cGreen + f"\n >>> You have not use [" + cYellow + f"{hero['bag']} +{itemDict[hero['bag']]}HP" + cGreen + f"].\n")
    print_option(hero)


def collect_item(hero):  # FIXED
    luck = random.randint(0, 100)
    if luck > 10:
        item_list = start_item + start_weapon + special_item + special_weapon
        item = random.choice(item_list)
        if item in itemDict:
            if hero['bag'] == 'empty':
                print(cGreen + "\n >>> You searched the dead " + cYellow + f"{hero['enemy']}" + cGreen + " and found a [" + cYellow + f"{item} +{itemDict[item]}HP" + cGreen + "]." + cEnd)
                hero['bag'] = item
            else:
                print(cGreen + "\n >>> You found [" + cYellow + f"{item} {itemDict[item]}HP" + cGreen + "] from the " + cYellow + f"{hero['enemy']}" + cGreen + " but your backpack is full." + cEnd)
                print(cGreen + " >>> Do you want to exchange it with your [" + cYellow + f"{hero['bag']} {itemDict[hero['bag']]}HP" + cGreen + "]?" + cEnd)
                x = input(" [1] Yes | [2] No\n > ")
                while x != '1' and x != '2':
                    invalid_selection()
                    print(cGreen + " >>> Do you want to exchange your [" + cYellow + f"{hero['bag']} {itemDict[hero['bag']]}HP" + cGreen + "] with the [" + cYellow + f"{item} {itemDict[item]}HP" + cGreen + "]?" + cEnd)
                    x = input(" [1] Yes | [2] No\n > ")
                if x == '1':
                    print(cGreen + "\n >>> You discard [" + cYellow + f"{hero['bag']} {itemDict[hero['bag']]}HP" + cGreen + "] from your backpack and took [" + cYellow + f"{item} {itemDict[item]}HP" + cGreen + "]." + cEnd)
                    hero['bag'] = item
                elif x == '2':
                    print(cGreen + "\n >>> You discard [" + cYellow + f"{item} {itemDict[item]}HP" + cGreen + "]." + cEnd)
        else:
            print(cGreen + "\n >>> You found a weapon from the " + cYellow + f"{hero['enemy']}" + cGreen + ". Do you want to exchange" +cEnd)
            print(cGreen + " >>> your [" + cYellow + f"{hero['weapon']} {weaponDict[hero['weapon']]}AP" + cGreen + "] and equiped the new [" + cYellow + f"{item} {weaponDict[item]}AP" + cGreen + "]?" + cEnd)
            x = input(" [1] Yes | [2] No\n > ")
            while x != '1' and x != '2':
                invalid_selection()
                print(cGreen + " >>> Do you want to drop your [" + cYellow + f"{hero['weapon']} {weaponDict[hero['weapon']]}AP" + cGreen + "] and equiped the new [" + cYellow + f"{item} {weaponDict[item]}AP" + cGreen + "]?." + cEnd)
                x = input(" [1] Yes | [2] No\n > ")
            if x == '1':
                print(cGreen + "\n >>> You discard [" + cYellow + f"{hero['weapon']} {weaponDict[hero['weapon']]}AP" + cGreen + "] and took the new [" + cYellow + f"{item} {weaponDict[item]}AP" + cGreen + "]." + cEnd)
                hero['weapon'] = item
            elif x == '2':
                print(cGreen + "\n >>> You discard [" + cYellow + f"{item} {weaponDict[item]}AP" + cGreen + "]" + cEnd)


def attack(hero):  # FIXED
    for i in range(4):
        print(cRed + f" {'=' * i}" + cEnd)
        i += 1
    print_pause("===》*", 1, cRed)
    atk = random.randint(0, weaponDict[hero['weapon']])
    if atk == 0:
        print(cGreen + f"\n >>> The [" + cYellow + f"{hero['enemy']} {hero['enemy_health']}HP" + cGreen + "] blocked you attack!" + cEnd)
    else:
        print(cGreen + "\n >>> You strike the [" + cYellow + f"{hero['enemy']} {hero['enemy_health']}HP" + cGreen + "] with a " + cYellow + f"{hero['weapon']}" + cGreen + f". Dealing [" + cYellow + f"{atk}HP" + cGreen + "] damage.")
    hero['t_attack'] += atk
    hero['enemy_health'] -= atk
    if hero['enemy_health'] <= 0:
        print(cGreen + f" >>> The " + cYellow + f"{hero['enemy']}" + cGreen + " is dead by your one hit critial strike!")
        collect_item(hero)
        print_pause(f">>> And you continue your journey...", 1, cGreen)
        hero['kill'] += 1
        hero['turn'] -= 1
        hero['in_battle'] = 0
        hero['enemy'] = enemy_type[random.randint(0, len(enemy_type) - 1)]
        hero['enemy_health'] = enemyHP[hero['enemy']]
        return
    if atk != 0:
        print_pause(cGreen + f">>> That was a good strike! But the [" + cYellow + f"{hero['enemy']} {hero['enemy_health']}HP" + cGreen + f"] is still alive.", 2, cGreen)
    print_pause(f">>> Now the {hero['enemy']} is getting angry and ready to charging at you!", 1, cGreen)
    for i in range(4):
        print(cRed + f"{' ===='[0:-i]}" + cEnd)
        i -= 1
    print_pause('*\n', 1, cRed)
    damage = random.randint(0, enemyAP[hero['enemy']])
    hero['t_damage'] += damage
    hero['hp'] -= damage
    if hero['hp'] <= 0:
        hero['finish'] = 'dead'
        ending(hero)
    else:
        if damage == 0:
            print(cGreen + " >>> But you evade the attack from the [" + cYellow + f"{hero['enemy']} {hero['enemy_health']}HP" + cGreen + "]. No damage was done." + cEnd)
        else:
            print(cGreen + f" >>> You took [" + cYellow + f"{damage}HP" + cGreen + f"] damage from the " + cYellow + f"{hero['enemy']}" + cGreen + "." + cEnd)
            print(cGreen + f" >>> You left [" + cYellow + f"{hero['hp']}HP" + cGreen + "]" + cEnd)


def run_away(hero):  # FIXED2
    luck = random.randint(0, 100)
    print(cGreen + f"\n >>> Attempting to try to run away" + cEnd)
    for i in range(4):
        print(cRed + f"{' ....'[0:-i]}" + cEnd)
        i -= 1
    if luck > 40:
        print(cRed + " >>> Successfully ran away!\n" + cEnd)
        print_pause(f">>> And you continue your journey...", 1, cGreen)
        hero['escape'] += 1
        hero['turn'] -= 1
        hero['in_battle'] = 0
        hero['enemy'] = enemy_type[random.randint(0, len(enemy_type) - 1)]
        hero['enemy_health'] = enemyHP[hero['enemy']]
    else:
        damage = random.randint(0, enemyAP[hero['enemy']])
        hero['t_damage'] += damage
        hero['hp'] -= damage
        print_pause(f">>> You failed to run away!\n", 1, cRed)
        if damage == 0:
            print(cGreen + " >>> But you evade the attack from the [" + cYellow + f"{hero['enemy']} {hero['enemy_health']}HP" + cGreen + "]. No damage was done." + cEnd)
        else:
            print(cGreen + " >>> You took [" + cYellow + f"{damage} HP" + cGreen + "] damage from " + cYellow + f"{hero['enemy']}" + cGreen + "." + cEnd)
        if hero['hp'] <= 0:
            hero['finish'] = 'dead'
            ending(hero)
        else:
            print(cGreen + " >>> You left [" + cYellow + f"{hero['hp']} HP" + cGreen + "]" + cEnd)


def battle_menu(hero):  # FIXED
    while True:
        print_pause(f"(Choose option 1 to 5)", 0, cBlue)
        choice = input(' > ')
        if choice == '1':
            checkHealth(hero)
        elif choice == '2':
            checkWeapon(hero)
        elif choice == '3':
            checkBag(hero)
        elif choice == '4':
            attack(hero)
            return
        elif choice == '5':
            run_away(hero)
            return
        else:
            invalid_selection()
            print_option(hero)


def walking(hero):  # FIXED
    while True:
        if hero['enter_counter'] == 0:
            hero['enter_counter'] = 1
            hero['t_battle'] += 1
            hero['turn'] = random.randint(0, 3)
            hero['enemy'] = enemy_type[random.randint(0, len(enemy_type) - 1)]
            hero['enemy_health'] = enemyHP[hero['enemy']]
            hero['in_battle'] = 0
        hero['option'] = f"[4] Attack the {hero['enemy']} ({hero['enemy_health']}HP) | [5] Try to run away\n"
        if hero['turn'] == 0:
            return
        if hero['in_battle'] == 0:
            hero['in_battle'] = 1
            print(cGreen + "\n >>> The " + cYellow + f"{hero['story']}" + cGreen + " is far away and you need " + cYellow + f"{hero['turn']}" + cGreen + " days to reach.")
            print(cGreen + f" >>> While traveling to the " + cYellow + f"{hero['story']}" + cGreen + ", suddenly a [" + cYellow + f"{hero['enemy']} {hero['enemy_health']}HP" + cGreen + "] appeared!\n" + cEnd)
        else:
            print(cGreen + f"\n >>> The [" + cYellow + f"{hero['enemy']} {hero['enemy_health']}HP" + cGreen + "] never seem wanting to give up!\n")
        print_option(hero)
        battle_menu(hero)


def ending(hero):  # WIP
    if hero['ending'] == 'dead':
        if hero['name'] == '':
            print('dead')
            return
        else:
            return
    elif hero['ending'] == 'complete':
        if hero['name'] == '':
            print("you won but you still don't know who are you and your past")
    return


def navigation_menu(hero):  # WIP
    if hero['story'] == 'world':  # FIXED
        while True:
            print_pause(f"\n (Choose option 1 to 5)", 0, cBlue)
            choice = input(' > ')
            if choice == '1':
                checkHealth(hero)
            elif choice == '2':
                checkWeapon(hero)
            elif choice == '3':
                checkBag(hero)
            elif choice == '4':
                hero['story'] = 'forest'
                hero['enter_counter'] = 0
                story_board(hero)
            elif choice == '5':
                hero['story'] = 'town'
                hero['enter_counter'] = 0
                story_board(hero)
            else:
                invalid_selection()
                print_option(hero)
    elif hero['story'] == 'town':  # WIP
        while True:
            print_pause(f"(Choose option 1 to 6)", 0, cBlue)
            choice = input(' > ')
            if choice == '1':
                checkHealth(hero)
            elif choice == '2':
                checkWeapon(hero)
            elif choice == '3':
                checkBag(hero)
            elif choice == '4':
                hero['story'] = 'inn'
                story_board(hero)
            elif choice == '5':
                hero['story'] = 'pub'
                story_board(hero)
            elif choice == '6':
                hero['story'] = 'world'
                hero['enter_counter'] = 0
                hero['sleep_counter'] = 0
                story_board(hero)
            else:
                invalid_selection()
                print_option(hero)
    elif hero['story'] == 'inn':  # WIP
        while True:
            choice = input("(Choose option 1 to 5)\n > ")
            if choice == '1':
                checkHealth(hero)
            elif choice == '2':
                checkWeapon(hero)
            elif choice == '3':
                checkBag(hero)
            elif choice == '4':
                hero['story'] = 'pub'
            elif choice == '5':
                story_board(hero)
                hero['story'] = 'world'
                hero['enter_counter'] = 0
                story_board(hero)
            else:
                invalid_selection()
                print_option(hero)
    elif hero['story'] == 'forest':  # WIP
        while True:
            choice = input("(Choose option 1 to 6)\n > ")
            if choice == '1':
                checkHealth(hero)
            elif choice == '2':
                checkWeapon(hero)
            elif choice == '3':
                checkBag(hero)
            elif choice == '4':
                hero['story'] = 'world'
                story_board(hero)
            elif choice == '5':
                hero['story'] = 'town'
                story_board(hero)


def story_board(hero):  # WIP
    if hero['story'] == "intro":  # FIXED
        print_pause("\n ++++++++++++++++++++++++++++++++++++++++++", 1, cGreen)
        print_pause("+ ____|                   |     _ )      +", 1, cGreen)
        print_pause("+ |    _ \   __| _ \  __| __|   _ \ \    +", 1, cGreen)
        print_pause("+ __| (   | |    __/\__ \ |    ( `  <    +", 1, cGreen)
        print_pause("+_|  \___/ _|  \___|____/\__| \___/\/    +", 1, cGreen)
        print_pause("+                                        +", 1, cGreen)
        print_pause("+ __ \                                   +", 1, cGreen)
        print_pause("+ |   |  __| _` |  _` |  _ \  __ \   __| +", 1, cGreen)
        print_pause("+ |   | |   (   | (   | (   | |   |\__ \ +", 1, cGreen)
        print_pause("+____/ _|  \__,_|\__, |\___/ _|  _|____/ +", 1, cGreen)
        print_pause("+                |___/                   +", 1, cGreen)
        print_pause("++++++++++++++++++++++++++++++++++++++++++", 1, cGreen)
        print(cGreen + " Press [" + cYellow + "ENTER" + cGreen + "] key to continue" + cEnd)
        input('')
        print_pause(">>> It is the medieval era. You woke up in a winding woods.", 2, cGreen)
        print_pause(">>> You felt a great pain in your head and you can't remember", 2, cGreen)
        print_pause(f">>> what happened, where are you and what's your name?\n", 2, cGreen)
        hero['story'] = 'world'
        story_board(hero)
    elif hero['story'] == 'world':  # FIXED
        print_pause("\n >>> The night fall soon and you saw the eerie dark forest", 2, cGreen)
        print_pause(">>> towards the north and to your south is a crowded town.\n", 2, cGreen)
        hero['option'] = "[4] Head north into the dark woods (Not Complete) | [5] Walk south to the crowded town"
        print_option(hero)
        navigation_menu(hero)
    elif hero['story'] == 'town':  # WIP
        if hero['enter_counter'] == 0:
            walking(hero)
        if hero['turn'] == 0:
            hero['option'] = "[4] Take a rest in the inn | [5] Check out the pub | [6] Leave the town\n"
            print_pause("\n >>> Finally you made it alive to the crowded town.\n", 2, cGreen)
            if hero['name'] == 'NoName':
                print_pause(">>> While you approaching the town gate, you heard an", 2, cGreen)
                print_pause(">>> angry voice. \"Who are you!?\" Shouted the fiercesome guard.\n", 2, cGreen)
                while hero['name'] == 'NoName':
                    print_pause("What you decide to do?", 1, cBlue)
                    print(" [1] Tell the guard your name | [2] You don't wish to tell the guard your name")
                    print_pause(f"\n (Choose option 1 or 2)", 0, cBlue)
                    x = input(" > ")
                    while x != '1' and x != '2':
                        invalid_selection()
                        print_pause("What you decide to do?", 1, cBlue)
                        print(" [1] Tell the guard your name | [2] You don't wish to tell the guard your name")
                        print_pause(f"\n (Choose option 1 or 2)", 0, cBlue)
                        x = input(" > ")
                    if x == '1':
                        print_pause("\n What is your name?", 1, cBlue)
                        i = input(" > ")
                        i = i.strip()
                        while i.replace(" ", "") == "":
                            print_pause("Input not reconise, please try again.\n", 1, cRed)
                            print_pause("What is your name?", 1, cBlue)
                            i = input(" > ")
                            i = i.strip()
                        print_pause(f"\n >>> You enter {i}. You cannot change your name once it is set", 1, cGreen)
                        print(" [1] Ok | [2] Change my mind")
                        print_pause(f"\n (Choose option 1 or 2)", 0, cBlue)
                        a = input(" > ")
                        print(" ")
                        while a != '1' and a != '2':
                            invalid_selection()
                            print_pause(f" >>> You enter {i}. You cannot change your name once it is set", 1, cBlue)
                            print(" [1] Ok | [2] Change my mind")
                            print_pause(f"\n (Choose option 1 or 2)", 0, cBlue)
                            a = input(" > ")
                            print(" ")
                            continue
                        if a == '1':
                            hero['name'] = i
                            hero['option'] = "[4] Take a rest in the inn | [5] Check out the pub (Not Complete) | [6] Leave the town\n"
                            i = random.randint(0, 1)
                            print_pause(f">>> Howdy {hero['name']}! What bring you here?", 2, cGreen)
                            if i == 1:
                                print_pause(f">>> Head over to the pub and speak with the folks around.\n", 2, cGreen)
                            else:
                                print_pause(f">>> It's getting dark soon, you should not wonder around.", 1, cGreen)
                                print_pause(f">>> You can spend a night in the inn if you would like.\n", 1, cGreen)
                    elif x == '2':
                        hero['name'] = 'stranger'
                        print_pause(f"\n >>> Hey Stranger! State your purpose here! Shouted the guards.\n", 2, cGreen)
                        hero['option'] = "[4] Visit the Inn | [5] Take a look in the Pub | [6] Leave town\n"
            elif hero['name'] == 'stranger':
                print_pause(f"\n>>> Hey Stranger! State your purpose here! Shouted the guards.\n", 2, cGreen)
                hero['option'] = "[4] Visit the Inn | [5] Take a look in the Pub | [6] Leave town\n"
            else:
                print_pause(f">>> Hi {hero['name']}! Welcome back! How is your quest? Greeted the guards", 2, cGreen)
                i = random.randint(0, 1)
                if i == 1:
                    print_pause(f">>> Head over to the pub and speak with the folks around\n.", 2, cGreen)
                else:
                    print_pause(f">>> It's getting dark soon, you should not wonder around.", 1, cGreen)
                    print_pause(f">>> You can spend a night in the inn if you would like.", 1, cGreen)
        print_option(hero)
        navigation_menu(hero)
    elif hero['story'] == 'inn':
        if hero['sleep_counter'] == 0:
            if hero['name'] == 'stranger':
                print_pause(f"\n >>> Come on in stranger. How \"WOULD\" you like to stay for a night?\n", 2, cGreen)
                print(cBlue + " What you decide to do?" + cEnd)
                print(' [1] Yes! Why not? | [2] No it alright.\n')
                print(cBlue + " (Choose option 1 or 2)" + cEnd)
                a = input(' > ')
                while a != '1' and a != '2':
                    invalid_selection()
                    print(cBlue + f" \"WOULD\" you like to stay for a night?" + cEnd)
                    print(' [1] Yes! Why not? | [2] No it alright.\n')
                    print(cBlue + " (Choose option 1 or 2)" + cEnd)
                    a = input(' > ')
                if a == '1':
                    add_hp = random.randint(1, 10)
                    hero['hp'] += add_hp
                    for i in range(4):
                        print_pause(f"{'=' * i}", 0.5, cGreen)
                        i += 1
                    if random.randint(0, 0) == 0:
                        print_pause(cGreen + ">>> You restore [" + cYellow + f"{add_hp}HP" + cGreen + "] from sleeping. Your new health is now [" + cYellow + f"{hero['hp']}HP" + cGreen + "]." + cEnd, 2, cGreen)
                        print_pause(cGreen + ">>> You notice your bag is opened and your [" + cYellow + f"{hero['bag']} +{itemDict[hero['bag']]}HP" + cGreen + "] is missing! You have been robbed!" + cEnd, 2, cGreen)
                        print_pause(">>> You left the inn feeling angry!\n", 2, cGreen)
                        hero['bag'] = 'empty'
                        hero['sleep_counter'] = 1
                        hero['story'] = 'town'
                    else:
                        print_pause(cGreen + ">>> You restore [" + cYellow + f"{add_hp}HP" + cGreen + "] from sleeping. Your new health is now [" + cYellow + f"{hero['hp']}HP" + cGreen + "]." + cEnd, 2, cGreen)
                        print_pause("\n >>> You left the Inn... \n", 2, cGreen)
                        hero['sleep_counter'] = 1
                        hero['story'] = 'town'
                elif a == '2':
                    print_pause("\n >>> You left the Inn... \n", 2, cGreen)
                    hero['story'] = 'town'
            else:
                print_pause(f"\n >>> Come on in {hero['name']}, you look tired. You should take a rest.\n", 2, cGreen)
                print(cBlue + " What you decide to do?" + cEnd)
                print(' [1] Yes I could take a nap | [2] No it alright, thanks for you offer\n')
                print(cBlue + " (Choose option 1 or 2)" + cEnd)
                x = input(' > ')
                while x != '1' and x != '2':
                    invalid_selection()
                    print_pause(f">>> Do you like to take a rest in the inn?", 2, cBlue)
                    print(' [1] Yes | [2] No\n')
                    print(cBlue + " (Choose option 1 or 2)" + cEnd)
                    x = input(' > ')
                if x == '1':
                    hero['sleeo_counter'] = 1
                    add_hp = random. randint(10, 50)
                    hero['hp'] += add_hp
                    for i in range(4):
                        print_pause(f"{'=' * i}", 0.5, cGreen)
                        i += 1
                    hero['sleep_counter'] = 1
                    hero['story'] = 'town'
                    print_pause(cGreen + ">>> Good morning " + cYellow + f"{hero['name']}" + cGreen + "! You restore [" + cYellow + f"{add_hp}HP" + cGreen + "] from your sleep.", 0, cGreen)
                    print_pause(cGreen + ">>> You left the inn and feeling great. Your new health is now [" + cYellow + f"{hero['hp']}HP" + cGreen + "].\n", 2, cGreen)
                elif x == '2':
                    hero['story'] = 'town'
                    print_pause("\n >>> Goodbye Sir! Have a nice day and see you soon! \n", 2, cGreen)
        elif hero['sleep_counter'] == 1:
            hero['story'] = 'town'
            print_pause(f"\n >>> The inn is closed now.\n", 2, cGreen)
        print_option(hero)
        navigation_menu(hero)
    elif hero['story'] == 'pub':
        return
    elif hero['story'] == 'forest':  # WIP
        return


story_board(hero)  # WIP
ending(hero)
