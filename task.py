from subject import list_subjects

def view_all_tasks(subject_list, task_list):
    for i, subjects in enumerate(subject_list, start=1):
        print(f"{i}. {subjects}")
        for j, tasks in enumerate(task_list[i-1], start=1):
            print(f"    {j}. {tasks}")
        
        print("")

def view_task(subject_list, task_list, index):
    print(subject_list[index-1])
    for i, tasks in enumerate(task_list[index-1], start=1):
        print(f"    {i}. {tasks}")
    

def add_task(subject_list, task_list):
    # Loop to allow user to return to subject selection and add tasks for another subject
    while True:
        list_subjects(subject_list)
        back = str(input("\nEnter Subject: "))
        if back == "--":
            return task_list
        
        # If selected subject index is in the list of subjects
        subject_index = int(back)
        if 0 < subject_index <= len(subject_list):
            while True:
                task = str(input("Enter Task: "))
                if task == "--":
                    return subject_list, task_list
                
                else:
                    task_list[subject_index-1].append(task)
                    continue

def remove_task(subject_list, task_list):
    while True:
        list_subjects(subject_list)
        back = str(input("\nEnter Subject: "))
        if back == "--":
            return task_list
        
        # If selected subject index is in the list of subjects
        subject_index = int(back)
        if 0 < subject_index <= len(subject_list):
            view_task(subject_list, task_list, subject_index)
            while True:
                task_input = str(input("Enter Task: "))
                if task_input == "--":
                    return subject_list, task_list

                else:
                    task = int(task_input)
                    popped = task_list[subject_index-1].pop(task-1)
                    print(f"'{popped}' was removed from {subject_list[subject_index-1]}")
                    continue


# Test case

# subject_list = ['Maths', 'English', 'Biology']
# task_list = [['weofnowe', 'dwedwef'],[],['weofnowe', 'dwedwef']]

# add_task(subject_list, task_list)
# view_all_tasks(subject_list, task_list)

# add_task(subject_list, task_list)
# remove_task(subject_list, task_list)
# view_all_tasks(subject_list, task_list)
# view_task(subject_list, task_list, 3)

