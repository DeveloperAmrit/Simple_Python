print(''' Rules of the game are:-
          1> Type 1 for stone
          2> Type 2 for paper
          3> Type 3 for scissors  ''')          # This is duo palyer game.

player1 = input("Enter player1's name\n")
player2 = input("Enter player2's name\n")

a = int(input(  player1+"'s turn. Enter 1 for stone , 2 for paper , 3 for scissors.\n"))
b = int(input( player2+"'s turn. Enter 1 for stone , 2 for paper , 3 for scissors.\n"))


if a==1 and b ==2 :
    print(player2,"is winner!")
elif a==1 and b==3:
    print(player1,"is winner!")

if a==2 and b==1:
    print(player1,"is winner!")
elif a==3 and b==1:
    print(player2,"is winner!")

if a ==2 and b==3:
    print(player2,"is winner!")
elif a ==3 and b ==2:
    print(player1,"is winner")

if a==b:
    print("Match draw!")




