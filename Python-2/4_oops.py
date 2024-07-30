class amrit():                                 #class consist of a object. Here object 1 is amrit().
         def a(self):                           # Objedct is the collection of functions.
             print("Name is ",self.name)             #Each function uses some elements.            
             print("Roll no is", self.roll)         # self is later replaced by a variable.  
                                                    #These elements are filled when the function is to be called.
         def b(self):
             print("sum is ",self.num1  + self.num2)     #Here,elements are num1 and num2.
      



c = amrit()                                   # When we call a class.All its functions are called.
                                              #You can use the functions as you desire.
c.name = "Alok ranjan"                        #You just have to fill elements of the function that you are going to call. 
c.roll = "5"                                  # Here we have to call a() so we are filling elements of a()

c.a()                                         #We called the function and function will do its work if all of its elements are pr-filled.

c.num1 = 7                                    # NOW,we are going to call b() so we are filling its elements.
c.num2 = 19

c.b()                                         #We called the function and function will do its work if all of its elements are pr-filled.

