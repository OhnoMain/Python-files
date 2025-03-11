
attempts = 3
validPW = False

pword = input("Please enter the password: ")

while validPW == False and attempts >0 :
    if pword != "QWERTY":
        attempts = attempts - 1
        print ("You have entered an invalid password")
        print (f"You have {attempts} attempts left")
        pword = input("Please re-enter your password: ")
    else:
        validPW = True
if validPW == False:
    print("Youve been locked out")
    
print("You're in")

























