a = int(input("Enter the number of rectangles you want in a form of ladder\n"))

for b in range(0,a):                                 # This will create a design
    print(  " " ,"#"*a)
    print(" #"*1 , " "*(a-2), "#"*1)
    

print(  " " ,"#"*a)                                 #This is to complete the design.