b = open( "48_2.txt", "wt")       #"wt" allows you to re-write a file.
                                  #"wt" first erase the prvious content and then re-writes the file.
                                  #If the file is not available on your device it creates a new file of the same name entered.
b.write("Anurag is so cute")
b.close()


b = open( "48_2.txt", "rt")      #"wt" had re-writed the file so, "rt" will the same data re-writed.

c = b.read()
print(c)
b.close()

# See next in 49.py