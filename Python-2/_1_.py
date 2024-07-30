for a in range(1,21):
    with open(f"tables/table_of_{a}.txt", "wt") as b:
        for c in range(1,11):
            b.write(f"{a}x{c}={a*c}\n")


#This program prints tables from 1 to 20 in different files in table folder.
