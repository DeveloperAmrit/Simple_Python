def sum(num1,num2):
    c = print( "sum of ",num1," and ",num2,"is " ,num1+num2)
    return c 

sum(40,90)
sum(90,890)

a = sum                 #We can also change the name of user defined function indirectly like this.

a(40,90)
a(239,2903)

b = int(input("Enter the first number\n"))
c = int(input("Enter the first number\n"))

a(b,c)