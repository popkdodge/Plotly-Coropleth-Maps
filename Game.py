
print("Welcome to not-nodeka.")

print("Enter your name:")
sname = input()
print("Hello, %s what class do you want to play?" % sname)
'''
print('1. Archer \n2. Warrior \n3. Mage')
'''
'''
def pick_class(input):
    """This function will create a class!"""
    input_value = str(input)
    input_value = input_value.lower()
    global sname
    while True:
        if input_value == '1' or input_value == "archer":
            classes = "Archer"
            while = False
        elif input_value == '2' or input_value == "Warrior":
            classes = "Warrior"
            while = False
        elif input_value == '3' or input_value == "Mage":
            classes = "Mage"
            while = False
        else:
            continue

    print(f"{sname}, you pick {classes}.")
'''

changeword = 0

while changeword != 1:
    print('1. Archer \n2. Warrior \n3. Mage')


    choices = str(input("Pick your classes!"))

    if choices == '1' or choices == "archer":
        classes = "Archer"
        changeword +=1
    elif choices == '2' or choices == "Warrior":
        classes = "Warrior"
        changeword +=1
    elif choices == '3' or choices == "Mage":
        classes = "Mage"
        changeword +=1
    else:
        print("Invalid classes choices try agian!")
print(f'{sname},You have pick {classes}!')


'''
name = str(input())
name = name.lower()
pick_class(name)
'''