for a in range(10):
    if a==5:              #When a will become 5.Python will skip the command only for 5,after that it will continue.
        continue          #Continue is used to skip some values.               
    print(a)

# A program to type only even numbers

for b in range(101):
    if b%2 ==1:                 #This will not print all thtose numbers who give remainder 1 when divided by 2. (Odd numbers)
        continue
    print(b)

#A program to type only odd numbers

for c in range(101):
    if c%2 ==0:
        continue
    print(c)

