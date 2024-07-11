'''

Write Testcases for user input and list input

'''

'''
USERS WILL ENTER '--' to go back.

This prevents the user from being restricted from using the word back as an item to the list

'''

def list_subjects(list):
    # If the list is not empty, list all subjects in the list
    print("")
    if len(list) > 0:
        for index, subjects in enumerate(list, start=1):
            print(f"{index}. {subjects}")
        
    # Otherwise print null [To be changed later]
    if len(list) == 0:
       print("Null")

def add_subject(list, task_list):

    # While loop to give user to add multiple subjects
    # Also allows user to exit function without being forced to exit the program
    while True:
        list_subjects(list)
        # 1. User enters subject
        subject = str(input("\nEnter Subject to be ADDED: ")) # User will enter a subject
        if subject == "--":
            return list, task_list
        
        # 2. User Will confirm subject
        decision = str(input(f"Are you sure you want to add '{subject.upper()}' to the list? ")) 

        # 3a. If user says yes, then add the subject to the list and return the new list value
        if decision.lower() == "yes" or decision.lower() == "y": 

            # Add subject to subject list
            list.append(subject)
            # For each subject, add an empty list of tasks to task_list
            task_list.append([])
            
            print(f"'{subject.upper()}' was added to the list")
            continue
        
        # 3b. If user says no, then the user is prompted back to step 1
        if decision.lower() == "no" or decision.lower() == "n":
            continue
        
        # 5. If user does not wish to continue, return list value
        if decision == "--":
            return list, task_list


def remove_subject(list):
    list_subjects(list)
    # If there are no subjects in the list, then inform the user and return the function
    if len(list) == 0:
        print("\nNo subjects in the list")
        return list
    
    # Otherwise, continue with removal process
    elif len(list) > 0:

        while True:
            # 1. User Enters subject
            subject_input = input("\nEnter Subject to be REMOVED: ")

            # Exit function
            if subject_input == "--":
                return list

            # 2. Convert input to int to reference list index values
            subject = int(subject_input)

            # 3. If a valid subject was selected
            if subject > 0:
                decision = str(input(f"Are you sure you want to remove '{list[subject - 1]}' from the list? ")) 

                # 3a. If user says yes, then add the subject to the list and return the new list value
                if decision.lower() == "yes" or decision.lower == "y": 
                    popped = list.pop(subject - 1)
                    list_subjects(list)
                    print(f"\n{popped} was removed from the list")
                    continue

                # 3b. If user says no, then the user is prompted back to step 1
                elif decision.lower() == "no" or decision.lower() == "n":
                    continue
                 
                # 4. If user does not wish to continue, return list value
                elif decision == "--":
                    return list
                
                # 5. If user inputs an invalid value, return to step 1
                else:
                    print("Please enter a valid response (yes/no/--)")
                    continue
            
            else:
                print("Please enter a valid index")
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



