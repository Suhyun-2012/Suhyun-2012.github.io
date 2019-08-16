f = open("dictionary.txt", "r")
file = f.readlines()

#ask for birthday
birthyear = input("what is your birth year?")

#ask for password and strip the list
userinput = input("Please enter your password")
list = []
for word in file:
    words = word.strip()
    list.append(words)

#return whether password is good or bad
if userinput in list or birthyear in userinput or "2019" in userinput:
    print("Weak Password")
else:
    print("Perfect Password")

#Extension 1: catch if password is combination of word + birthyear or current year
if userinput in list:
    print()
