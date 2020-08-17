import random

choice = input("Do you want to roll the dice? yes/no\n")

if choice == "no":
    print("ok then why did you run this...????")
    exit()

while choice == "yes":
    print(random.randint(1, 6))
    choice = input("wanna roll the dice again?\n")

else:
    exit()
