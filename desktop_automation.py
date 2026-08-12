import pyautogui
import time
import ast
import threading
import keyboard



class COCMacro:

    def __init__(self):

        self.macrorunning = False
        self.stopmacro = False
        self.troopselected = False

        self.unitcounter = 1
        self.herocounter = 0


        # Army Troops
        self.usedunits = 0
        self.troopspacecounter = 0
        self.troopunits = 44

        # Army Spells
        self.spellunitsused = 0
        self.spellspacecounter = 0
        self.spellunits = 11

        # Event Elephant Riders
        self.eriderunits = 50
        self.erider_us = 0
        self.erider_sc = 0

        # Event Super Valkyries
        self.svalkunits = 20
        self.svalk_us = 0
        self.svalk_sc = 0


        # Reading Files
        with open("coordinateslist.csv", "r") as file1:
            coordinateslist = ast.literal_eval(file1.read())



        with open("troopdeployment.csv", "r") as file2:
            troopdeployment = ast.literal_eval(file2.read())


        with open("menubuttons.csv", "r") as file3:
            menubuttons = ast.literal_eval(file3.read())


        with open("eventdeployment.csv", "r") as file4:
            eventdeployment = ast.literal_eval(file4.read())


        # Creating Dictionaries
        self.eventdeployment = {

        "erider": eventdeployment[0],
        "svalk": eventdeployment[1],
        "valk": eventdeployment[2],
        "siege": eventdeployment[3],
        "heroes": eventdeployment[4:8],
        "spells": eventdeployment[8]

        }


        self.menubuttons = {

        "bottomleftattackbutton": menubuttons[0],
        "findmatchbutton": menubuttons[1],
        "attackbutton": menubuttons[2],
        "endbattlebutton": menubuttons[3],
        "surrenderconfirmationbutton": menubuttons[4],
        "returnhomebutton": menubuttons[5],

        }


        self.armylocations = {

        "troops&heroes": coordinateslist[:24],
        "earthquakespell": coordinateslist[24:]

        }

        self.army = {

        "valks": troopdeployment[0],
        "loglauncher": troopdeployment[1],
        "heroes": troopdeployment[2:6],
        "earthquake": troopdeployment[6]

        }

        self.herolist = ["Barbarian King", "Grand Warden", "Archer Queen", "Minion Prince"]

        print("\nYou must make sure your resolution is correct before running the program!\n\nOriginal resolution is 2560x1440, with an aspect ratio of 16:9!")

    def resolution(self, resolutionwidth, resolutionheight):


        self.resolutionwidth = resolutionwidth
        self.resolutionheight = resolutionheight

        self.ogresolutionwidth = 2560 #resolution that coordinates are recorded in
        self.ogresolutionheight = 1440 #resolution that coordinates are recorded in

        self.newresolutionscalingpercent = (self.resolutionwidth/self.ogresolutionwidth)

        if (self.resolutionheight / self.ogresolutionheight) != self.newresolutionscalingpercent:
            raise ValueError("Either your aspect ratio is not 16:9 or you have entered the wrong numbers for your resolution!")

        else:

            for coordinate in self.armylocations["troops&heroes"]:
                for index in range(len(coordinate)):
                    coordinate[index] = round(coordinate[index]*self.newresolutionscalingpercent)

            for coordinate in self.armylocations["earthquakespell"]:
                for index in range(len(coordinate)):
                    coordinate[index] = round(coordinate[index]*self.newresolutionscalingpercent)


            for coordinate in self.army.values():


                if coordinate == self.army["heroes"]:
                    for i in coordinate:
                        for index in range(len(i)):
                            i[index] = round(i[index]*self.newresolutionscalingpercent)



                else:
                    for index in range(len(coordinate)):
                        coordinate[index] = round(coordinate[index]*self.newresolutionscalingpercent)

            for coordinate in self.menubuttons.values():
                for index in range(len(coordinate)):
                    coordinate[index] = round(coordinate[index]*self.newresolutionscalingpercent)

            for coordinate in self.eventdeployment.values():

                if coordinate == self.eventdeployment["heroes"]:

                    for i in coordinate:

                        for index in range(len(i)):
                            i[index] = round(i[index]*self.newresolutionscalingpercent)

                else:
                    for index in range(len(coordinate)):
                        coordinate[index] = round(coordinate[index]*self.newresolutionscalingpercent)


    def RunMacro(self):


        while self.unitcounter <= len(self.army):

            if self.stopmacro == True:
                return

            if self.unitcounter == 1:

                if self.troopselected == False:

                    print(f"moving to troop \n{list(self.army.keys())[self.unitcounter-1].upper()}\n")

                    pyautogui.click(self.army["valks"])

                    self.troopselected = True

                else:

                    pyautogui.click(self.armylocations["troops&heroes"][self.usedunits])

                    self.troopspacecounter +=1
                    self.usedunits +=1

                    if self.usedunits >= len(self.armylocations["troops&heroes"]):
                        self.usedunits = 0

                    if self.troopspacecounter >= self.troopunits:
                        self.unitcounter +=1
                        self.troopselected = False


            elif self.unitcounter == 2:

                print(f"moving to troop \n{list(self.army.keys())[self.unitcounter-1].upper()}\n")

                pyautogui.click(self.army["loglauncher"])
                pyautogui.click(self.armylocations["troops&heroes"][0])

                self.unitcounter+=1



            elif self.unitcounter == 3:

                for coordinate in self.army["heroes"]:

                    print(f"{self.herolist[self.herocounter]}")
                    self.herocounter+=1

                    pyautogui.click(coordinate)
                    pyautogui.click(self.armylocations["troops&heroes"][19])
                    pyautogui.click(coordinate)

                self.unitcounter +=1

            elif self.unitcounter == 4:


                if self.troopselected == False:

                    print(f"moving to spell \n{list(self.army.keys())[self.unitcounter-1].upper()}\n")

                    pyautogui.click(self.army["earthquake"])

                    self.troopselected = True

                else:

                    if self.spellspacecounter < self.spellunits:

                        pyautogui.click(self.armylocations["earthquakespell"][self.spellunitsused])

                        self.spellspacecounter+=1
                        self.spellunitsused+=1

                        if self.spellunitsused >= len(self.armylocations["earthquakespell"]):
                            self.spellunitsused = 0

                    else:
                        self.unitcounter+=1
                        self.troopselected = False


    def MacroStart(self):



        if self.stopmacro == True:
            return


        self.macrorunning = True


        threading.Thread(target = self.MacroStopper,
        daemon = True).start()

        #the time sleeps here allow the macro to click the buttons (game has press down cooldown)

        time.sleep(0.75)
        pyautogui.click(self.menubuttons["bottomleftattackbutton"])
        time.sleep(0.75)
        pyautogui.click(self.menubuttons["findmatchbutton"])
        time.sleep(0.75)
        pyautogui.click(self.menubuttons["attackbutton"])

        time.sleep(7) #this time sleep allows the macro to properly find a base during the loading base in the clouds

        self.RunMacro() #runs the actual macro

        if self.stopmacro:
            self.macrorunning = False
            return

        if not self.Wait(10):
            self.macrorunning = False
            return


        #the time sleeps here allow the macro to click the buttons (game has press down cooldown)

        pyautogui.click(self.menubuttons["endbattlebutton"])
        time.sleep(0.75)
        pyautogui.click(self.menubuttons["surrenderconfirmationbutton"])
        time.sleep(0.75)
        pyautogui.click(self.menubuttons["returnhomebutton"])
        time.sleep(0.75)

        self.macrorunning = False

    def MacroStopper(self):

        while self.macrorunning:

            if keyboard.is_pressed("esc"):
                self.stopmacro = True
                print("---ESC PRESSED---\n===WARNING===\n---MACRO IS STOPPING---")
                return

            time.sleep(0.1)



    def Wait(self,timecount):

        start_time = time.perf_counter()

        while time.perf_counter() - start_time < timecount:

            if self.stopmacro == True:
                return False


            time.sleep(0.1)


        return True


    def RecordCoords(self):
        self.coordslist = []
        self.coordscount = 0
        while True:

            self.coordscount+=1


            wantclick = input("do you want to click?\n y | any input to cancel\n: " )
            if wantclick == "y":
                mousepos = pyautogui.position()
                #clickcheck = pyautogui.click(mousepos)

                self.coordslist.append([mousepos.x, mousepos.y])
                print(self.coordslist)
                print(f"\n coordscount = {self.coordscount}")
            else:
                print("leaving loop")
                break




        print(f"loop has been exited\nfinal coordslist is: {self.coordslist}")
