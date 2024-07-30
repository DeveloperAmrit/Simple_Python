

class employee:
    salary = 100
    location = "Delhi"
    company = "Honda"


# What if we want to change values of attributes of this class.
#We can create a instace attribute

Amrit = employee()

print(Amrit.salary)

Amrit.salary = 200          # This is an instance attribute who change the value of salary attribute ONLY  for Amrit.

print(Amrit.salary)

# BUT what if we want to change the value of salary attribute permanently.
# We can do the following.

class employee:
    salary = 100
    location = "Delhi"
    company = "Honda"

    def changesalary(self,new_salary):
        self.__class__.salary = new_salary         # __F__  type methods are called denter methods. 

Alok = employee()

Alok.changesalary(300)

print(Alok.salary)









 