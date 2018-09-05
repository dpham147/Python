import random
import time

def displayIntro():
    print('''You are lost in a cave full of dragons. You must make
your way to the exit, but each path you take could give you 
treasure, or a quick death. Follow the clues and survive.''')
    print()


def generateCave():
    badEnd = random.randint(1, 2)
    if badEnd == 1:
        print('Towards your LEFT is a clear path leading to a dark cave.')
        print('Towards your RIGHT you see the faint glint of metal sunken in the ground.')
    if badEnd == 2:
        print('Towards your LEFT in the ground lays an ornate sword laden with pristine gems.')
        print('Towards your RIGHT lies a muddy trail continuing into the darkness.')
    return badEnd

def chooseCave():
    cave = ''
    while cave != 'LEFT' and cave != 'RIGHT':
        print('Which cave will you go into? (Left or Right)')
        cave = input().upper()

    return cave


def checkCave(chosenCave, badEnding):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)

    if (badEnd == 1 and chosenCave == 'RIGHT') or (badEnd == 2 and chosenCave == 'LEFT'):
        print('The air around you suddenly becomes humid...')
        time.sleep(1)
        print('You hear a roar that pierces your senses as you tremble to the ground.')
        time.sleep(1)
        print('A voice calls out to you')
        time.sleep(1)
        print('PUNY HUMAN. YOU DARE DEFILE MY HOME WITH YOUR INSATIABLE GREED')
        time.sleep(1)
        print('NOW PERISH')
        time.sleep(1)
        print('The world around you begins to spin until - thud.')
        print('Your vision falls to the ground as you lay your eyes on your headless corpse.')
        return False
    else:
        print('The cave opens up to you to reveal yet another two caves.')
        print()
        time.sleep(2)
        return True

def goodEnd():
    print('You are interrupted by rumbling earth.')
    time.sleep(2)
    print('The stone above you begins to crumble, giving way to the sky above...')
    time.sleep(2)
    print('And a dragon')
    time.sleep(3)
    print('It calls out to you...')
    time.sleep(2)
    print('Your lack of avarice moves me, child')
    time.sleep(1)
    print('Take this as a token of my respect.')
    time.sleep(2)
    print('Now leave this place before I change my mind.')
    time.sleep(2)
    print('I tire of humans quickly.')
    time.sleep(2)
    print('You take the dragon\'s gift and scurry out the cave.')
    print()


playAgain = 'YES'
goodEnd = True
ending = 5
room = 0
while playAgain == 'YES' or playAgain == 'Y':
    displayIntro()

    while goodEnd and room < ending:
        badEnd = generateCave()
        caveNumber = chooseCave()
        goodEnd = checkCave(caveNumber, badEnd)
        room = room + 1

    if goodEnd:
        goodEnd()

    print('Do you want to play again? (yes or no)')
    playAgain = input().upper()
