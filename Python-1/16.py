s = { 18, "18",18.0 }                                #A SET{} will recongnize these same values as different because of their type.
print(s,"\tThis is a", type(s))                      #A SET() doesnot show repeated values but, here these values  are really different. 
                                                     # SET() recongnized integer and floating number as same and printed only one.
                                                     #BUT,it recongnized string as  different.

a = set()                                            #Created an empty set.
a.add(5)
a.add("5")
a.add(5.0)

print(a, "\tThis set has a length of", len(a) )      #This will the length of the set as 2.
                                                     #Because it has recongnized integer and floating number as same and printed only one.
                                                     #BUT,it recongnized string as  different.