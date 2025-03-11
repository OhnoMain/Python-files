movie = [""]*5

for x in range(5):
    mc = input("Please enter one of your top 10 movies of all time")

    movie[x] = mc


print("Your top 5 movies of all time are")

counter = 1

for x in range(5):
    print(f"{counter}: {movie[x]}")

    conter =+ 1
