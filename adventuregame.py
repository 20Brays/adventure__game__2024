import time
#-------------------------------------------------------------
def intro():
    print("DROID 147 LANDING successful")
    time.sleep(2)
    print("ERROR 726")
    time.sleep(2)
    print("ERROR 869")
    time.sleep(0.2)
    print("LIVE VIDEO FEED FAILURE")
    time.sleep(0.2)
    print("LIVE AUDIO FEED FAILURE")
    time.sleep(2)
    print("REBOOTING...")
    time.sleep(4)
    print("ERRORS UNRESOLVED")
    time.sleep(1)
    print("Try other communication methods")
    time.sleep(1)
#-------------------------------------------------------------
def choose_method():
    method = ""
    while method not in ["1", "2", "3"]:
        method = input("Enter 1 to perform a LIDAR scan, 2 to try communicate with the onboard AI, or 3 to connect to an INFARED camera feed: ")
    return method
#-------------------------------------------------------------
def method_1():
    print("You try performing a LIDAR scan..")
    time.sleep(2)
    print("The LIDAR scanner has failed ")
#------------------------------------------------------------
def lidar_option():
    option = ""
    while option not in ["1", "2"]:
        option = input("Enter 1 to try debug the LIDAR scanner or enter 2 to go back")
    return option
#-------------------------------------------------------------
def lidar_option_yes():
    print("")
#-------------------------------------------------------------
def method_2():
    print("Congratulations! Your attempt to communicate with the onboard AI has been successful.")
    time.sleep(2)
    print("Hello, I am the AI system of DROID 147")
    time.sleep(2)
    print("I have access to the camera systems, do you wish for me to describe my surroundings?")
#-------------------------------------------------------------
def method_3():
    print("You confidently try using the droid's INFARED camera feed to resolve the issue.")
    time.sleep(2)
    print("The INFARED camera has been disabled due to damage")
    time.sleep(2)
    print("You lose")
    # End program
#-------------------------------------------------------------
def describe_surroundings():
    surroundings = ""
    while surroundings not in ["Y", "N"]:
        surroundings = input("Choose 'Y' for yes and 'N' for no: ")
    return surroundings
#-------------------------------------------------------------
def surroundings_yes():
    print("I am currently confined within the landing capsule, my metal frame squeezed tightly into an uncomfortable angle due to the less-than-optimal landing.")
    time.sleep(2)
    print("As your droid finds itself trapped within the confines of the landing capsule, it's damaged systems limiting your options, you contemplate your next move.")
    time.sleep(2)
    print("The situation is dire, but you know that every decision counts in the harsh expanse of space.")
#-------------------------------------------------------------    
def stuck_droid():
    stuck_droid_choice = ""
    while stuck_droid_choice not in ["1", "2"]:
        stuck_droid_choice = input("Enter 1 to open the module latch and release the droid robot. or enter 2 to check the exterior cameras for possible hazards ")   
#-------------------------------------------------------------   
def stuck_droid_1():
    print("")
    #incomplete
#-------------------------------------------------------------
def stuck_droid_2():
    print("Blue flames flicker from around the modules elongated tear shaped scar engraved deeply into the terrain.")
    time.sleep(2)
    print("The scar spans 300 metres ripping through a mess of wild alien tress and into the earth.")
    time.sleep(2)
    print("The module is covered in mud and clumps of shredded foliage, sparks fly and flicker from the ship a broken ")
#-------------------------------------------------------------
def surroundings_no():
    print("Okay, how can I help you?")
#-------------------------------------------------------------
def ai_help():
    help_choice = ""
    while help_choice not in ["1", "2", "3"]:
        help_choice = input("Enter 1 to let me tell you a joke, enter 2 to add 2 numbers together, and enter 3 to go back: ")
    return help_choice
#-------------------------------------------------------------
def ai_option_1():
    print("What do you call an italian with a toe consisting of (C 5 h 8)n?")
    time.sleep(2)
    print("Roberto! *wo-ch* Get back shadrack! Its all inside your mind!")
    time.sleep(2)
    ai_help()
#-------------------------------------------------------------
def ai_option_2():
    numOne = input("Enter the first number you would like to input.")
    time.sleep(2)
    numTwo = input("Enter the second number you would like to input")
    print(numOne + numTwo)
    ai_help()
#-------------------------------------------------------------
def ai_option_3():
    print("going backwards")
    describe_surroundings()
#-------------------------------------------------------------
def main():
    intro()
    method_choice = choose_method()
    if method_choice == "1":
        method_1()
    elif method_choice == "2":
        method_2()
        describe_surroundings()
        ai_choice = ai_help()
        if ai_choice == "1":
            ai_option_1()
        elif ai_choice == "2":
            ai_option_2()
        elif ai_choice == "3":
            ai_option_3()
        else:
            method_3()

    if method_choice == "3" and ai_choice != "3":
        surroundings_choice = describe_surroundings()
        if surroundings_choice == "Y":
            surroundings_yes()
        else:
            surroundings_no()
#-------------------------------------------------------------
if __name__ == "__main__":
    main()
