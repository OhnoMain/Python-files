import time 

char = ("!", "@", "#", "£", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", ":", "<", ">", "?", "[", "]", ",", ";")
num = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

print("""
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|

        password strength checker
        

            created by Ohno
  """)
print("")
time.sleep(1)

# Get user to enter the password
password1 = input("Please enter the password: ")

# Check password length
while len(password1) < 7:
    print("Your password does not have enough characters...")
    password1 = input("Please re-enter the password: ")
    time.sleep(1)

# Special character 
while any(special_char in password1 for special_char in char) == False:
    print("Your password does not contain any special characters from the list. Please try again.")
    print("")
    print("It must contain at least one of the following characters:", char)
    password1 = input("Please re-enter the password: ")
    print("")

while any(digit in password1 for digit in num) == False:
    print("Your password does not contain any numerical characters. Please try again.")
    print("")
    print("It must contain at least one of the following numbers:", num)
    password1 = input("Please re-enter the password: ")
    print("")



print("It is a strong password")
