# inheritance is used to create new class from existing class and making changes in previous class.

class employee:                                        # This is parent class.
    company = "Google"
    def details(self):
        print("This is an employee")

Amrit = employee()

Amrit.details()


class programmer(employee):                                # This is first child class.
    language = "Python"                                    #We made changes in its details.
    def details(self):                                    
        print( "This is a programmer working in ",employee.company ,"with", programmer.language , "language")

Alok = programmer()

Alok.details()


class head(employee):                                  # This is second child class. Both are single inheritence.
    def details(self,name,branch):
        self.branch = branch
        self.name = name
        print(self.name ,"is a head of",self.branch,"branch")


Anjali = head()

Anjali.details( "Anjali","Chapra")