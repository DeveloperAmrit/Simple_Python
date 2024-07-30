myDict = {
    "Apple" : "A red colored delicious and nutritious fruit , grown in colder regions",
    "Amrit" : "A uselesss person without brain.Also called Baklol",
    "Anurag": "A very cute and nice man.Also called kitty ",
    "Alok"  : "A very cute , responsible and nice man.Also called Duta",
    "Anjali": "A very cute , responsible , hardworking and nice girl.Also called julia",
}
print( "Amrit is" ,myDict["Amrit"])              #This will print definition of Amrit as given in your dictionary.

myDict["Alok"] = "only DUTA"                     #Keys in dictionary canbe modified.
print( "Alok is" ,myDict["Alok"])

print("Keys are",myDict.keys())                  #This will print all keys of the dictionary.

print("Values are",myDict.values())              #This will print all values in the dictionary.

print(myDict.items())                            #This will print all keys + values of the dictionary.

UpdatedDict = { 
     "Mango" : "A delicious fruit",
     "Orange" : "A citrus fruit",
}

myDict.update(UpdatedDict)                       # This will update myDict and add new items
print("Updated ",myDict)                         #This is updated myDict.
print("Orange is a",myDict["Orange"])            #New item "Orange"  is available.

print(myDict.get("Guava"))                       #Guava is not in list so it will show NONE as reasult.
 # print(myDict["Guava"])                        #Direct printing (Without using .get ) will throw an error.