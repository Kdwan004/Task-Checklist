from subject import list_subjects
from os import system
from time import sleep


# Main UI for managing tasks --> added to main menu
def task_ui(subject_list, task_list):
    while True:
        print("EDITING TASKS\n")
        print("1. Add Task: ")
        print("2. Remove Task: ")
        print("3. View Tasks: ")

        back = str(input("\nEnter Option: "))

        if back == "--":
            break

        else:
            user_input = int(back)
            if user_input == 1:
                add_task(subject_list, task_list)
                system('clear')
            if user_input == 2:
                remove_task(subject_list, task_list)
                system('clear')
            if user_input == 3:
                view_all_tasks(subject_list, task_list)
                str(input("\nPress any key to exit"))
                system('clear')

            

# View all tasks with numeric point values
def view_all_tasks(subject_list, task_list):
    for i, subject in enumerate(subject_list, start=1):
        print(f"{i}. {subject}")
        if task_list[i-1]:  # Check if there are tasks in the current subject's list
            for j, task in enumerate(task_list[i-1], start=1):
                print(f"    {j}. {task}")
        else:
            print("")
            print("    EMPTY")

        
# View subject specific tasks with numeric point values
def view_task(subject_list, task_list, index):

    print(subject_list[index-1])
    for i, tasks in enumerate(task_list[index-1], start=1):
        print(f"    {i}.{tasks}")
    

def add_task(subject_list, task_list):
    # Loop to allow user to return to subject selection and add tasks for another subject
    while True:
        system('clear')
        print("ADD TASK\n")

        view_all_tasks(subject_list, task_list)
        
        back = str(input("\nEnter Subject: "))

        if back == "--":
            return task_list
        
        # If selected subject index is in the list of subjects
        try:
            subject_index = int(back)

            if 0 < subject_index <= len(subject_list):
                while True:
                    try:
                        task = str(input("Enter Task: "))
                    except ValueError:
                        print("ERROR: Invalid Value")
                        continue
                    if task == "--":
                        return task_list

                    else:
                        task_list[subject_index-1].append(f"[ ]{task}")
                        view_task(subject_list, task_list, subject_index-1)
                        continue
        except ValueError:
            print("ERROR:") 
            continue
def remove_task(subject_list, task_list):
    while True:
        system('clear')
        print("REMOVE TASK\n")
        view_all_tasks(subject_list, task_list)
        back = str(input("\nSelect Subject: "))
        if back == "--":
            return task_list
        
        # If selected subject index is in the list of subjects
        subject_index = int(back)
        if 0 < subject_index <= len(subject_list):
            view_task(subject_list, task_list, subject_index)
            while True:
                task_input = str(input("Enter Task: "))
                if task_input == "--":
                    return task_list

                else:
                    task = int(task_input)
                    popped = task_list[subject_index-1].pop(task-1)
                    view_task(subject_list, task_list, subject_index-1)
                    continue
        
        else:
            print("ERROR: Index out of range")

def check_task(subject_list, task_list):
    if len(subject_list) == 0:
        print("You have no subjects to choose from")
        return None
    
    while True:
        list_subjects(subject_list)

        back = str(input("\Select Subject: "))
        if back == '--':
            return None
        
        else:
            # Loop to allow user to select multiple tasks to check
            while True:
                system('clear')
                # Conver back value to subject for subject index
                # List all tasks for the selected subject
                subject = int(back)
                view_task(subject_list, task_list, subject)
                user_input = str(input("\nEnter Task: "))
                if user_input == '--':
                    return task_list
                
                else:
                    task = int(user_input)

                    # Convert task string into array of characters
                    char_split = list(task_list[subject-1][task-1])

                    # Check if task has already been checked
                    if char_split[1] == 'x':
                        char_split[1] = ' '
                        modified_task = "".join(char_split)
                        task_list[subject-1][task-1] = modified_task
                        continue

                    if char_split[1] == ' ':
                        char_split[1] = 'x'
                        modified_task = "".join(char_split)
                        task_list[subject-1][task-1] = modified_task
                        continue
                
                



# Test case

subject_list = ['Maths', 'English', 'Biology']
task_list = [[],[],['[] Test']]

# task_list = [[''],['','',''],['', '']]


# add_task(subject_list, task_list)
# add_task(subject_list, task_list)
view_all_tasks(subject_list, task_list)

# add_task(subject_list, task_list)
# remove_task(subject_list, task_list)
# view_all_tasks(subject_list, task_list)
# view_task(subject_list, task_list, 3)

