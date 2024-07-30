a = int(input("Enter the first number\n"))          #This program is to check the gratest number between 5 numbers.
b = int(input("Enter the second number\n"))
c = int(input("Enter the third number\n"))
d = int(input("Enter the fourth number\n"))
e = int(input("Enter the fifth number\n"))

if(a==b==c==d==e):
    print(a,b,c,d,e,"are equal")
elif(e>a and e>b and e>c and e>d):
    print(e,"is greatest")
elif(d>a and d>b and d>c and d>e):
    print(d,"is greatest")
elif(c>a and c>b and c>d and c>e):
    print(c,"is greatest")
elif(b>a and b>c and b>d and b>e):
    print(b,"is greatest")
elif(a>b and a>c and a>d and a>e):
    print(a,"is greatest")
