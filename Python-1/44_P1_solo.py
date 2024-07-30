import random                        # random module selects any one item from the list at random

print(''' Rules of the game are:-
          1> Type 1 for stone
          2> Type 2 for paper
          3> Type 3 for scissors  ''')          # This is solo palyer game.


a = int(input("Enter your choice, 1 for stone , 2 for paper and 3 for scissor\n"))

b = random.randrange(0,4)              #random modules range is  like list/index range it also donot covers last one.
                                       #randrange attribute of random module allows to set range for selection.
if a==1 and b ==2 : 
    print("You lose! Computer chosed paper(2) ")
elif a==1 and b==3:
    print("You are  winner! Computer chosed scissor(3) ")

if a==2 and b==1:
    print("You are  winner! Computer chosed stone(1) ")
elif a==3 and b==1:
    print("You lose! Computer chosed stone(1) ")

if a ==2 and b==3:
    print("You lose! Computer chosed scissor(3)")
elif a ==3 and b ==2:
    print("You are  winner! Computer chosed paper(2)" )

if a==b:
    print("Match draw! Both choosed",a)

if a>3 :
    print("Please enter a valid value. 1 for stone , 2 for paper and 3 for scissor")