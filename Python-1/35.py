a = int(input("Enter the number of rows you want filled with stars from centre in a successive manner\n"))

for b in range(0,a):
    print(" "*(a-b-1), end="")
    print("#"*(2*b+1) , end="")
    print(" "*(a-b-1))
