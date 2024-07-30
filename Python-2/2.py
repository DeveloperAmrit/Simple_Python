
l1 = ["Donkey","donkey","mote","Mote","Ass","ASS","Dog","dog","ass"]


with open("F:\Python_2_practice\\2_1.txt", "rt") as a:
    b = a.read().lower()                                    #lower() reads the file in lower case .

for li in l1:
    b = b.replace(li,"#####")


with open("F:\Python_2_practice\\2_1.txt","wt") as z:
    z.write(b)



