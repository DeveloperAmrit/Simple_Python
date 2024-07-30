class employee:                                 # This is parent or super class.
    company = "B.V.P chhapra"
    def details(self):
        print("I am working in",employee.company)







class teacher(employee):                       # This is first child.
    standard = "10th"

        
    def details(self):
        
        super().details()                        #super() fetches information from the parent class.And run the functions present in the parent class.  

        print("I am a techer of class", teacher.standard,"in",teacher.company)

Prince = teacher()

Prince.details()                            # This will print BOTH function in teacher class and employee class as super() is there in teacher class.




class principal(teacher):
    name = "Mr. Digraj singh rajput"

    def details(self):
        
        super().details()
        print("I am the pricipal of ", principal.company,)

a = principal()

a.details()              #Due to super() the teacher class function will also be executed.
                         #BUT the teacher class function also ha super() so the functions of employee class will also be executed.