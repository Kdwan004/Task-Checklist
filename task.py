from subject import list_subjects
from os import system
from time import sleep


# Main UI for managing tasks --> added to main menu
def task_ui(subject_list, task_list):
    while True:
        system('clear')
        print("EDITING TASKS\n")
        print("1. Add Task: ")
        print("2. Remove Task: ")
        print("3. View Tasks: ")

        option = str(input("\nEnter Option: "))

        if option == "--":
            break

        else:
            if option.isdigit():
                system('clear')
                user_input = int(option)

                if user_input == 1:
                    add_task(subject_list, task_list)
                    system('clear')
                if user_input == 2:
                    remove_task(subject_list, task_list)
                    system('clear')
                if user_input == 3:
                    print("VIEWING TASKS")
                    view_all_tasks(subject_list, task_list)
                    input("\nPress ENTER to return to menu...")
                    system('clear')
            else:
                print("\nERROR: Invalid Input")
                input("Press ENTER to continue...")
                continue

            

# View all tasks with numeric point values
def view_all_tasks(subject_list, task_list):
    for i, subject in enumerate(subject_list, start=1):
        print(f"{i}. {subject}")
        if task_list[i-1]:  # Check if there are tasks in the current subject's list
            for j, task in enumerate(task_list[i-1], start=1):
                print(f"    {j}. {task}")
        else:
            print("    EMPTY")


def add_task(subject_list, task_list):
    # Loop to allow user to return to subject selection and add tasks for another subject

    # If count is 0, then input subject, else keep inputting task.
    count = 0

    if len(subject_list) == 0:
        print("ADD TASK")
        print("\nERROR: Subject list is EMPTY")
        input("Press ENTER to return to menu...")
        return None
    
    while True:
        system('clear')
        print("ADD TASK\n")
        view_all_tasks(subject_list, task_list)
        if count == 0:
            select_subject = str(input("\nEnter Subject: "))
            if select_subject == "--":
                return task_list

            # Check if subject is a digit
            if select_subject.isdigit():
                subject_index = int(select_subject)
                # Ensure index given is within range
                if 0 < subject_index <= len(subject_list):
                    count = 1

                else:
                    print("\nERROR: Index out of range")
                    input("Press ENTER to continue...")
                    continue
            else:
                print("\nERROR: Invalid Input")
                input("Press ENTER to continue...")
        else:   
            # If selected subject index is in the list of subjects
            if 0 < subject_index <= len(subject_list):
                print(f"\nSelected - '{subject_list[subject_index-1]}'")
                while True:
                    task = str(input("Enter Task: "))
                    if task == "--":
                        count = 0
                        break

                    if task == "" or task == " ":
                        print("ERROR: Invalid Input")
                        input("Press ENTER to continue...")
                        continue
                    
                    else:
                        task_list[subject_index-1].append(f"[ ]{task}")
                        break
            else:
                print("ERROR: Index out of range")
# Adjust remove_task function to be similar to add_task
def remove_task(subject_list, task_list):

    count = 0

    # List index out of range error to be fixed
    # Check if subject list is empty
    if len(subject_list) == 0:
        print("REMOVE TASK")
        print("\nERROR: Subject list is EMPTY")
        input("Press ENTER to return to menu...")
        return None
    
    while True:
        system('clear')
        print("REMOVE TASK\n")
        view_all_tasks(subject_list, task_list)
        if count == 0:
            select_subject = str(input("\nEnter Subject: "))
            if select_subject == "--":
                return task_list
        
            # Check if subject is a digit
            if select_subject.isdigit():
                subject_index = int(select_subject)
                if 0 < subject_index <= len(subject_list): 
                    count = 1
                else:
                    print("ERROR: Index out of range")
                    input("Press ENTER to continue...")
                    continue

            else:
                print("\nERROR: Invalid Input")
                input("Press ENTER to continue...")
                continue
        else:
            # If selected subject index is in the list of subjects
            if 0 < subject_index <= len(subject_list):
                print(f"\nSelected: '{subject_list[subject_index-1]}'")
                while True:
                    task_input = str(input("Enter Task: "))
                    if task_input == "--":
                        count = 0
                        break

                    else:
                        if task_input.isdigit():
                            task = int(task_input)
                            task_list[subject_index-1].pop(task-1)
                            break
                        else:
                            print("ERROR: Invalid Input")
                            input("Press ENTER to continue...")
                            break
                        
            else:
                print("ERROR: Index out of range")


# Complete error handling for check function
def check_task(subject_list, task_list):

    count = 0

    # List index out of range error to be fixed
    # Check if subject list is empty
    if len(subject_list) == 0:
        print("CHECK TASK")
        print("\nERROR: Subject list is EMPTY")
        input("Press ENTER to return to menu...")
        return None
    
    while True:
        system('clear')
        print("CHECK TASK\n")
        view_all_tasks(subject_list, task_list)
        if count == 0:
            select_subject = str(input("\nEnter Subject: "))
            if select_subject == "--":
                return task_list
        
            # Check if subject is a digit
            if select_subject.isdigit():
                subject = int(select_subject)
                if 0 < subject <= len(subject_list): 
                    count = 1
                else:
                    print("\nERROR: Index out of range")
                    input("Press ENTER to continue...")
                    continue

            else:
                print("\nERROR: Invalid Input")
                input("Press ENTER to continue...")
                continue
        else:
            # If selected subject index is in the list of subjects
            if 0 < subject <= len(subject_list):
                print(f"\nSelected: '{subject_list[subject-1]}'")
                while True:
                    task_input = str(input("Enter Task: "))
                    if task_input == "--":
                        count = 0
                        break

                    else:
                        if task_input.isdigit():
                            task = int(task_input)
                            char_split = list(task_list[subject-1][task-1])
                            # Check if task has already been checked
                            if char_split[1] == 'x':
                                char_split[1] = ' '
                                modified_task = "".join(char_split)
                                task_list[subject-1][task-1] = modified_task
                                break                        
                            if char_split[1] == ' ':
                                char_split[1] = 'x'
                                modified_task = "".join(char_split)
                                task_list[subject-1][task-1] = modified_task
                                break
                        
            else:
                print("ERROR: Index out of range")

subject_list = ['History']
task_list = [['[ ]Hwk 1', '[ ]Hwk 2', '[ ]Hwk 3']]

#task_list = [['Term Paper']]


# add_task(subject_list, task_list)
# add_task(subject_list, task_list)
# view_all_tasks(subject_list, task_list)

# add_task(subject_list, task_list)
# remove_task(subject_list, task_list)
# view_all_tasks(subject_list, task_list)
# view_task(subject_list, task_list, 1)
# check_task(subject_list, task_list)

