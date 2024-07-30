class Employee:                            #The class name is employee. Company is its alltibute.
    company = "Google"                     #The name of the company is google 

Amrit = Employee()                         #Started class.
Alok = Employee()                          #The class has no elements so nothing to fill.


print(Amrit.company)                      #This will print "Google"
print(Alok.company)
    
#We can change the value of attributes of class later also.

Employee.company = "Youtube"              # Changed the value of attribute of Employee class

print(Amrit.company)                      #This will print "Youtube"
print(Alok.company)

