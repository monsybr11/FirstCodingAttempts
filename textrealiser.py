abc = input("Type any text in.\n")

abc = str(abc)  # converting the input to a string in case of text and digits being used.

if abc.islower() is True:
    print("the text is lowercase!")

if abc.isupper() is True:
    print("the text is Uppercase!")

if abc.isupper() is False and abc.islower() is False and abc.isnumeric() is False and abc.isdigit() is False:
    print("The text is mixed!!!")  # so many "and" uses to make sure that one output is chosen.

if abc.isnumeric() is True:
    print("these are numbers!")
