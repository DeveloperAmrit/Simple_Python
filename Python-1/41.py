a = float(input("Input the first number\n"))        # This program finds largest number of three numbers given.
b = float(input("Input the second number\n"))   
c = float(input("Input the third number\n"))

if (a>b):
    if(a>c):
        print( "The largest number is"  ,a)
    else:
        print( "The largest number is"  ,c)
else:
    if(b>c):
        print( "The largest number is"  ,b)
    else:
        print(    "The largest number is"  ,c)

    
    