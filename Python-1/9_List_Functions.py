l1 = [98,78,1,46,2,987,37,8,9,6,2]                       #List is in [big] brackets.
print(  "Unsorted list:" ,l1)                            # This will print a UNSORTED list.

print( "Sum=" ,sum(l1))             #This will print sum of all itmes in l1
                          
l1.sort()                           # sort() function sorts the list in INCREASING order.
print( "Sorted list:", l1)          # This will print a SORTED list.

l1.reverse()                        # reverse() function reverses the list.
print( "Reversed list:" ,l1)        # This will print a Reversed list.

l1.append(100)                      # This will add new item "100" at the end of the list. You can further command to sort this list too.
print("Appended 100 :" , l1)  

l1.insert(0,18)                     # This will first shift the number at index 0 to 1.Then, will add 18 at index 0.
l1.insert(3,45)                     # This will insert 45 at 3 index.
print(  "Inserted list:"  , l1)

l2 = [0,1,2,3,4,5,6,7,8,9]
print("second list",l2)
l2.pop(-1)                          #This will remove (DELETE) the number at index -1.
l2.pop(0)                           #This will remove the number at index 0.
l2.remove(4)                        #This will dirctly remove the first occurance of item named 4 from the list irrespective of its index.
print("poped list" ,l2)

l3 = ["a","b","c","d","e","z","g","h","i","j"]           #List can contain any thing.
print(   "Third list:"  ,l3)
l3.sort()                                                #Sort() can sort any type of list.
print("Sorted list",l3)
