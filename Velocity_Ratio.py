counter = 1
gears = int(input("How many gears do you have?: "))

gear = [""]*gears
print("Please enter the size of each gear")

for x in range(gears):
    gear[x] = int(input(f"{counter}): "))
    counter += 1

print(f"The velocity ratio is {gear[0]/gear[counter]}")
for x in range(gears):
    print(gear[x])
