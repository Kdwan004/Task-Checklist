'''

Write Testcases for user input and list input

'''

def list_subjects(list):
    # If the list is not empty, list all subjects in the list
    if len(list) > 0:
        for index, subjects in enumerate(list, start=1):
            print(f"{index}. {subjects}")
            print("")
        
    # Otherwise print null [To be changed later]
    if len(list) > 0:
       print("\n Null \n")

def add_subjects(list):

    # While loop to give user to add multiple subjects
    # Also allows user to exit function without being forced to exit the program
    while True:
        # 1. User enters subject
        subject = str(input("Enter Subject: ")) # User will enter a subject
        if subject.lower == "back":
            return list
        
        # 2. User Will confirm subject
        decision = str(input(f"Are you sure you want to add '{subject}' to the list?")) 

        # 3a. If user says yes, then add the subject to the list and return the new list value
        if decision.lower() == "yes": 
            list.append(subject)
            return list
        
        # 3b. If user says no, then the user is prompted back to step 1
        elif decision.lower() == "no":
            continue
        
        # 4. If user does not wish to continue, return list value
        elif decision.lower() == "back":
            return list


