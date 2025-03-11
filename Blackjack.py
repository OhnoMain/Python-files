# By Ohno
import random
import time
money = 100

# Welcome to the game ;)
print("""


 ____  _            _       _            _    
| __ )| | __ _  ___| | __  | | __ _  ___| | __
|  _ \| |/ _` |/ __| |/ /  | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   < |_| | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\


    made by Ohno who is better than Brodie
    """)
time.sleep(2)
print("""
            (why is jack black?)
            
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")


player_hand = []
dealer_hand = []

# Player cards
cards = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
player_hand.append(cards[random.randint(0, len(cards) - 1)])
player_hand.append(cards[random.randint(0, len(cards) - 1)])

# Dealer cards
dealer_hand.append(cards[random.randint(0, len(cards) - 1)])
dealer_hand.append(cards[random.randint(0, len(cards) - 1)])

# Calculate the player's score
player_score = 0
for card in player_hand:
    player_score += card
if 11 in player_hand and player_score > 21:
    player_score -= 10
    
time.sleep(1)
money = int(input("How much money do you want to start of with?(0-500): "))
# Loop for player
game_over = False
while not game_over:
    print("")
    print("")
    print(f"                                                                          £{money}")
    time.sleep(2)
    print("")
    reveal = input("Press 'r' to reveal your cards: ")
    if reveal == "r":
        time.sleep(2)
    print(f"Your 2 cards are: {', '.join(map(str, player_hand))}")
    time.sleep(1)
    print(f"Your score is: {player_score}")
    time.sleep(1)
    print("")
    print(f"The dealer's score is: {dealer_hand[0]}")
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    time.sleep(1)
    
    if player_score == 21:
        print("Blackjack! You win!")
        game_over = True
    elif player_score > 21:
        print("You went over 21. You lose!")
        game_over = True
    else:
        print("")
        action = input("'h' to hit or 's' to stand: ").lower()
        if action == 'h':
            money = money-20
            new_card = cards[random.randint(0, len(cards) - 1)]
            player_hand.append(new_card)
            player_score += new_card
            if 11 in player_hand and player_score > 21:
                player_score -= 10
        elif action == 's':
            money = money-10
            game_over = True
        else:
            print("Invalid input! Please type 'h' or 's'.")
            print("")

# Dealer's turn (this is automated)
dealer_score = 0
for card in dealer_hand:
    dealer_score += card
if 11 in dealer_hand and dealer_score > 21:
    dealer_score -= 10

while dealer_score < 17:
    new_card = cards[random.randint(0, len(cards) - 1)]
    dealer_hand.append(new_card)
    dealer_score += new_card
    if 11 in dealer_hand and dealer_score > 21:
        dealer_score -= 10

# Display final results
time.sleep(1)
print(f"Your final hand: {', '.join(map(str, player_hand))}, final score: {player_score}")
print("")
time.sleep(1)
print(f"Dealer's final hand: {', '.join(map(str, dealer_hand))}, final score: {dealer_score}")
drink = input("Would you like a drink?(y/n): ")
if drink == "y":
    print("")
    print("""
                         .sssssssss.
                   .sssssssssssssssssss
                 sssssssssssssssssssssssss
                ssssssssssssssssssssssssssss
                 @@sssssssssssssssssssssss@ss
                 |s@@@@sssssssssssssss@@@@s|s
          _______|sssss@@@@@sssss@@@@@sssss|s
        /         sssssssss@sssss@sssssssss|s
       /  .------+.ssssssss@sssss@ssssssss.|
      /  /       |...sssssss@sss@sssssss...|
     |  |        |.......sss@sss@ssss......|
     |  |        |..........s@ss@sss.......|
     |  |        |...........@ss@..........|
      \  \       |............ss@..........|
       \  '------+...........ss@...........|
        \________ .........................|
                 |.........................|
                /...........................\
               |.............................|
                  |.......................|
                      |...............|
""")
    print("glug, glug")

if player_score > 21:
    time.sleep(1)
    print("")
    print("You went over 21. You lose :( ")
elif dealer_score > 21:
    time.sleep(1)
    print("")
    print("Dealer went over 21. You win :)")
elif player_score > dealer_score:
    time.sleep(1)
    print("")
    print("You win :)")
elif player_score < dealer_score:
    time.sleep(1)
    print("")
    print("You lose :(")
else:
    time.sleep(1)
    print("")
    print("It's a draw!")
