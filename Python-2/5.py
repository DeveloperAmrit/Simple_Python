class operations(): 
    def sum(self):                                                       
        print(self.num1,"+",self.num2 , "=" , self.num1 + self.num2)
     
    def difference(self):                                              #We are taking same elemets for all functions to use any with same data.
        print( self.num1,"-",self.num2,"=", self.num1 - self.num2 )

    def product(self):
        print( self.num1,"*",self.num2 ,"=", self.num1 * self.num2)
    
    def divison(self):
        print(self.num1 ,"/", self.num2,"=",self.num1/self.num2)



a = operations()

a.num1 = int(input("Enter first number\n"))
a.num2 = int(input("Enter second number\n"))

a.sum()
a.difference()
a.product()
a.divison()    