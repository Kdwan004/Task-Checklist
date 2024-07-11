from subject import list_subjects

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
                    break
                else:
                    task_list[subject_index-1].append(task)
                    continue


subject_list = ['Maths', 'English', 'Biology']
task_list = [[],[],[]]

add_task(subject_list, task_list)

