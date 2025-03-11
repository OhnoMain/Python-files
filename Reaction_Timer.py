import time
import random

print("""
         .--.
    .-._;.--.;_.-.
   (_.'_..--.._'._)
    /.' . 60 . '.\
   // .      / . \\
  |; .      /   . |;
  ||45    ()    15||
  |; .          . |;
   \\ .        . //
    \'._' 30 '_.'/
     '-._'--'_.-'
         `""` 
      Reaction Timer Game
          made by Ohno
""")

# Instructions
print("Instructions: Wait for the 'GO!' signal, then press ENTER as fast as you can.\n")
input("Press ENTER when you're ready to begin...\n")

# Random delay before starting
delay = random.uniform(2, 5)  # Random delay between 2 and 5 seconds
print("Get ready...")
time.sleep(delay)  # Wait for the random delay

# Start timer
start_time = time.time()
print("GO!")

# Wait for user to hit ENTER
input()
end_time = time.time()

# Calculate reaction time
reaction_time = end_time - start_time
print(f"Your reaction time: {reaction_time:.3f} seconds")

# Feedback
if reaction_time < 0.2:
    print("Incredible reflexes!")
elif reaction_time < 0.5:
    print("Great job! Very quick!")
else:
    print("Good effort! Keep practicing!")
