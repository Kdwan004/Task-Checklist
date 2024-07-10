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

    print("")
        
    # Otherwise print null [To be changed later]
    if len(list) == 0:
       print("\n Null \n")

def add_subject(list):

    # While loop to give user to add multiple subjects
    # Also allows user to exit function without being forced to exit the program
    while True:
        # 1. User enters subject
        subject = str(input("Enter Subject: ")) # User will enter a subject
        if subject == "--":
            return list
        
        # 2. User Will confirm subject
        decision = str(input(f"Are you sure you want to add '{subject}' to the list? ")) 

        # 3a. If user says yes, then add the subject to the list and return the new list value
        if decision.lower() == "yes" or decision.lower == "y": 
            list.append(subject)
            print("")
            print(f"{subject} was added to the list")
            return list
        
        # 3b. If user says no, then the user is prompted back to step 1
        elif decision.lower() == "no" or decision.lower() == "n":
            continue
        
        # 4. If user does not wish to continue, return list value
        elif decision == "--":
            return list


def remove_subject(list):
    # If there are no subjects in the list, then inform the user and return the function
    if len(list) == 0:
        print("\nNo subjects to be removed")
        return list
    
    # Otherwise, continue with removal process
    elif len(list) > 0:

        while True:
            # User Enters subject
            subject_input = input("Enter Subject: ")

            # Exit function
            if subject_input == "--":
                return list

            # Convert input to int to reference list index values
            subject = int(subject_input)
            if subject > 0:
                decision = str(input(f"Are you sure you want to remove '{list[subject - 1]}' from the list? ")) 

                # 3a. If user says yes, then add the subject to the list and return the new list value
                if decision.lower() == "yes" or decision.lower == "y": 
                    popped = list.pop(subject - 1)
                    print("")
                    print(f"{popped} was removed from the list")
                    return list

                # 3b. If user says no, then the user is prompted back to step 1
                elif decision.lower() == "no" or decision.lower() == "n":
                    continue
                 
                # 4. If user does not wish to continue, return list value
                elif decision == "--":
                    return list
                
                # X. If user inputs an invalid value, return to step 1
                else:
                    print("Please enter a valid response (yes/no/--)")
                    continue

                



# For testing
list = ['a', 'b', 'c']

list_subjects(list)
remove_subject(list)

