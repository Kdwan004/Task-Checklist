'''

Write Testcases for user input and list input

'''

'''
USERS WILL ENTER '--' to go back.

This prevents the user from being restricted from using the word back as an item to the list

'''
from os import system

def list_subjects(list):
    # If the list is not empty, list all subjects in the list
    print("")
    if len(list) > 0:
        for index, subjects in enumerate(list, start=1):
            print(f"{index}. {subjects}")
        
    # Otherwise print null [To be changed later]
    if len(list) == 0:
       print("EPMTY")

def add_subject(list, task_list):

    # While loop to give user to add multiple subjects
    # Also allows user to exit function without being forced to exit the program
    while True:
        system('clear')
        print("ADD SUBJECT")
        list_subjects(list)
        # 1. User enters subject
        subject = str(input("\nEnter Subject: ")) # User will enter a subject

        if subject == "--":
            return list, task_list
        
        if subject == "" or subject == " ":
            print("\nERROR: Invalid Input")
            input("Press ENTER to continue...")

        else:
            # Add subject to the list
            list.append(subject)
            # For each subject, add an empty list of tasks to task_list
            task_list.append([])
            continue

def remove_subject(list):
    # If there are no subjects in the list, then inform the user and return the function
    if len(list) == 0:
        print("REMOVE SUBJECT")
        print("\nERROR: Subject list is EMPTY")
        input("Press ENTER to return to menu...")
        return list
    
    # Otherwise, continue with removal process
    elif len(list) > 0:

        while True:
            system('clear')
            print("REMOVE SUBJECT")
            list_subjects(list)
            # 1. User Enters subject

            select_subject = input("\nEnter Subject: ")

            # Exit function
            if select_subject == "--":
                return list

            # 2. Convert input to int to reference list index values
            # Check subject if it is a digit
            if select_subject.isdigit():
                subject = int(select_subject)
            else:
                print("\nERROR: Invalid Input")
                input("Press ENTER to continue... ")
                continue

            # 3. If a valid subject was selected
            if 0 < subject <= len(list):
                while True:
                    decision = str(input(f"Are you sure you want to remove '{list[subject - 1]}' from the list? ")) 
    
                    # 3a. If user says yes, then add the subject to the list and return the new list value
                    if decision.lower() == "yes" or decision.lower == "y": 
                        popped = list.pop(subject - 1)
                        list_subjects(list)
                        print(f"\n{popped} was removed from the list")
                        break
                    
                    # 3b. If user says no, then the user is prompted back to step 1
                    elif decision.lower() == "no" or decision.lower() == "n":
                        break
                    
                    # 4. If user does not wish to continue, return list value
                    elif decision == "--":
                        return list
                    
                    # 5. If user inputs an invalid value, return to step 1
                    else:
                        print("\nPlease enter a valid response (yes/no/--)")
                        continue
                    
            else:
                print("ERROR: Index out of range")
                continue

                



# For testing


# task_list = [['Q1'], ['Q2'], ['Q3']]
#task_list = []
#list = []
# list1 = ['a', 'b', 'c']
# list_subjects(list)
# list_subjects(list1)
# 
#add_subject(list, task_list)
# add_subject(list1)
# 
# remove_subject(list)
# remove_subject(list1)



