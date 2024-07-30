a = [1,2,3,4,5,6,7,8,9,"Amrit","Alok","Mango",95.99]
                                                         #For loop is easier than while loop.
for item in a:
    print(item)                                          #This will print all items in list a.

for b in range(8):                                       #This will print numbers from 0 to 7 (Not 8).
    print(b)

for c in range(1,8):                                    # This will print from 1 to 7. (Not 8)
    print(c)                    

for d in range(1,8,2):                                 # it is range(start,stop,step)  format.
    print(d)                                           #This will print from 1 to 7 with a step jump of 2.
                                                       #This will print 1 then 1+2=3 then 3+2=5 then 5+2=7. Like in list list functions.
