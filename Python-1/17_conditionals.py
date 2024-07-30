a = input("Enter the   number\n")                  
a = int(a)                         
                                                               #Following is called if-elif-else ladder.
if(a>10):                                                      #Python will print the first true if or elif.
    print("The value of",a,"is greater than 10")               #elif is secondary if.
elif(a==10):
    print("The value of",a,"is equal  to 10")                  # You can also use this in "if" by using (>=) sign.
else:
    print("The value of",a,"is less than 10")                  #  If none of the ifs or elifs became true, PYTHON will execute the command writen in else.

b = input("Enter the number")                      
b = int(b)

if(b>0):                                       # This is an independent if without else statement.
    print(b,"is a positive integer")           #If its condition satisfies it will be executed.
                                               #if its condition is not satisfied , nothing will happen.                                                             