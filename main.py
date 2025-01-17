from os import system
import subject
import task
from i_o import read_subject, read_task


def preview():
    while True:
        system('clear')
        print("TERMINAL TASK-CHECKLIST v 1.0.\n")
        print("This software is a simple terminal task manager")
        print("You will be prompted with a list of different options")
        print("To select an option, enter the number next to the option you wish to select")
        print("If you wish to backtrack, enter '--'")

        option = str(input("\nDo you wish to proceed(yes/no)? "))
        if option.lower() == 'y' or option.lower() == 'yes':
            break

        if option.lower() == 'n' or option.lower() == 'no':
            exit()
        
        else:
            print("\nERROR: Invalid Input")
            input("Press ENTER to continue...")
            continue

def main_menu(subject_list, task_list):

    while True:
        # Display main menu
        print("TERMINAL TASK-CHECKLIST v 1.0.\n")
        print("1. Create Subject")
        print("2. Remove Subject")
        print("3. Edit Tasks (Add/Remove)")
        print("4. Check Tasks")
        print("5. Exit\n")    

        # Input for main menu
        while True:    
            try:
                user_input = int(input("Select Option: "))
                break 
            except ValueError:
                print("\nERROR: Invalid Value\n")
                continue
        # Call required functions
        if 0 < user_input <= 5:
            system('clear')
            if user_input == 1:
                subject.add_subject(subject_list, task_list)
                system('clear')
                continue
            if user_input == 2:
                subject.remove_subject(subject_list, task_list)
                system('clear')
                continue
            if user_input == 3:
                task.task_ui(subject_list, task_list)
                system('clear')
                continue
            if user_input == 4:
                task.check_task(subject_list, task_list)
                system('clear')
                continue
            if user_input == 5:
                exit()
        
        else:
            print("Invalid Input")
            continue

def main():
    # Declare variables
    subject_list = read_subject()
    task_list = read_task()

    # Begin Process
    preview()
    system('clear')
    main_menu(subject_list, task_list)


if __name__ == '__main__':
    main()
