a = int(input("Enter your age\n"))

if(a >= 18 and a <40):                                            # AND means BOTH canditions should be satisfied.
    print("You can work with us for ", 41-a,"years.")
elif(a==40):
    print("You can work with us but you can work only for 1 year.") 
elif(a<=0):
    print("Please enter a valid age.")
else:
    print("Sorry,You cannot work with us. ")



b = int(input("Enter your roll\n"))

if(b==3 or b==4 or b==18 or b==39):                               # OR means any of the conditions should be satisfied.
    print("You are a legend.")
elif(b<=0):
    print("Please enter a valid roll number.") 
else:
    print("Sorry, but you are a FOOL.")




c = [1,2,3,4,5,6,18,19,20,32,33,54,55,67,68,69,70,80,90,100]
d = int(input("Enter your roll number\n"))

if(d in c):                                                      # IN checks wheter the item is in list or not.
    print("You has been SELECTED for JEE") 
elif(d<=0):
    print("Please enter a valid roll number")
else:
    print("Sorry, but has NOT been selected, Try again next year")   