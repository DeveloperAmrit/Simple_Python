# Multiple inheritance means when a child class inherits from multiple parent classes.

class employee:                                    # This is first parent class.
    company = "Google"
    def details(self,name):
        self.name = name
        self.salary = "$ 200"
        print(self.name,"is an employee of ",employee.company,"earning a salary of ",self.salary)


class programmer:                                   # This is second parent
    language = "Python"
    def details(self,name,country):
        self.name = name
        self.country = country 
        print(self.name,"is a programmer of ", programmer.language,"from",self.country)

class head(employee,programmer):                    # This inherited information from both parent classes i.e company from employee class and language from programmer class.
    def details(self,name,branch):
        self.name = name 
        self.branch = branch
        print("In", head.company,self.name,"is the head of",self.branch,    "branch"  ,"working in",head.language )


Amrit = employee()

Amrit.details("Amrit")

Alok = programmer()

Alok.details("ALok","India")

Anjali = head()

Anjali.details("Anjali","Bihar")

