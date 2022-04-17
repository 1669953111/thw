from sys import exit

def dead(why):
    print(f"{why}, good job!")


#start game
print("""
You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input("> ")

    if bear == "1":
        dead("The bear eats your face off.")
    elif bear == "2":
        dead("The bear eats your leg off.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
    exit(0)

if door == "2":
    print("Your stare into the endless abyss at Cthuhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Under standing relovers yellow melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        dead("Your body surives powered by a mind of jello.")
    else:
        dead("The insanity rots your eyes into a pool of muck.")
    exit(0)

else:
    dead("You stumble around and fall on a knife and die.")
    exit(0)
