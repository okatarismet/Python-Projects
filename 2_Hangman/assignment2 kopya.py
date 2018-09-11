#
#
#
#
#Guessed word: y used in IN mode. The game turned into OUt mode.
#
#
#
#
import sys


stringkelime = "s"
kelime = list(sys.argv[1])
stringkelime = sys.argv[1]
list_denenen = sys.argv[2].split(",")
mode = "IN"
usedin = 0
usedINlist = []
usedOUTlist = []
usedout = 0
guesses = 5
empty_list = []
match = "0"
turn = ""
usedmode = ""

def emptylist_adder():
    for i in kelime:
        empty_list.append("-")



emptylist_adder()

print("You have 5 guesses left")
print(empty_list)
print("--------------------------------------------")
for i in range(len(list_denenen)):

    if guesses < 1 :
        print("")
        print("You lost the game")
        break


    for y in range(len(usedINlist)):
        if list_denenen[i] == usedINlist[y]:
            usedin = 1
            usedmode = ""
            break
        else:
            usedin = 0
            #print("amidiye")
    for y in range(len(usedOUTlist)):
        if list_denenen[i] == usedOUTlist[y]:
            usedout = 1
            #print("ayyip")
            break
        else:
            usedout = 0
            # print("ilicadar")

    match = "0"
    for x in range(len(kelime)):
        if mode == "IN":
            if list_denenen[i] == kelime[x]:
                empty_list[x] = list_denenen[i]
                usedINlist.append(list_denenen[i])
                match = "1"

        if mode == "OUT":
            if list_denenen[i] == kelime[x]:
                #empty_list[x] = list_denenen[i]
                usedOUTlist.append(list_denenen[i])
                match = "1"


    if mode == "IN":                        #####ANA MODUL
        if match == "1" and usedin == 0:
            turn = ""
            print("Guessed word: " + list_denenen[i] + " You are in IN mode")

        else:
            if usedin == 1:
                guesses = guesses - 1
                mode = "OUT"
                turn = "The game turned into OUT mode"
                print("Guessed word: " + list_denenen[i] + " used in IN mode. "  + turn + "")
            else:
                guesses = guesses - 1
                mode = "OUT"
                turn = "The game turned into OUT mode"
                print("Guessed word: " + list_denenen[i] + " The game turned into OUT mode")



    else :
        if match == "0" and usedout == 0:
            mode ="IN"
            turn = "The game turned into IN mode"
            print("Guessed word: " + list_denenen[i] + " The game turned into IN mode")

        else:
            mode = "OUT"
            guesses = guesses - 1
            turn = ""

            print("Guessed word: " + list_denenen[i] + " You are in OUT mode")

    # print("usedin",usedINlist,usedin)
    # print("usedout",usedOUTlist,usedout)
    print(" You have " + str(guesses) + " guesses left")
    print(empty_list)
    print("--------------------------------------------")
if empty_list != kelime:
    print("")
    print("You finished all letters")
    print("You lost the game")
elif guesses > 0 :
    print("")
    print("You won the game")
