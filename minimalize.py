import random
counter = 1
Choice = []
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
print("│╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝                          │")
print("└─────────────────────────────────────────────────────────────────────────────┘")
print("")
print("")
print("                       Welcome to the dishwasher decider")
print("")
print("This program is designed to help resolve common family issues through luck")
print("")
print("")
num = int(input("Please enter the number of people playing: "))

for x in range(num):
    People = input(f"What is the name of contestant number {counter}?: ")
    Choice.append(People)
    counter += 1
    
# Generate the person
chosen_indices = random.sample(range(num), 2)
Chosen1 = Choice[chosen_indices[0]]
Chosen2 = Choice[chosen_indices[1]]

print("")
print("")
print(f"The 2 people doing the dishwaser are: {Chosen1} and {Chosen2}")
print("")
print("")
BorT = int(input(f"{Chosen1}, please pick 1(bottom) or 2(top): "))
print("")
if BorT == 1:
    print(f"Great, so {Chosen1} is doing the bottom shelve and {Chosen2} is doing the top")
else:
     print(f"Great, so {Chosen1} is doing the top shelve and {Chosen2} is doing the bottom")   


