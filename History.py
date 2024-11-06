# Blank Line

print("\nThe Red Quest.")
input("\nPress enter to continue: ")

# First part.
# Sorry for long text, i wanted this code with not many lines.

print("\nYou successfully find a secret cave, in a quest fo find a sacred treasure. \nHowever you need something to defend. You only got a dartgun and a knive.")
fisrtop = input("\nUse DARTGUN or KNIVE? (Write 'dartgun' or 'knive', any other term will softlock your progress) ")

if fisrtop.lower() == "dartgun":

    input("\nYou find a bear while walking. You use the dartgun, while succesfully hit\nthe bear, the bear resisted and unfortunately you fell unconscious.\n\n\nGAME OVER\n\nRun the program again to retry")
    print("")()

# The reason i put "print("")()" is to crash the game on purpose. The player will not get any further than that.
# Every time i wrote a wrong awnser for testing reasons it will show the intended text but also the next
# part of the game. I forsed a crash so this didn't happen.

if fisrtop.lower() == "knive":
    
    print("\nYou find a bear while walking. You use your knive, you waited until the\nbear attacked and by a flash cut part of his arm. You felt a soft heart attack but managed to survive.")
    input("\nPress enter to continue")

else:
    print("\nYou wrote a unknown term for this question, please run the game again.\n")

# Second part

print("\nYou are at the middle of the cave, while walking you encontured with a long\nwaterfall between the road, then you se a passage of small rocks and a long tree.")
secondop = input("\nWalk through the ROCKS or use the big tree as a BRIDGE? (Write 'rocks' or 'bridge') ")

if secondop.lower() == "rocks":

    print("\nYou start to jump on the rocks, it wasn't easy though. the piranhas on \nthe closer lake came to annoy me and tried to bit my feet.\nBy some miracle i managed to cross the long waterfall lake.")
    input("\nPress enter to continue")

else:
    print("\nYou wrote a unknown term for this question, please run the game again.\n")

if secondop.lower() == "bridge":

    input("\nYou use your previously used knive to cut the long tree to use it as a \nbridge(I wonder why is some vegetation in this cave).\nThe log rolled on a right spot where i could potentially walk through, but unfortunately\nsome piranhas started to eat the log while you were walking through and you fell off.\n\n\nGAME OVER\n\nRun the program again to retry")
    print("")()

# Third part

print("\nFinally, You find out the sacred treasure, a red diamond. But you didn't realised\n that there was a trap while you were holding the red diamond.\n You didn't knew what should happen because rocks started to fall quickly. \nBut you have 3 options.")
print("\nYou could RUN to the nearvy exit, HIDE in the chest, or use your TNT in cases like this.")
thirdop = input("(Choose between 'run', 'hide' or 'tnt'): ")

if thirdop.lower() == "run":

    input("\nYou started to run, managed to avoid most of the rocks, while most of\nthem hurt a lot, i was able to get out...\n But unfortunately it wasn't the case for the shiny red diamond.\nIt broke because of a rock, now it was just shards of something big.\n\n\nBAD ENDING #1 (Just red crystal shards)\n\nBetter luck next time.")
    print("")()

if thirdop.lower() == "hide":
    print("\nYou saw that the chest was big enough to hide yourself in the chest,\nthe only thing i heard inside was loud noices, it was until it stoped\ni saw a light of hope, i'm managed to survive and get this shiny red diamond.\nIt was a exhausted though, but it worth a lot\n\n\nGOOD ENDING !!! (Successful quest!)\n\nCongrats! You are a SUPER PLAYER!")
    input("\nPress enter to continue")

else:
    input("\nYou wrote a unknown term for this question, please run the game again.\n")
    print("")()

if thirdop.lower() == "tnt":
    input("\nYou use your TNT, it was quick enough to break the rock, however it was\npretty risky to use for obvious reasons.\nA big rock closed the exit and you had only 1 TNT box left.\nSadly some rocks befind you were falling faster than usual. And pushed you onto the TNT.\nThe rest... is history...\n\n\nBAD ENDING #2 (FLAT'n'KABOOM)\n\nBetter luck next time.")
    print("")()

print("\nMade By Nicolas B.\n")