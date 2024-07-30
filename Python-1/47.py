a = open( "45_1.txt", "rt")

b = a.readline()       #This is first read line command so will read only first line.
print(b)

b = a.readline()       #This is second read line command so will read only second line.
print(b)

b = a.readline()       #This is third read line command so will read only third line.
print(b)
           

a.close()