'''

Write Testcases for user input and list input

'''

def list_subject(list):
    # If the list is not empty, list all subjects in the list
    if len(list) > 0:
        for index, subjects in enumerate(list, start=1):
            print(f"{index}. {subjects}")
            print("")
        
    # Otherwise print null [To be changed later]
    if len(list) > 0:
       print("\n Null \n")
    

    # While loop to give user to add multiple subjects
    # Also allows user to exit function without being forced to exit the program
    while True:
        # User enters subject
        subject = str(input("Enter Subject: "))
        if subject.lower == "back":
            return list
        
        # Confirmation wall
        decision = str(input(f"Are you sure you want to add '{subject}' to the list?"))
        if decision.lower() == "yes":
            list.append(subject)
            return list
        
        # If no, user is prompted to go and edit subject name
        if decision.lower() == "no":
            continue
        
        # Exit code
        if decision.lower() == "back":
            return list


