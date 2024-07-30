a = "Python is very easy to learn and understand"

print(a[0:])                      # For this explanation visite 4.py. # Note counting of indexes starts with 0 and NOT 1.

print(len(a))                     # Len function shows the total number of characters in the string.

print(a.endswith("sjyewi"))       #This tells whether a ends with sjyewi or not. This shows reasults in True and False.
print(a.endswith("understand"))   #This will reasult in TRUE.
print(a.endswith("stand"))        #This will also reasult in TRUE.
print(a.endswith("d"))            #This will also reasult in TRUE.

print(a.count("o"))               #This will count the total numbers of small o in the string a.
print(a.count("P"))               #This will count the total numbers of capital P in the string a.
print(a.count("easy"))            #This will count the total numbers of capital easy in the string a.

b = "my name is Amrit"
print(b.capitalize())             #This will make the first letter of the string b capital. (in the print NOT in the code)

print(b.find("name"))             #This will answer whether "name" is in string or not. If is available then it will print its position.
print(b.find("Anurag"))           #If "Anurag" is not available. It will print -1. 
print(b.find("my"))               #If "my" is available.It will print its position as 0 because the string starts with "my".
print(b.find("i"))                #This function ONLY states the FIRST occurance. i first occurs in "is".

print(b.replace("my name","this"))     #This will replace "my" with "this". It replaces all occurances.


c = "                         I am a   good boy    ."

print(c)                          #This will look odd
print(c.strip())                  #Strip() removes extra space before starting and ending of line.
                                  #Strip() doesnot remove extra space from middle of the line