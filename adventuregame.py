import time

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

def choose_method():
    method = ""
    while method not in ["1", "2", "3"]:
        method = input("Enter 1 to perform a LIDAR scan, 2 to try communicate with the onboard AI, or 3 to connect to an INFARED camera feed.")
    return method

def method_1():
    print("You try performing a LIDAR scan..")
    time.sleep(2)
    print("The LIDAR system is not working.")
    #ask if want to debug if yes it works if no fails
def method_2():
    print("Congartulations! your attempt to communicate with the onboard AI has been successful.")
    time.sleep(2)
    print("Hello, I am the AI system of DROID 147")
    time.sleep(2)
    print("I have access to the camera systems, do you wish for me to describe my surroundings?")

def describe_surroundings():
    surroundings = ""
    while surroundings not in ["Y", "N"]:
        surroundings = input("Choose 'Y' for yes and 'N' for no")


def surroundings_yes():
    print("I am currently confined within the landing capsule, my metal frame squeezed tightly into an uncomfortable angle due to the less-than-optimal landing.")
    time.sleep(2)
    #add stuff


def surroundings_no():
    print("okay how can i help you?")

def ai_help():
    help = ""
    while help not in ["1", "2", "3"]
    help = input("Enter 1 to let me tell you a joke, enter 2 to add 2 numbers together, and enter 3 to go back")


    """
    boat_choice = ""
    while boat_choice != "1" and boat_choice != "2":
        boat_choice = input("Enter 1 to take the boat or 2 to continue on foot: ")

    if boat_choice == "1":
        print("You decide to take the boat.")
        time.sleep(2)
        print("The boat leads you to a hidden chamber with a magical artifact.")
        time.sleep(2)
        print("Congratulations! You found the legendary artifact! You win!")
    else:
        print("You decide to continue on foot.")
        time.sleep(2)
        print("You slip on a wet rock and fall into the lake.")
        time.sleep(2)
        print("In the chaos, you lose your way and find yourself back at the entrance.")
        time.sleep(2)
        print("You decide to leave the cave.")
        time.sleep(2)
        print("Game Over.")
        """
def method_3():
    print("You confidently try using the droids INFARED camera feed to resolve the issue.")
    time.sleep(2)
    print("The INFARED camera has been disabled due to damaged")
    time.sleep(2)
    print("you lose")
    #end program

  
def main():
    intro()
    method_choice = choose_method()
    if method_choice == "1":
        method_1()
    elif method_choice == "2":
        method_2()
    else:
        method_3()

    method_2()
    surroundings_choice = describe_surroundings()
    if surroundings_choice == "Y":
        surroundings_1()
    else:
        surroundings_2()

if __name__ == "__main__":
    main()

   
