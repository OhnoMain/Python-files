import random
Decision = True
Counter = 0
mysteryFruits = ["Kiwi","Mango","Apple","Pineapple"]
fruitChoice = [""]*6

while Decision == True:
    chosenFruit = input("Please enter your chosen fruit: ")
    fruitChoice[x] = chosenFruit
    Counter = Counter + 1
    Choice = input("Would you like to enter another fruit?: ")
    if Choice == "Yes" or Choice == "yes" and Counter <6 and Decision == True:
        print("")
    else:
        Decision = False 
        mysteryFruitNumber = random.randint(0,3) ## Change to 9##
        for x in range(Counter):
            print(f"The fruits you entered were: {fruitChoice[x]}")
        mysteryFruits = mysteryFruits[mysteryFruitNumber]
        print(f"The mystery fruit is {mysteryFruits}")
print("Uh oh")




