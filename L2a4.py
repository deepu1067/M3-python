import os

def shutdown_computer(option):
    if option == "yes":
        print("Shutting down the computer...")
        os.system("shutdown /s /t 30")

    elif option == "no":
        print("Shutdown cancelled.")

    else:
        print("Invalid option!")


# Function call
shutdown_computer("no")