import subprocess
import random
import time
reassure = "n"                       ## Ascii art finally works so dont touch :) ##
print("")
print("     ____                _               ____             _      _   _        ")
print("    |  _ \ _   _ ___ ___(_) __ _ _ __   |  _ \ ___  _   _| | ___| |_| |_ ___  ")
print("    | |_) | | | / __/ __| |/ _` | '_ \  | |_) / _ \| | | | |/ _ \ __| __/ _ \ ")
print("    |  _ <| |_| \__ \__ \ | (_| | | | | |  _ < (_) | |_| | |  __/ |_| ||  __/ ")
print("    |_| \_\\__,_|___/___/_|\__,_|_| |_| |_| \_\___/ \__,_|_|\___|\__|\__\___| ")
print("")
print("            I am not responsible for any risk or damage to your device")
print("")
print("                                made by Ohno")

                      
print("")

choice = input("Do you want to play Russian Roulette?(y/n): ")
print("")
info = input("Do you want instructions on how to play?(y/n): ")  #
if info == "Y" or info == "y":                                   #
    print("")                                                    #
    print("Welcome to Pc Roulette")                              #
    time.sleep(2)                                                #
    print("This is a game based on the classic Russian Roulette")#
    print("")#                                                   #
    time.sleep(2)                                                #
    print("In this version it will randomly select a number")    #
    print("and then it will ask you to enter a number")          #
    print("")                                                    #  
    time.sleep(3)                                                #
    print("If your number is the same number as the one selected")## Instructions ##
    print("you will feel the wrath of file explorer 😈")         #
    print("")                                                    #
    time.sleep(3)                                                #
    print("Here is a little example...")                         #
    time.sleep(2)                                                #
    subprocess.Popen(['explorer'])                               #
    print("")                                                    #
    time.sleep(3)                                                #
    print("This game is best played with friends")               #
    print("Good luck :)")                                        #
    print("")                                                    #
    time.sleep(3)                                                #
# Round 1
if choice == "Y" or choice =="y":
    number = random.randint(1,10)
    print("")
    print("")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("")
    print("You are currently playing low stakes (round 1)")
    print("")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    numero = int(input("Please enter a number between 1 and 10 (inclusive): "))
    if numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        reassure = input(f"Are you sure you want to pick {numero}?(Y/N):")
    if reassure =="Y" or reassure =="y":
        print(f"The number you picked was {numero}")
        print("And the chosen number was...")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("...")
        # Import several delays with ... inbertween to add suspension
        print(f"{number}")
        if numero == number:
            for i in range(10):
                subprocess.Popen(['explorer'])
                
        else:
            time.sleep(2)
            print("If you are reading this you survived :)")
            print("")
# Round 2           
            if choice == "Y"or choice =="y":
                number = random.randint(1,7)
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("")
                print("You are currently playing medium stakes (round 2)")
                print("")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("The stakes have been times by 10")
                numero = int(input("Please enter a number between 1 and 7 (inclusive): "))
                reassure = input(f"Are you sure you want to pick {numero}?(y/n):")
                if reassure =="Y" or reassure =="y":
                    print(f"The number you picked was {numero}")
                    print("And the chosen number was...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    # Import several delays with ... inbertween to add suspension
                    print(f"{number}")
                    if numero == number:
                        for i in range(100):
                            subprocess.Popen(['explorer'])
                    else:
                        time.sleep(1)
                        print("If you are reading this you survived :)")
                        
# Round 3
                        if choice == "Y" or choice =="y":
                            number = random.randint(1,5)
                            time.sleep(2)
                            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                            print("")
                            print("You are currently playing high stakes (round 3)")
                            print("")
                            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                            print("The stakes have been times by another 10")
                            print("")
                            time.sleep(1)
                            numero = int(input("Please enter a number between 1 and 5 (inclusive): "))
                            reassure = input(f"Are you sure you want to pick {numero}?(Y/N):")
                            if reassure =="Y" or reassure =="y":
                                print(f"The number you picked was {numero}")
                                print("And the chosen number was...")
                                time.sleep(1)
                                print("...")
                                time.sleep(1)
                                # Import several delays with ... inbertween to add suspension
                                print(f"{number}")
                                if numero == number:
                                    for i in range(1000):
                                        subprocess.Popen(['explorer'])
                                else:
                                    time.sleep(2)
                                    print("If you are reading this you have survived :)")

# Round 4
                                    if choice == "Y" or choice =="y":
                                        number = random.randint(1,3)
                                        time.sleep(2)
                                        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                        print("")
                                        print("You are currently playing extreme stakes (round 4)")
                                        print("")
                                        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                        print("The stakes have been times by another 10")
                                        print("")
                                        time.sleep(1)
                                        numero = int(input("Please enter a number between 1 and 3 (inclusive): "))
                                        if numero != 1 or numero != 2 or numero !=3:
                                            reassure = input(f"Are you sure you want to pick {numero}?(Y/N):")
                                        if reassure =="Y" or reassure =="y":
                                            print(f"The number you picked was {numero}")
                                            print("And the chosen number was...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(1)
        
                                            print(f"{number}")
                                            if numero == number:
                                                for i in range(10000):
                                                    subprocess.Popen(['explorer'])
                                            else:
                                                time.sleep(2)
                                                print("If you are reading this you have survived :)")
print("Cheater found")
time.sleep(2)
print("You have made me angry 😠")
for i in range(20):
    subprocess.Popen(['explorer'])
    os.makedirs("Bad")
