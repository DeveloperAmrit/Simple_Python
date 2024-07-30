a = int(input("Enter the number\n"))               #This is a program to check whether a given numbe is prime or not.

prime = True

for b in range(2,a):
    if a%b == 0 :
        prime = False
        break
if prime:
    print("This is a prime number")
else:
    print("This is a composite number")