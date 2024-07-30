import os                                  #This program renames files

z = input("Enter  file's name.Ensure you donot have two files of same name.\n")
y  = input("Enter  file's new name\n")


with open(z,"rt") as a:
    b = a.read()

with open(y,"wt") as c:                      #This will make a new file with name y with same content as z has.
    c.write(b)

os.remove(z)                                 # This will delete the old original file

