print(
    "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"
)
door = input("> ")
if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
# Study drill..
elif door == "3":
    print("The room is set to fire: ")
    print("1. Run between the fire and escape.")
    print("2. Stay there and wait to grill.")
    death = input("> ")
    if death == "1":
        print("You make it out alive! Congratulations!")
    else:
        print("You are now in Heaven. Let's Party!!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
