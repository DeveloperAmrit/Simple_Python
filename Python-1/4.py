a = "Amrit"       # An +ve index starts with 0. -ve index starts from end of the name.-ve index starts with -1.
print(a[1:2])       
print(a[0:5])         #This will print from index 0 to 4 only. NOT 5.
print(a[-6:-1])       #This will print from index -6  to -2 and NOT -1.
print(a[-1])          #This will print the last letter ( first letter from end).
print(a[0])           #Thsi will print the first letter.
print(a[4])           #Thsi will print last letter.
print(a[:4])          #Python will interpret blank space as minimum index that,in this case, is 0. It will print 0 to 3. NOT 4.
print(a[0:])          #Python will interpret blank space as maximum index that , in this case, is 5.It will print 0 to 4.
print(a[0:5])         #This is as same as print(a[0:]) . 5 is not index here but we use this to print 0 to 4.
print(a[2:])          # This will print 2 to 4. NOT 5.
b = "Anurag" 
print(b[0:])          #This is as same as print(b[0:6]). If we donot know the last index we may left it as blank.
print(b[0:6])         #This is as same as print(b[0:]) . 
print(b[0:6:2])       #This will print every 2nd character of the string b.Printing will strat with 1st character then 1+2=3rd charcter then 3+2= 5th carachter.
c = "123456789"
print(c[0::3])         #This will print every 3rd character of the string b.Printing will strat with 1st character then 1+3=4th charcter then 4+3= 7th carachter.
print(c[1::3])         #This will print every 3rd character of the string b.Printing will strat with 2nd character then 2+3=5th charcter then 5+3= 8th carachter.