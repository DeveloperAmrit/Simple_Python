# inheritance is used to create new class from existing class and making changes in previous class.

class employee:                                        # This is parent class.
    company = "Google"
    def details(self):
        print("This is an employee")

Amrit = employee()

Amrit.details()


class programmer(employee):                                # This is child class.
    language = "Python"                                    #We made changes in its details.
    def details(self):                                    
        print( "This is a programmer working in ",employee.company ,"with", programmer.language , "language")




Alok = programmer()

Alok.details()
