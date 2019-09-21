def enter_name(i):
    i = input('Your Name: ')
    return i



n = '3'
name = ''
i = ''

while n == '3':
    x = input("\n[1] Tell the guard your name. [2] You don't wish to tell the guard your name\n")
    if x == '1':
        i = enter_name(i)
        while i.replace(" ", "") == "":
            print("Input not reconise, please try again.\n")
            i = input("Enter your name?\n")
            i = i.strip()             
        print(f"\n>>> You enter {i}. You cannot change your name once it is set.")
        a = input('[1] Yes | [2] No\n')
        while a != '1' and a != '2':
            print('invalid_selection(hero)')
            a = input('[1] Yes | [2] No')
        if a == '1':
            name = i
        elif a == '2':
            i = enter_name(i)
        
    elif x == '2':
        name = 'stranger'
    print('invalid_selection')