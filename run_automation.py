from ctypeslibrary import COCMacro
import time

while True:

    macro = COCMacro()
    macro.resolution(2560,1440)
    macro.MacroStart()

    if macro.stopmacro == True:
        break

    time.sleep(2)