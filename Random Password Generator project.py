import random

print("Welcome to Devarajan's Random Password Generator")

randomchars = ("ABCDEFGHJIJKLMNOPQSTUVWXYZabcdefghjiklmnopqrstuvwxyz@$&*1234567890")

numberofpassword = int(input("Please Enter the Numnber of Password to be Generated :"))

passwordlength = int(input("Please Enter the Length of the Password to be Generated :"))

print("Here are the passwords :")

for x in range(numberofpassword):
    password = ""
    for chars in range(passwordlength):
        password = password + random.choice(randomchars)
    print(password)

print("Thank You for using Devarajan's Random Password Generator !")
