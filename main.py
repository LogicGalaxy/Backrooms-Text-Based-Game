import time
import json
import os


# ============================================================
# PROJECT INFORMATION
# ============================================================

name = "Backrooms: Command"
version = "1.0.0"

# ============================================================
# GENERATION
# ============================================================

forcedDefaultGeneration = True

whatGenerationToUse = ""
useDefaultGeneration = False
useSeeds = False
useRandomGeneration = False

# ============================================================
# VARIABLES FOR THINGS THE USER CAN DO
# ============================================================

directionToGo = "none"

# ============================================================
# VARIABLES FOR THE ROOMS
# ============================================================

roomID = 1

# ============================================================
# STARTUP MESSAGE
# ============================================================
def startupMessage():
    print(f"Running {name} {version}\n")


# ============================================================
# FUNCTIONS
# ============================================================

def chooseWhatGeneration():
    global useDefaultGeneration
    global useSeeds
    global useRandomGeneration
    global whatGenerationToUse

    if forcedDefaultGeneration == True:
        useDefaultGeneration = True
        useSeeds = False
        useRandomGeneration = False
        time.sleep(0.1)
    else:
        whatGenerationToUse = input("What generation do you want to use?\n1. Default generation (use a predifined map).\n2. Seed generation (use a seed to generate the map).\n3. Random generation (generate more of the map while you explore).\n")
        if whatGenerationToUse == "1":
            useDefaultGeneration = True
        elif whatGenerationToUse == "2":
            useSeeds = True
        elif whatGenerationToUse == "3":
            useDefaultGeneration = True
        else:
            print(f"\n{whatGenerationToUse} is not one of the choices.\n")
            chooseWhatGeneration()


def generationMessage():
    global useDefaultGeneration
    global useSeeds
    global useRandomGeneration

    if useDefaultGeneration == True:
        print("\nUsing the default generation.\n")
        useSeeds = False
        useRandomGeneration = False
        time.sleep(0.1)
    elif useSeeds == True:
        print("\nUsing seed generation.\n")
        useRandomGeneration = False
        time.sleep(0.1)
    elif useRandomGeneration == True:
        print("\nUsing random generation.\n")
        time.sleep(0.1)

# Things the user can do:
def gameInput():
    global directionToGo
    global data
    global roomID

    userInput = input("What do you want to do?\n")

    if userInput.lower() == "go north":
        directionToGo = "north"
        goToDiverentRoom()
        return

    elif userInput.lower() == "go east":
        directionToGo = "east"
        goToDiverentRoom()
        return

    elif userInput.lower() == "go south":
        directionToGo = "south"
        goToDiverentRoom()
        return 

    elif userInput.lower() == "go west":
        directionToGo = "west"
        goToDiverentRoom()
        return

    elif userInput.lower() == "go up":
        directionToGo = "up"
        goToDiverentRoom()
        return

    elif userInput.lower() == "go down":
        directionToGo = "down"
        goToDiverentRoom()
        return

    elif userInput.lower() == "quit":
        print("")
        quit()
    
    elif userInput.lower() == "clear chat":
        print("Clearing the chat...")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        startupMessage()
        generationMessage()
        print("One day, you noclip out of reality. When you open your eyes again, you're lying on the damp carpet of a place you don't recognize.\n")
        print(data["rooms"][roomID-1]["description"])
        gameInput()
        return

    else:
        print(f"You can't do: \"{userInput}\".\n")
        time.sleep(0.9)
        gameInput()
        return


def goToDiverentRoom():
    global data
    global directionToGo
    global roomID

    if directionToGo == "south":
        if data["rooms"][roomID-1]["connections"]["south"] != 0:
            roomID = data["rooms"][roomID-1]["connections"]["south"]

            print(data["rooms"][roomID-1]["description"])
            
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return
        else:
            print(f"You can't go: \"{directionToGo}\".\n")
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return

    if directionToGo == "west":
        if data["rooms"][roomID-1]["connections"]["west"] != 0:
            roomID = data["rooms"][roomID-1]["connections"]["west"]

            print(data["rooms"][roomID-1]["description"])
            
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return
        else:
            print(f"You can't go: \"{directionToGo}\".\n")
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return


    if directionToGo == "north":
        if data["rooms"][roomID-1]["connections"]["north"] != 0:
            roomID = data["rooms"][roomID-1]["connections"]["north"]

            print(data["rooms"][roomID-1]["description"])
            
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return
        else:
            print(f"You can't go: \"{directionToGo}\".\n")
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return

    if directionToGo == "east":
        if data["rooms"][roomID-1]["connections"]["east"] != 0:
            roomID = data["rooms"][roomID-1]["connections"]["east"]

            print(data["rooms"][roomID-1]["description"])
            
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return
        else:
            print(f"You can't go: \"{directionToGo}\".\n")
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return

    if directionToGo == "up":
        if data["rooms"][roomID-1]["connections"]["up"] != 0:
            roomID = data["rooms"][roomID-1]["connections"]["up"]

            print(data["rooms"][roomID-1]["description"])
            
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return
        else:
            print(f"You can't go: \"{directionToGo}\".\n")
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return
    
    if directionToGo == "down":
        if data["rooms"][roomID-1]["connections"]["down"] != 0:
            roomID = data["rooms"][roomID-1]["connections"]["down"]

            print(data["rooms"][roomID-1]["description"])
            
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return
        else:
            print(f"You can't go: \"{directionToGo}\".\n")
            time.sleep(0.33)
            #directionToGo = ""
            gameInput()
            return


def startGame():
    global useDefaultGeneration
    global useSeeds
    global useRandomGeneration
    global data
    global directionToGo
    global roomID

    print("One day, you noclip out of reality. When you open your eyes again, you're lying on the damp carpet of a place you don't recognize.\n")

    if useDefaultGeneration == True:
        print(data["rooms"][0]["description"])

        gameInput()



with open('map.json', "r") as file:
    data = json.load(file)

chooseWhatGeneration()
generationMessage()
startGame()
