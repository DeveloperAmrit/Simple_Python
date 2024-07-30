for a in range(1,10):
    print(a)
else:                                    #ELSE is used with for_loop.
    print("Loop ended")                  #The command written in ELSE is executed when loop ends successfully.

for b in range(10):
    print(b) 
    if b==5: 
        print("Loop breaked")            #When the value of b will become 5 the loop will get breaked.
        break                            #When loop breaks , loop ends but NOT successfully.
else:                                    #The loop will end unsuccessfully. so,the else command will not be executed.
    print("Loop ended successfully")

#The same can be applied for while loop.

for b in range(10):
    print(b) 
    if b==11:                          #If value of b will reach 11 loop will break.                     
        break                          #Value of b cannot be 11, so loop will not break and end successfully.
else:                                    
    print("Loop ended successfully")
