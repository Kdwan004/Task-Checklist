def preview():
    pass

def main_menu():
    while True:
        # Display main menu
        print("1. \nCreate Subject")
        print("2. Remove Subject")
        print("3. Edit (Add/Remove)")
        print("4. Check Tasks\n")
        print("5. Exit")    

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
    preview()


if __name__ == '__main__':
    main()
