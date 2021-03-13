from tkinter import *
import random
root = Tk()
root.configure(bg='gray')
# This is where all the variables used later are set
level = 1
gold = 0
attackPower = 1
bossHealth = 0
knightCounter = 0
archerCounter = 0
assassinCounter = 0
mageCounter = 0
giantCounter = 0
knightValue = 10
archerValue = 50
assassinValue = 250
mageValue = 1000
giantValue = 5000
labelTextColor = "lime"
labelBackgroundColor = "gray"
buttonBackgroundColor = "lime"
buttonTextColor = "black"


# These functions allow you to buy heroes
def buy_knight():
    global gold
    global attackPower
    global knightValue
    global knightCounter
    if gold >= knightValue:
        gold -= knightValue
        knightValue = round(knightValue * 1.5)
        attackPower += 1
        knightCounter += 1
        currentGold.configure(text=f"Gold: {gold}")
        knightButton.configure(text=f"Knights: {knightCounter} \n Cost: {knightValue}")


def buy_archer():
    global attackPower
    global gold
    global archerValue
    global archerCounter
    if gold >= archerValue:
        gold -= archerValue
        archerValue = round(archerValue * 1.5)
        attackPower += 3
        archerCounter += 1
        currentGold.configure(text=f"Gold: {gold}")
        archerButton.configure(text=f"Archers: {archerCounter} \n Cost: {archerValue}")


def buy_assassin():
    global gold
    global attackPower
    global assassinValue
    global assassinCounter
    if gold >= assassinValue:
        gold -= assassinValue
        attackPower += 10
        assassinCounter += 1
        assassinValue = round(assassinValue * 1.5)
        currentGold.configure(text=f"Gold: {gold}")
        assassinButton.configure(text=f"Assassins: {assassinCounter} \nCost: {assassinValue}")


def buy_mage():
    global gold
    global attackPower
    global mageValue
    global mageCounter
    if gold >= mageValue:
        gold -= mageValue
        attackPower += 25
        mageValue = round(mageValue * 1.5)
        mageCounter += 1
        currentGold.configure(text=f"Gold: {gold}")
        mageButton.configure(text=f"Mages: {mageCounter} \nCost: {mageValue}")


def buy_giant():
    global gold
    global attackPower
    global giantValue
    global giantCounter
    if gold > giantValue:
        gold -= giantValue
        attackPower += 100
        giantCounter += 1
        giantValue = round(giantValue * 1.5)
        currentGold.configure(text=f"Gold: {gold}")
        giantButton.configure(text=f"Giants: {giantCounter} \nCost: {giantValue}")


# This is the function that is called when using the attack/spawn button
def attack():
    global bossHealth
    global attackPower
    global level
    global gold
    if bossHealth > 0:
        bossHealth -= attackPower
        currentHealth.configure(text=f"Boss Has {bossHealth} Health")
        if bossHealth < 0:
            bossHealth = 0
    if level >= 15 and bossHealth <= 0:
        bossHealth = (level ** 3) * (random.randint(25, 30))
        currentHealth.configure(text=f"Boss Health: {bossHealth}")
        gold = round(gold + ((level ** 2) * random.randint(3, 5)))
    if bossHealth <= 0:
        currentHealth.configure(text="Boss Health: 0")
        bossHealth = (level ** 2) * (random.randint(15, 20))
        currentHealth.configure(text=f"Boss Health: {bossHealth}")
        gold = round(gold + (level * (random.randint(1, 3))))
    currentHealth.configure(text=f"Boss Health: {bossHealth}")
    currentGold.configure(text=f"Gold: {gold}")


# These 2 functions allow the user to change the level that they are on
def next_level():
    global level
    if level <= 29:
        level += 1
        currentLevel.configure(text=f"Level: {level}")


def prev_level():
    global level
    if level >= 2:
        level -= 1
        currentLevel.configure(text=f"Level: {level}")


# Where labels are created and placed
currentGold = Label(text="Gold: 0", font=('', 15), bg=labelBackgroundColor, fg=labelTextColor)
currentGold.place(x=140, y=0)

currentLevel = Label(text="Level: 1", font=('', 15), bg=labelBackgroundColor, fg=labelTextColor)
currentLevel.place(x=390, y=0)

prevButton = Button(text="<---- Previous Level", command=prev_level, bg=buttonBackgroundColor, fg=buttonTextColor,
                    width=16)
prevButton.place(x=0, y=0)

nextButton = Button(text="Next Level ---->", command=next_level, bg=buttonBackgroundColor, fg=buttonTextColor, width=16)
nextButton.place(x=486, y=0)

mainAttack = Button(text="Attack/Spawn", command=attack, font=("", 12), bg=buttonBackgroundColor, fg=buttonTextColor)
mainAttack.place(x=249, y=25)

currentHealth = Label(text="Boss Health: 0", font=('', 15), bg=labelBackgroundColor, fg=labelTextColor)
currentHealth.place(x=235, y=0)

# Where the buttons are created and placed
knightButton = Button(text=f"Knights: {knightCounter} \nCost: {knightValue}", width=10, command=buy_knight,
                      bg=buttonBackgroundColor, fg=buttonTextColor)
knightButton.place(x=163, y=85)

archerButton = Button(text=f"Archers: {archerCounter} \nCost: {archerValue}", width=10, command=buy_archer,
                      bg=buttonBackgroundColor, fg=buttonTextColor)
archerButton.place(x=263, y=85)

assassinButton = Button(text=f"Assassins: {assassinCounter} \nCost: {assassinValue}", width=10,  command=buy_assassin,
                        bg=buttonBackgroundColor, fg=buttonTextColor)
assassinButton.place(x=363, y=85)

mageButton = Button(text=f"Mages: {mageCounter} \nCost: {mageValue}", width=10, command=buy_mage,
                    bg=buttonBackgroundColor, fg=buttonTextColor)
mageButton.place(x=213, y=135)

giantButton = Button(text=f"Giants: {giantCounter} \nCost: {giantValue}", width=10, command=buy_giant,
                     bg=buttonBackgroundColor, fg=buttonTextColor)
giantButton.place(x=313, y=135)

exitButton = Button(text="Click Here To Exit", command=root.destroy, bg="red")
exitButton.place()

root.title("Clicker Game")
root.geometry("600x200")
root.mainloop()
