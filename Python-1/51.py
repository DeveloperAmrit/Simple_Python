with open("51_5.txt" ,'rt') as a:                
    b = a.read()

c =input("Enter the word you want to find in 51_5.txt \n") 

if (c in b):
    print(   c ,"is present in the file 51_5.txt ")
else:
    print(  c ,"is not present in the file 51_5.txt")