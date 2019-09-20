import time
import random


start_item = ['Potion', 'Bread', 'Cookie']
special_item = ['Mega potion', 'Elixir', 'Bandage']
start_weapon = ['Fork', 'Cooking pan', 'Worn dagger']
special_weapon = ['Bow & Arrow', 'Spear', 'Axe', 'Excalibur']
enemyHP = {'Dog': 10, 'Bandit': 30, 'Zombie': 60, 'Dragon': 80}
# enemyHP = {'Dog': 1, 'Bandit': 1, 'Zombie': 1, 'Dragon': 1} # for debugging use only!
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
    'name': 'Chris', 
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
    'finish': ''
    }

hero['hp'] = random.randint(20, 80)
hero['bag'] = start_item[random.randint(0, len(start_item) - 1)]
hero['weapon'] = start_weapon[random.randint(0, len(start_weapon) - 1)]


def print_pause(message, delay):
    print(message)
    # time.sleep(delay - delay + 0.2) # for debugging use only!
    time.sleep(delay - delay + 1)


def print_option(hero):
    print_pause("\nWhat you decide to do, next?", 1)
    print("[1] Check your health stats | [2] Check weapon |"
          " [3] Check backpack")
    print(hero['option'])


def invalid_selection():
    print("\n>>> Invalid option selected. Please try again.")


def checkHealth(hero):
    print(f"\n>>> You current health is {hero['hp']}HP")
    print_option(hero)


def checkWeapon(hero):
    print(f"\n>>> You are equiped with a {hero['weapon']} ({weaponDict[hero['weapon']]}AP)!")
    print_option(hero)


def checkBag(hero):
    if hero['bag'] == 'empty':
        print("\n>>> Your bag is empty. There is nothing you can use!")
        print_option(hero)
        return
    else:
        print(f"\n>>> You have a {hero['bag']} ({itemDict[hero['bag']]}HP), do you want to use?")
        x = input("[1] Yes | [2] No\n")
        if x == '1':
            new_hp = hero['hp'] + itemDict[hero['bag']]
            print(f"\n>>> You have used {hero['bag']}. You increase {itemDict[hero['bag']]}HP. Your HP is now {new_hp}.")
            hero['bag'] = 'empty'
            hero['hp'] = new_hp
            print_option(hero)
            return
        elif x == '2':
            print(f"\n>>> {hero['bag']} not used")
            print_option(hero)
            return
        else:
            invalid_selection()
            checkBag(hero)


def collect_item(hero):
    luck = random.randint(0, 100)
    if luck > 10:
        item_list = start_item + start_weapon + special_item + special_weapon
        item = random.choice(item_list)
        if item in itemDict:
            if hero['bag'] == 'empty':
                print(f"\n>>> You searched the {hero['enemy']} and found a {item} ({itemDict[item]}HP)")
                hero['bag'] = item
                return
            else:
                print(f"\n>>> You found {item} ({itemDict[item]}HP) from the {hero['enemy']} but you backpack is full.")
                print(f">>> Do you want to exchange it with your {hero['bag']} ({itemDict[hero['bag']]}HP)?")
                x = input("[1] Yes | [2] No\n")
                while x != '1' and x != '2':
                    invalid_selection()
                    print(f">>> Do you want to exchange it with your {hero['bag']} ({itemDict[hero['bag']]}HP) with {item} ({itemDict[item]}HP)?")
                    x = input("[1] Yes | [2] No\n")
                if x == '1':
                    print(f"\n>>> You discard {hero['bag']} ({itemDict[hero['bag']]}HP) from your backpack and took {item} ({itemDict[item]}HP).")
                    hero['bag'] = item
                    return
                elif x == '2':
                    print(f"\n>>> You discard {item} ({itemDict[item]}HP)")
                    return
        else:
            print(f"\n>>> You found weapon from the {hero['enemy']}. Do you want to exchange")
            print(f">>> your {hero['weapon']} ({weaponDict[hero['weapon']]}AP) and equiped the new {item} ({weaponDict[item]}AP)?.")
            x = input("[1] Yes | [2] No\n")
            while x != '1' and x != '2':
                invalid_selection()
                print(f">>> Do you want to drop your {hero['weapon']} ({weaponDict[hero['weapon']]}AP) and equiped the new {item} ({weaponDict[item]}AP)?.")
                x = input("[1] Yes | [2] No\n")
            if x == '1':
                print(f"\n>>> You discard {hero['weapon']} ({weaponDict[hero['weapon']]}AP) and took the new {item} ({weaponDict[item]}AP).")
                hero['weapon'] = item
                return
            elif x == '2':
                print(f"\n>>> You discard {item} ({weaponDict[item]}AP)")
            return
    else:
        return


