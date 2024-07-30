import random

name = input("Enter your name\n")
min = int(input("Lower limit\n"))
max = int(input("Higher limit\n"))

r = int(max-min)
b  = random.randrange(min,max)

a = None       # We do this to fix error.
guesses = 0


while a != b:
    guesses = guesses+1
    a = int(input(f"Guess the number between {min} to {max}\n"))

    if a == b:
        print("You guessed right! The number is",b)

    elif a>(b+r/2):
        print("Too high! Think low")
    
    elif a>b:
        print("Little high! Think low")

    elif a<(b-r/2):
        print("Too low! Think high")

    elif a<b:
        print("Little low! Think high" )


print("You got it right in ",guesses,"guesses")
y = (r/guesses)*100
y = int(y)

with open("20_high_score.txt","rt") as f:
      f.readline()            # This wil read the 1st line.
      z = f.readline(3)        # This will read the second line. The previous high score is in 2nd line.
z = int(z)


if y>z :
    print(f"CONGRATULATIONS! .You made a new high score.\nPrevious: {z} \t New: {y}")
    with open("20_high_score.txt","wt") as g:
            g.write(f"Played for range {min} to {max}. High score is\n{y}\nmade by\t{name}")

    
