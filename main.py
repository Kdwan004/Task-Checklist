from os import system

def preview():
    while True:
        print("This software is a simple terminal task manager")
        print("You will be prompted with a list of different options")
        print("To select an option, enter the number next to the option you wish to select")
        print("If you wish to backtrack, enter '--'")

        option = str(input("\nDo you wish to proceed(yes/no)? "))
        if option.lower() == 'y' or option.lower() == 'yes':
            break

        if option.lower() == 'n' or option.lower() == 'no':
            exit()

def main_menu():
    while True:
        # Display main menu
        print("1. \nCreate Subject")
        print("2. Remove Subject")
        print("3. Edit (Add/Remove)")
        print("4. Check Tasks")
        print("5. Exit\n")    

        # Input for main menu
        input = int(input("Select Option: "))   

        # Call required functions
        if 0 < input <= 5:
            if input == 1:
                pass 
            if input == 2:
                pass 
            if input == 3:
                pass 
            if input == 4:
                pass
            if input == 5:
                exit()
        
        else:
            print("Invalid Input")
            continue

def main():
    system("clear")
    preview()

if __name__ == '__main__':
    main()
