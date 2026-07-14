inchar = input("Input one character:")
if inchar >= 'A' and inchar <= 'Z' :
    print("Yor in put Upper case Latter " , inchar)
elif inchar >= 'a' and inchar <= 'z' :
    print("Yor in put Loewer Case Letter ", inchar)
elif inchar >= '0' and inchar <= '9' :
    print("You in put Nember ", inchar)
else :
    print("It's not a letter or number.", inchar)