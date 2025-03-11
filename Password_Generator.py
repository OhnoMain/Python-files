import random

password = ["nebula", "catalyst", "synergy", "mosaic", "horizon", 
            "quasar", "luminary", "cascade", "aether", "verdant", 
            "zephyr", "eclipse", "prism", "zenith", "cosmos", 
            "serenity", "fusion", "atlas", "paradigm", "echo"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "~", "?"]

keywords = False
print("""
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--'

                made by Ohno

              Password Generator \n
""")

secure = int(input("\nHow secure should your password be? (1-10): "))
keywordChoice = input("Do you want to enter any keywords? (y/n): ")
if keywordChoice.lower() == "y":
    keyword = input("What keyword should we include in your password?: ")
    keywords = True

# Low security levels
secureNum = 3 if secure < 5 else secure

# Make the password
generated_password = []
for _ in range(secureNum):
    # Choose things
    choice = random.choice(["word", "number", "special"])
    if choice == "word":
        generated_password.append(random.choice(password))
    elif choice == "number":
        generated_password.append(random.choice(numbers))
    elif choice == "special":
        generated_password.append(random.choice(special_chars))

# Add keyword
if keywords:
    generated_password.insert(random.randint(0, len(generated_password)), keyword)

# Displaying the password
final_password = "".join(generated_password)
print(f"\nYour generated password is: {final_password}")
