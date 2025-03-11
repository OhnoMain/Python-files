# To calculate the speed distance or time

print("What do you want to work out?: ")
print("")
print("1) Speed")
print("2) Distance")
print("3) Time")
print("")
choice = input("(enter the number): ")
print("")
print("")

# Working out the speed
if choice == "1":
    print("Speed")
    print("")
    print("Please enter the distance and the time")
    print("")
    distance = int(input("Distance(to the nearest meter): "))
    time = int(input("Time(to the nearest second): "))
    print("")
    print(f"The speed is {distance/time} ms")

# Working out the distance 
elif choice == "2":
    print("Distance")
    print("")
    print("Please enter the speed and the time")
    print("")
    speed = int(input("Speed(to the nearest m/s): "))
    time = int(input("Time(to the nearest second): "))
    print("")
    print(f"The distance is {speed*time} m")

# Working out the time
else:
    print("Time")
    print("")
    print("Please enter the distance and the speed")
    print("")
    distance = int(input("Distance(to the nearest meter): "))
    speed = int(input("speed(to the nearest m/s): "))
    print("")
    print(f"The time is {distance/speed} s")
