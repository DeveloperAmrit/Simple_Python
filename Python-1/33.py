a = int(input("Enter the range upto which you want product\n"))    
if(a==0):
    print("Please enter a valid value")        #This program shows the product of first a natural numbers.i.e 1*2*3*4
    exit()                                     #This is also called factorial of a.
                                       
b = 0
product = 1

for c in range(b,a):                                   
    b = b + 1
    product = product*b
    
print(  "Factorial of ",a,"is" ,product)