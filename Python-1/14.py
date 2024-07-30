a = { 1,2,3,90,4,4,5,2,6,7,}                           # A set is written in {middle} brackets.
b = { "Mango","Orange", "Mango","Apple"}               #Sets donot allow repeated  items.
print(a)                                               #They automatically sort the items(integers).       
print(b)

c = set()                                             #This creates an empty set.
print(type(c))                                       

#DIFFERENCE BETWEEN LIST[] , TAPLES()  , Dictionary{}    and   SETS{}
#LIST , Dictionary and SETS can be modified.
#TAPLES  cannot be modified.

d = [ "amrit","alok", "Anjali","Anurag"]
print(d,       "\t\tThis is a"    ,type(d))                                     # This is a list.

e = ("Kitty", "Duta" ,"Flamingo","Badmingo")                        
print(e,"\t\tThis is a ",type(e))                                                # This is a taple.

f = {
    "Apple" : "A red colored delicious and nutritious fruit , grown in colder regions",
    "Amrit" : "A uselesss person without brain.Also called Baklol",
    "Anurag": "A very cute and nice man.Also called kitty ",
    "Alok"  : "A very cute , responsible and nice man.Also called Duta",
    "Anjali": "A very cute , responsible , hardworking and nice girl.Also called julia",
}
print(f,"\t\tThis is a" , type(f))                                               #This is a dictionary

g = {"Amrit", "Alok","Anurag","Kitty"}                                    
print(g,"\t\tThis is a ",type(g))                                                #This is a SET.