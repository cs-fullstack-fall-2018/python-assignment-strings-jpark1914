import os
os.system('clear')



bandMate = "ringo"

# print(len(bandMate))

# print(bandMate.upper())

# print(bandMate.lower())

# print(bandMate[2])

# print(bandMate[1:3])

# print(bandMate[3:])

# ======Challenges=====

# print(reversed(bandMate))
# print(bandMate.capitalize())

# input("What is your name")
# print("The entered string is x characters long")
# print("The entered string is x characters long".upper())

names = [len(input("What is your name?")),len(input("What is your name?")),len(input("What is your name?"))]

if(names[0]>names[1] and names[0]> [2]):
     print("String 1 is longer")
elif(names[1] >names[0] and names[1]>names[2]):
    print("String 2 is longer")
else:
    print("String 3 is longer")
