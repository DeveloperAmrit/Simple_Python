a = {1,2,3,4,8,9,30,100,4048,343,201}              #This is a SET.

print("A simple set is",a)       

b = set()                                         #This is an empty set
print("This is empty ",b)
b.add(90)     
b.add(87)                                         # Add function of SET inserts new items in the SET.                                     
b.add("Amrit") 
print( "Modified empty  set b is"  ,b)              # SET donot adds repeated items.

b.add((4,5,6,7,))                                 #Tuples (NOT lists)   can be added in SETS.
print("This is tupled SET b \t",b)         

print(len(b))                                    #len() counts the number of itmes in the SET.

b.remove(90)                                     #This will remove 90 from the SET.
print("Removed 90\t",b) 

b.add(1)
b.add(2)
print("New modified set b is",b) 
print("Common items in list a and b are",b.intersection(a))     # This will print only those items who are common in both lists a and b.

b.pop()                                                         #This removes any random item from the SET.
print("poped SET is \t",b) 

