a = int(input("How many hearts you wnat\n"))            #This program prints hearts

c = str(input("Enter the name.Name must be of  less than 10 characters \n"))

d = int(len(c))


if len(c) == 9:
    pass
elif len(c)<9:
    c = (" "*(9-d)+c)

else:
    print("Please enter the name of maximum length of 9")
    exit()
                                                      
for b in range(0,a):
    print("    ","## "," "," ##","    ")
    print("   ","#"," #","  #"," #")
    print("  ","#","  ","# #","  ","#")
    print(" ","#","   "," #","    ","#")
    print(" #","    "," ","     "," #")
    print(" #"," ",c,"  #")
    print(" ","#","   "," ","     ","#")
    print("  ","#","   "," ","   ","#")
    print("   ","#","   "," "," ","#")
    print("    ","#","   "," ","#")
    print("     ","#","   ","#")
    print("      ","#"," ","#")
    print("       ","# #")
    print("        ","#")