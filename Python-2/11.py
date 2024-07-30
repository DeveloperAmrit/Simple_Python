class operations(): 
    def square(self):                                                       
        print("square of",self.num, "=" , self.num ** 2)       # ** in python stands for power ^. like 5^2 = 25 also 5**2 = 25  
     
    def cube(self):                                              #We are taking same elemets for all functions to use any with same data.
        print("The cube of",self.num,"=", self.num ** 3)

    def squareroot(self):
        print("The square root of",self.num,"=", self.num ** 0.5)

    
    
    
a = operations()

a.num = int(input("Enter the number\n"))


a.square()
a.cube()
a.squareroot()

