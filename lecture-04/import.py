import random
print("What is my magic number (1 to 1..) ?")
number = random.randint(1,100)
ntries = 1
yourguess = 1
while ntries <7 and yourguess == number:
    msg = str(ntries) + ">>"
    if(ntries == 6):
        print("your last chance")
    yourguess = int(input(msg))
