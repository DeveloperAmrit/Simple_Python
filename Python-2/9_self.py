class Employee(): 
    def salary(self):                                                       
        print("Salary is 10k")

Amrit = Employee()



# When we type

Amrit.salary()

# This get converted in 

Employee.salary(Amrit)

# Here salary function has some argument/object.
# We must put a place for this object in our function of class. So we put "pass" as an empty place for later elements.

# If we will not place self. Error will occur and say Employee.salary() takes 0 positional arguments but 1 was given.

# The 1 argument is "Amrit". BUT, the function has no place for it (if self is removed).