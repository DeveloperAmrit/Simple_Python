lst = [x**2 for x in range(10)]
print("list 1",lst)

lst2 = [x**2 for x in range(10) if x%2!=0]           # list of sqaure of all odd numbers till 10
print("list 2",lst2)

lst3 = [x**2 if x%2==0 else x for x in range(10)]    # You cannot put if...else after the for if you're using else.
print("list 3",lst3)

lst4 = [x if x % 2 == 0 else x**2 for x in range(10) if x > 5] 
print("list 4",lst4)

lst5 = [x for x in range(10) if x % 2 == 0 and x % 3 == 0]
print("list 5",lst5)


# Nested list comprehension

lst6 = [x+y for x in range(1,10) for y in range(1,3)]
print("list 6",lst6)

lst7 = [(x,y) for x in range(1,10) for y in range(1,3)]
print("list 7",lst7)

lst8 = [(x,y) if(x%2==0) else x-y for x in range(1,10) if(x>4) for y in range(1,8) if y>5]
print("list 8",lst8)
