y = int(input("Upto what you want prime numbers\n"))

z = y+1

l1 = []                          # This program prints prime numbers upto a range defined by user.
l2 = []


for m in range(2,z):
    l1.append(m)

l = len(l1)    

for i in range(0,l):
    a = l1[i]            

    prime = True

    for b in range(2,a):
        if a%b == 0 :
            prime = False
            break
    if prime:
        l2.append(a)
    
    else:
        pass

print(l2)
    