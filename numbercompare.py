a = input("put the first number in.\n")
b = input("put the second number in.\n")
c = input("put the third number in.\n")

choice = input("do you want the biggest or the smallest number? [big/small/both]\n")

str(choice)
str(a)
str(b)
str(c)

if choice == "big":
    print("this is the biggest number: " + max(a, b, c))

if choice == "small":
    print("this is the smallest number: " + min(a, b, c))

if choice == "both":
    print("this is the biggest number: " + max(a, b, c))
    print("this is the smallest number: " + min(a, b, c))
