#startup for AGE GENERATOR: Version 2.0

import time as wait
version_major = '2'
version_minor = '0'

print("WELCOME TO:")
wait.sleep(0.4)

print(f"Age Generator: Version {version_major}.{version_minor}")
wait.sleep(2)

#cancel option added 9-27-21 / removed 4-13-22

# old cancel code at: https://spaceplace.live/agegencancelcode.txt

print("Loading..")
wait.sleep(1.5)

#finding age

isCorrectInput = False

while isCorrectInput == False:

    val = input("Input age: ") 

    age = int(val)

    if age < 10:
        print("Age is too low!")
        wait.sleep(0.8)
    if age > 101:
        print("Age is too high!")
        wait.sleep(0.8)

    if age >= 10:
        isCorrectInput = True


#started new age description chart 9-27-21 "IM ON THE FLOOR LAUGHING"

print("Loading in Magic...")
wait.sleep(1)

#added new code interpretor 4-13-22:

if age >= 10:
    if age < 20:
        print("Age 10 - 19: Young, looking strong! (But geez, these growing pains suck)!")
if age >= 20:
    if age < 30:
        print("Age 20 - 29: Getting older; growing less and less by the day...")
if age >= 30:
    if age < 30:
        print("Age 30 - 39: You have stopped growing altogether. Now the only part of your body that is still developing is your mind.")
if age >= 40:
    if age < 50:
        print("Age 40 - 49: If you weren't before, now your hair is going white, and you may even start to shrink! AAARGH!")
if age >= 50:
    if age < 60:
        print("Age 50 - 59: Alright, now you KNOW you're getting old, because you can't remember what happened when you were 22!")
if age >= 60:
    if age < 70:
        print("Age 60 - 69: You shrink, your skin is wrinkily, and you may have already gon full silver with your hair! These are all signs of getting old!")
if age >= 70:
    if age < 80:
        print("Age 70 - 79: Your skin has become so precious that you need many creams, just to keep it nice and smooth. Your speed is slower, but the wise old mind is still there!")
if age >= 80:
    if age < 90:
        print("Age 80 - 89: Remember the good old days, when your body was like elastic? Sure you do! You'd love to have that feeling. Plus, you dont even know how to use these NEW-FANGELED-YOUNG-PEOPLE-GADGETS!")
        wait.sleep(1)
        print("(Also, why need to take away my driver's liscense!?!?!?!?!?!)")
if age >= 90:
    if age <= 100:
        print("Age 90 - 100: Congrats to you for making it this far. Really, props to you.")

wait.sleep(4)

print("If you enjoyed, stay tuned, as cycoo4 will release a new update soon! You can DM him on Discord at cycoo4#4444. Plus, he posts videos here!: https://www.youtube.com/channel/UC59BSpVifRrk0KV2l963dag")

wait.sleep(1.5)

print("Ending session...")

wait.sleep(1)

exit(0)