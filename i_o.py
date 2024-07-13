# Write subjects to file seperated by a new line
def write_subject(subject_list, task_list):
    with open('Data/subjects.txt', 'w') as file:
        for subject in subject_list:
            file.write(str(subject))
            file.write('\n')
            task_list.append([])

# Read subjects form file and return a list of the subjects
def read_subject():
    with open('Data/subjects.txt', 'r') as file:
        subjects = file.readlines()

    subject_list = [subject.strip() for subject in subjects]

    return subject_list
    
# Write tasks to file, each task is seperated by a comma
# and for each subject it is seperated by a new line
def write_task(task_list):
    with open('Data/tasks.txt', 'w') as file:
        for tasks in task_list:
            # Join tasks with commas and write the line
            file.write(','.join(map(str, tasks)) + '\n')


# Read tasks from file
def read_task():
    with open('Data/tasks.txt', 'r') as file:
        task_lines = file.readlines()

    # Create an array of lists for each line in the file
    task_list = []
    for line in task_lines:
        # Strip any trailing newlines or spaces and split by commas
        stripped_lines = line.strip()
        if stripped_lines: # If lines is not empty
            tasks = line.strip().split(',')

        # Append the list of tasks to the task_list
        else:
            tasks = []

        task_list.append(tasks)

    return task_list

# subject = ['English', 'Maths', 'Science']
# task = [["[ ]hwk 1", "[ ]hwk 2"], [], ["Hi"]]
# 
# write_subject(subject)
# write_task(task)

# task = read_task()
# print(task)


