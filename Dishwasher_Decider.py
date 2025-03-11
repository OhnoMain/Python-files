import random

def display_banner():
    print("┌─────────────────────────────────────────────────────────────────────────────┐")
    print("│██████╗ ██╗███████╗██╗  ██╗██╗    ██╗ █████╗ ███████╗██╗  ██╗███████╗██████╗ │")
    print("│██╔══██╗██║██╔════╝██║  ██║██║    ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗│")
    print("│██║  ██║██║███████╗███████║██║ █╗ ██║███████║███████╗███████║█████╗  ██████╔╝│")
    print("│██║  ██║██║╚════██║██╔══██║██║███╗██║██╔══██║╚════██║██╔══██║██╔══╝  ██╔══██╗│")
    print("│██████╔╝██║███████║██║  ██║╚███╔███╔╝██║  ██║███████║██║  ██║███████╗██║  ██║│")
    print("│╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝│")
    print("│                                                                             │")
    print("│██████╗ ███████╗ ██████╗██╗██████╗ ███████╗██████╗                           │")
    print("│██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝██╔══██╗                          │")
    print("│██║  ██║█████╗  ██║     ██║██║  ██║█████╗  ██████╔╝                          │")
    print("│██║  ██║██╔══╝  ██║     ██║██║  ██║██╔══╝  ██╔══██╗                          │")
    print("│██████╔╝███████╗╚██████╗██║██████╔╝███████╗██║  ██║                          │")
    print("│╚═════╝ ╚══════╝╚═════╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝                          │")
    print("└─────────────────────────────────────────────────────────────────────────────┘")
    print("")
    print("Welcome to the dishwasher decider")
    print("This program is designed to help resolve common family issues through luck")
    print("")

def get_people():
    counter = 1
    choice = []
    num = int(input("Please enter the number of people playing: "))
    print("")
    for x in range(num):
        people = input(f"What is the name of contestant number {counter}?: ")
        print("")
        choice.append(people)
        counter += 1
    return choice

def choose_people(choice):
    chosen_indices = random.sample(range(len(choice)), 2)
    return choice[chosen_indices[0]], choice[chosen_indices[1]]

def main():
    display_banner()
    choice = get_people()
    chosen1, chosen2 = choose_people(choice)
    print(f"The 2 people doing the dishwasher are: {chosen1} and {chosen2}")
    print("")
    BorT = input(f"{chosen1}, please pick 1 or 2: ")
    print("")
    if BorT == "1":
        print(f"Great, so {chosen1} is doing the bottom shelf and {chosen2} is doing the top")
    elif BorT == "2":
        print(f"Great, so {chosen1} is doing the top shelf and {chosen2} is doing the bottom")
    elif BorT == "Override":
        password = input("Please enter the override password: ")
        if password != "Addman123":
            print("Unauthorised access")
        else:
            print("Welcome to the override menu, what would you like to do?")
            print("1) Force the dishwasher on someone")
            print("2) Remove yourself from the choices")
            print("3) Exit the override menu")
            overrideOptions = int(input("Please make your choice: "))
            if overrideOptions == 1:
                force = input("Make sure the person will be choice 1 (press y to confirm): ")
                if force == "y":
                    # Override force menu logic
                    pass

main()