def attack(hero):
    i = 0
    while i < 4:
        x = '='
        print_pause(f"{x * i}", 0.5)
        i += 1
    print_pause("===》*", 1)
    atk = random.randint(0, weaponDict[hero['weapon']])
    if atk == 0:
        print_pause(f"\n>>> The {hero['enemy']} ({hero['enemy_health']}HP) blocked you attack!", 1)
    else:
        print_pause(f"\n>>> You strike {hero['enemy']} ({hero['enemy_health']}HP) with a {hero['weapon']}. Dealing {weaponDict[hero['weapon']]}HP damage.", 1)
    hero['t_attack'] += atk
    hero['enemy_health'] -= atk
    if hero['enemy_health'] <= 0:
        print(f">>> The {hero['enemy']} is dead by your one hit critial strike!")
        collect_item(hero)
        print_pause(f">>> And you continue your journey...", 1)
        hero['kill'] += 1
        hero['turn'] -= 1
        hero['in_battle'] = 0
        hero['enemy'] = enemy_type[random.randint(0, len(enemy_type) - 1)]
        hero['enemy_health'] = enemyHP[hero['enemy']]
        return
    if atk != 0:
        print_pause(f">>> That was a good strike! But the {hero['enemy']} ({hero['enemy_health']}HP) is still alive.", 2)
    print_pause(f">>> Now the {hero['enemy']} is getting angry and ready to charging at you!\n", 1)
    i = 4
    while i > 0:
        x = '='
        print_pause(f"{x * i}", 0.5)
        i -= 1
    print_pause('*\n', 1)
    damage = random.randint(0, enemyAP[hero['enemy']])
    hero['t_damage'] += damage
    hero['hp'] -= damage
    if hero['hp'] <= 0:
        hero['finish'] = 'dead'
        ending(hero)
        return
    else:
        if damage == 0:
            print(f">>> But you evade the attack from the {hero['enemy']}. No damage was done.")
            return
        else:
            print(f">>> You took {damage} damage from the {hero['enemy']}.")
            print_pause(f">>> You left {hero['hp']}HP", 1)
            return


def run_away(hero):
    luck = random.randint(0, 100)
    print_pause(f"\n>>> Attempting to try to run away", 1)
    i = 3
    while i > 0:
        x = '.'
        print_pause(f"{x * i}", 0.5)
        i -= 1
    if luck > 40:
        print(f">>> Successfully ran away!\n")
        print_pause(f">>> And you continue your journey...", 1)
        hero['escape'] += 1
        hero['turn'] -= 1
        hero['in_battle'] = 0
        hero['enemy'] = enemy_type[random.randint(0, len(enemy_type) - 1)]
        hero['enemy_health'] = enemyHP[hero['enemy']]
        return
    else:
        damage = random.randint(0, enemyAP[hero['enemy']])
        hero['t_damage'] += damage
        hero['hp'] -= damage
        print_pause(f">>> You failed to run away!\n", 1)
        if damage == 0:
            print(f">>> But you evade the attack from the {hero['enemy']}. No damage was done.")
        else:
            print(f">>> You took {damage} damage from {hero['enemy']}.")
        if hero['hp'] <= 0:
            hero['finish'] = 'dead'
            ending(hero)
        else:
            print(f">>> You left {hero['hp']}HP")
        return


def battle_menu(hero):
    while True:
        choice = input("(Choose option 1 to 5) ")
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


def navigation_menu(hero):
    if hero['story'] == 'world':
        while True:
            choice = input("(Choose option 1 to 5) ")
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
    elif hero['story'] == 'town':
        while True:
            choice = input("(Choose option 1 to 6) ")
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
                story_board(hero)
            else:
                invalid_selection()
                print_option(hero)
    elif hero['story'] == 'forest':
        while True:
            choice = input("(Choose option 1 to 6) ")
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


def walking(hero):
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
            print_pause(f"\n>>> The {hero['story']} is far away and you need {hero['turn']} days to reach.", 2)
            print_pause(f">>> While traveling to the {hero['story']}, suddenly a {hero['enemy']} ({hero['enemy_health']}HP) appeared!", 2)
        else:
            print_pause(f"\n>>> The {hero['enemy']} ({hero['enemy_health']}HP) never seem wanting to give up!", 2)
        print_option(hero)
        battle_menu(hero)



def ending(hero):
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


def story_board(hero):
    if hero['story'] == "intro":
        print_pause("\n\n>>> It is the medieval era. You woke up in a winding woods.", 2)
        print_pause(">>> You felt a great pain in your head and you can't remember", 2)
        print_pause(">>> what happened, where are you and what's your name?", 2)
        hero['story'] = 'world'
        story_board(hero)
        return
    elif hero['story'] == 'world':
        print_pause("\n>>> The night fall soon and you saw the eerie dark forest", 2)
        print_pause(">>> towards the north and to your south is a crowded town.", 2)
        hero['option'] = "[4] Head north into the dark woods (Not Complete) | [5] Walk south to the crowded town\n"
        print_option(hero)
        navigation_menu(hero)
        return
    elif hero['story'] == 'town':
        if hero['enter_counter'] == 0:
            walking(hero)
            return
        if hero['turn'] == 0:
            hero['option'] = "[4] Take a rest in the inn (Not Complete) | [5] Check out the pub (Not Complete) | [6] Leave the town\n"
            print_pause("\n>>> Finally you made it alive to the crowded town.\n", 2)
            if hero['name'] == '':
                print_pause(">>> While you approaching the town gate, you heard an", 2)
                print_pause(">>> angry voice. \"Who are you!?\" Shouted the fiercesome guard.\n", 2)
                
            else:
                print_pause(f">>> Hi {hero['name']}! Welcome back! How is your quest? Greeted the guards", 2)
                i = random.randint(0, 1)
                if i == 1:
                    print_pause(f">>> Head over to the pub and speak with the folks around.", 2)
                else:
                    print_pause(f">>> It's getting dark soon, you should not wonder around.", 1)
                    print_pause(f">>> You can spend a night in the inn if you would like.", 1)
            print_option(hero)
            navigation_menu(hero)
        return
    elif hero['story'] == 'forest':
        return


story_board(hero)
