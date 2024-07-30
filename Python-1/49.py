b = open( "49_3.txt", "at")       # "at" means append text file.
                                  #Unlike the wt ,  at function donot rewrites the file.
b.write("I am appending")         #append adds some new data in the file in the last same line.
b.close()                         # wt and at uses the same function "write" but wt rewrites the file whereas at appends the file.
                                  # As much as times you will run this program it will add new data to the file.

b = open( "49_3.txt", "rt")

c = b.read()
print(c)
b.close
