"""

For running this module you need to install random_word package

You should be able to install using easy_install or pip in the usual ways:

$ easy_install random-word
$ pip install random-word
Or just clone this repository and run:

$ python3 setup.py install
Or place the random-word folder that you downloaded somewhere where it can be accessed by your scripts.

Credit goes to VAIBHAV SINGH for this package.

"""

from random_word import RandomWords
import random as rnd
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

r = RandomWords()

def generatePassword(type):
    smallLetters = [chr(x) for x in range(ord('a'), ord('z'))]
    capLetters = [chr(x) for x in range(ord('A'), ord('Z'))]
    specialCharacters = ['_', '@', '$', '&', '*', '!', '?']
    numerics = [chr(x) for x in range(ord('0'), ord(':'))]
    password = ""
    if(type > 3 or type < 1):
        print("Please enter correct value !!!")
        t.sleep(2)
        return 0
    else :
        if(type == 1):
            password = r.get_random_word(hasDictionaryDef="false")
            return password
        elif(type == 2):
            password = "".join(rnd.sample(smallLetters, rnd.randint(3,6))+rnd.sample(capLetters, rnd.randint(3,6))+rnd.sample(numerics, rnd.randint(1,3))+rnd.sample(specialCharacters, rnd.randint(1,3)))
            myList = list(password)
            password = "".join(rnd.sample(myList, rnd.randint(1,2))) + r.get_random_word(hasDictionaryDef="true") + "".join(rnd.sample(myList, rnd.randint(1,2)))
            return password
        else:
            password = "".join(rnd.sample(smallLetters, rnd.randint(4,8))+rnd.sample(capLetters, rnd.randint(4,8))+rnd.sample(numerics, rnd.randint(4,8))+rnd.sample(specialCharacters, rnd.randint(1,3)))
            myList = list(password)
            password = "".join(rnd.sample(myList, rnd.randint(10,15)))
            return password

stop = False
ls = []
while(not stop):
    clear()
    print("Welcome!!! You need internet connection to generate WEAK and MODERATE passwords!!!")
    print("Strength Levels are\n 1. WEAK\n 2. MODERATE\n 3. STRONG")
    type = int(input("Enter strength level : "))
    password = generatePassword(type)
    ls = ls + [password]
    print(password)
    if(input("Type \'STOP\' to stop : ").upper() == "STOP"):
        stop = True
        clear()
        print("List of passwords generated : %s" %ls)
        sleep(2)
        exit()
    sleep(1)
