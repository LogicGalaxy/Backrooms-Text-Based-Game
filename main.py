import time
import json
import os
import threading


# ============================================================
# PROJECT INFORMATION
# ============================================================

name = "Backrooms: Command"
version = "1.3.0"

# ============================================================
# DEV/TESTING VARIABLES
# ============================================================

useTestMode = True

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
whatToGet = "none"
itemsGrabbed = []
inventory = []
whatToUse = "none"
torchUseTime = 30
usesTorch = False

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
        print("Using the default generation.\n\n")
        useSeeds = False
        useRandomGeneration = False
        time.sleep(0.1)
    elif useSeeds == True:
        print("Using seed generation.\n\n")
        useRandomGeneration = False
        time.sleep(0.1)
    elif useRandomGeneration == True:
        print("Using random generation.\n\n")
        time.sleep(0.1)


# Things the user can do:
def gameInput():
    global directionToGo
    global data
    global roomID
    global whatToGet
    global whatToUse

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
    
    elif userInput.lower().startswith("get "):
        if userInput[4:] != "":
            whatToGet = userInput[4:]
            getItem()
        else:
            print("you need to get something to make this command work.")
            gameInput()
            return
    

    elif userInput.lower().startswith("use "):
        if userInput[4:] != "":
            whatToUse = userInput[4:]
            useItem()
        else:
            print("you need to get something to make this command work.")
            gameInput()
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
        print("One day, you noclip out of reality. When you open your eyes again, you're lying on the damp carpet of a place you don't recognize.")
        print("You stand up wondering where you are, as you look around you see that you are in a room leading south.\n")
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
    global inventory
    global usesTorch

    if directionToGo == "south":
        if data["rooms"][roomID-1]["connections"]["south"] != 0:
            roomID = data["rooms"][roomID-1]["connections"]["south"]

            if data["rooms"][roomID-1]["darkRoom"] == "false":
                print(data["rooms"][roomID-1]["description"])
                if inventory:
                    print("Inventory: ", inventory)
            else:
                if usesTorch == False:
                    print(data["rooms"][roomID-1]["description"])
                    if inventory:
                        print("Inventory: ", inventory)
                else:
                    print(data["rooms"][roomID-1]["alternativeDescription"])
                    if inventory:
                        print("Inventory: ", inventory)

            
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

            if data["rooms"][roomID-1]["darkRoom"] == "false":
                print(data["rooms"][roomID-1]["description"])
                if inventory:
                    print("Inventory: ", inventory)
            else:
                if usesTorch == False:
                    print(data["rooms"][roomID-1]["description"])
                    if inventory:
                        print("Inventory: ", inventory)
                else:
                    print(data["rooms"][roomID-1]["alternativeDescription"])
                    if inventory:
                        print("Inventory: ", inventory)
            
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

            if data["rooms"][roomID-1]["darkRoom"] == "false":
                print(data["rooms"][roomID-1]["description"])
                if inventory:
                    print("Inventory: ", inventory)
            else:
                if usesTorch == False:
                    print(data["rooms"][roomID-1]["description"])
                    if inventory:
                        print("Inventory: ", inventory)
                else:
                    print(data["rooms"][roomID-1]["alternativeDescription"])
                    if inventory:
                        print("Inventory: ", inventory)
            
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

            if data["rooms"][roomID-1]["darkRoom"] == "false":
                print(data["rooms"][roomID-1]["description"])
                if inventory:
                    print("Inventory: ", inventory)
            else:
                if usesTorch == False:
                    print(data["rooms"][roomID-1]["description"])
                    if inventory:
                        print("Inventory: ", inventory)
                else:
                    print(data["rooms"][roomID-1]["alternativeDescription"])
                    if inventory:
                        print("Inventory: ", inventory)
            
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

            if data["rooms"][roomID-1]["darkRoom"] == "false":
                print(data["rooms"][roomID-1]["description"])
                if inventory:
                    print("Inventory: ", inventory)
            else:
                if usesTorch == False:
                    print(data["rooms"][roomID-1]["description"])
                    if inventory:
                        print("Inventory: ", inventory)
                else:
                    print(data["rooms"][roomID-1]["alternativeDescription"])
                    if inventory:
                        print("Inventory: ", inventory)
            
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

            if data["rooms"][roomID-1]["darkRoom"] == "false":
                print(data["rooms"][roomID-1]["description"])
                if inventory:
                    print("Inventory: ", inventory)
            else:
                if usesTorch == False:
                    print(data["rooms"][roomID-1]["description"])
                    if inventory:
                        print("Inventory: ", inventory)
                else:
                    print(data["rooms"][roomID-1]["alternativeDescription"])
                    if inventory:
                        print("Inventory: ", inventory)
            
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


def getItem():
    global whatToGet
    global roomID
    global data
    global itemsGrabbed
    global inventory
    global useTestMode

    room = data["rooms"][roomID - 1]

    if whatToGet.lower() in room["objects"]:
        if [roomID, whatToGet] in itemsGrabbed:
            print(f"There is no {whatToGet} here.")
            gameInput()
            return
        else:
            print(f"You picked up the {whatToGet}.")
            itemsGrabbed.append([roomID, whatToGet])
            inventory.append(whatToGet.lower())
            if useTestMode == True:
                # Only prints if you have dev/test mode on
                print(itemsGrabbed)
            print("Inventory: ", inventory)
            gameInput()
            return
    else:
        print(f"There is no {whatToGet} here.")
        gameInput()
        return


def torchCountdown():
    global usesTorch

    time.sleep(torchUseTime)

    usesTorch = False
    print("\nThe torch goes out.\n")

    if data["rooms"][roomID-1]["darkRoom"] == "true":
        if usesTorch == False:
            print(data["rooms"][roomID-1]["description"])
            if inventory:
                print("Inventory: ", inventory)


def useItem():
    global whatToUse
    global roomID
    global data
    global itemsGrabbed
    global inventory
    global torchTimer
    global torchUseTime
    global usesTorch

    room = data["rooms"][roomID - 1]

    if whatToUse.lower() in inventory:

        print(f"You use the {whatToUse}.\n")

        # Remove the item from the inventory
        inventory.remove(whatToUse.lower())

        if whatToUse.lower() == "torch":

            usesTorch = True

            print(f"You can use the torch for {torchUseTime} seconds.\n")

            threading.Thread(
                target=torchCountdown,
                daemon=True
            ).start()

            if data["rooms"][roomID-1]["darkRoom"] == "true":
                if usesTorch == False:
                    print(data["rooms"][roomID-1]["description"])
                    if inventory:
                        print("Inventory: ", inventory)
                else:
                    print(data["rooms"][roomID-1]["alternativeDescription"])
                    if inventory:
                        print("Inventory: ", inventory)

        gameInput()
        return


    else:
        print(f"There is no {whatToUse} in your inventory.")
        gameInput()
        return


def startGame():
    global useDefaultGeneration
    global useSeeds
    global useRandomGeneration
    global data
    global directionToGo
    global roomID
    global whatToGet

    print("One day, you noclip out of reality. When you open your eyes again, you're lying on the damp carpet of a place you don't recognize.")
    print("You stand up wondering where you are, as you look around you see that you are in a room leading south.\n")

    if useDefaultGeneration == True:
        print(data["rooms"][0]["description"])

        gameInput()



with open('map.json', "r") as file:
    data = json.load(file)

startupMessage()
chooseWhatGeneration()
generationMessage()
startGame()
