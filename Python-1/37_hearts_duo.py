a = int(input("How many hearts you wnat\n"))            #This program prints hearts

name1 = str(input("Enter name of person1.Name must be of  less than 18 characters \n"))

c = str(input("Enter the name of person 2.Name must be of  less than 18 characters \n"))
s = str(input("Enter the relation between the prsons .must be of  less than 18 characters \n"))

d = int(len(c))
e = int(len(name1))
f = int(len(s))
if len(c) == 18:
    pass
elif len(c)<18:
    c = (" "*(18-d)+c)


if len(name1) == 18:
    pass
elif len(name1)<18:
    name1 = (name1+(" "*(18-e)))

if len(s) == 10:
    pass
elif len(s)<10:
    s = (" "*(10-f)+s)



                                                      
for b in range(0,a):
    print("     ","###","   "," ###","    ")
    print("    ","# "," #","   #","  #")
    print("   ","#   "," #","#  ","   #")
    print("  ","#","     ","#  ","    ","#")
    print(" ","#","     ","  ","       ","#")
    print(" #",name1,"#")
    print(" #",s,"        #")
    print(" #",c,"#")
    print(" ","#","       "," ","      ","#")
    print("  ","#","       "," ","    ","#")
    print("   ","#","       "," ","  ","#")
    print("    ","#","        "," ","#")
    print("     ","#","        ","#")
    print("      ","#","      ","#")
    print("       ","#","    ","#")
    print("        ","#    #")
    print("         ","#  #")
    print("          ","##")
   