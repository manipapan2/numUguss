import random

#===global===
emtiaz = 0
emtiaz2 = 0
emtiazsolo = 0


#===player1===
def randomizer():
    global emtiaz
    global emtiaz2
    global list1
    global chos


    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
    chos = random.choice(list1)
    guess = input(str(first + " " + "turn: "))
    lal = int(guess)

    if lal == chos:
        print("good!")
        emtiaz = emtiaz + 1
        randomizer2()
    if lal == 6969:
        done1()
        return False
    # if lal != str:
    #     print("are u dumb?")
    #     randomizer()
    if lal != chos:
        print("bad!")
        print("The number was" + " " + str(chos))
        randomizer2()  
    if lal == "" or lal == " ":
        randomizer2()


#===player2===
def randomizer2(): 
    global emtiaz
    global emtiaz2

    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
    chos2 = random.choice(list2)
    guess1 = input(str(second + " " + "turn: "))
    lal1 = int(guess1)

    if lal1 == chos2:
        print("good!")
        emtiaz2 = emtiaz2 + 1
        randomizer()
    if lal1 == 6969:
        done2()
        return False
    if lal1 != chos2:
        print("bad!")
        print("The number was" + " " + str(chos2))
        randomizer()  
    if lal1 == "" or lal1 == " ":
        randomizer()   


#===soloRandomizer===
def randosolo():
    global emtiazsolo

    list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
    chos3 = random.choice(list3)
    guess3 = input(str(soln + " " + "turn: "))
    lal3 = int(guess3)
    if lal3 == chos3:
        print("good!")
        emtiazsolo = emtiazsolo + 1
        randosolo()
    if lal3 == 6969:
        dones()
        return False
    if lal3 != chos3:
        print("bad!")
        print("The number was" + " " + str(chos3))
        randosolo()  
    if lal3 == "" or lal3 == " ":
        randosolo()


#===done===
def done1():
    print("game has been ended")
    stsscore = str(emtiaz)
    print(first + " score" + " = " + stsscore)
    stsscore2 = str(emtiaz2)
    print(second + " score" + " = " + stsscore2)
    again = input(str("You want to continue? (Y or N): "))
    if again == "Y":
        randomizer()
    if again == "N":
       exit()
    else:
        done1()



def done2():
    print("game has been ended")
    stsscore2 = str(emtiaz)
    print(first + " score" + " = " + stsscore2)
    stsscore22 = str(emtiaz2)
    print(second + " score" + " = " + stsscore22)
    again2 = input(str("You want to continue? (Y or N): "))
    if again2 == "Y":
        randomizer2()
    if again2 == "N":
       exit()
    else:
        done2()



def dones():
    print("game has been ended")
    stsscore3 = str(emtiazsolo)
    print(soln + " score" + " = " + stsscore3)
    again3 = input(str("You want to continue? (Y or N): "))
    if again3 == "Y":
        randosolo()
    if again3 == "N":
        exit()
    else:
        dones()
        



#===start===
def duos():
    global first
    global second
    first = input(str("Enetr first player name: "))
    second = input(str("Enetr second player name: "))
    if first == "" or first == " ":
        duos()    
    else:
        print("game has been started")
        randomizer()


#===solostart===
def solo():
    global soln

    soln = input(str("Enetr your name: "))
    if soln == "" or soln == " ":
        solo()
    else:
        randosolo()

#===sord===
def check():
    chec = input(str("duos or solo? (D or S): "))
    if chec == "S":
        solo()
    if chec == "D":
        duos()
    else:
        check()
check()