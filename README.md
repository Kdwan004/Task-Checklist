# Task-Checklist
A second attempt at making a checklist, was too ambitous with my last
attempt and got lost on the way. My code became confusing and I became overwhelmed by what I had done. 

Project Plan: main.py <-- subject.py <-- tasks.py

Main Menu:

- Create Subject [DONE]
	- List Subjects [System] 
	- Input Subject Name [User] 
		- Confirm Subject [User]
		- Cancle Subject (Return to main menu) [User]

- Edit Subject (Add, Remove options) 
	- List Subjects (Select by index numebr) [System]
		- List Task Options [System]
			- ADD [System]
				- List tasks in subject [System]
				- Input task name [User]
				- Add task to the list [System]
				- Display updated task list [System]

				- Back (Return to main menu) [User]

			- REMOVE [System]
				- List tasks in subject [System]
				- Input task name [User]
				- Confirm 'Are you sure you want to remove 'task?''[User]
				- Remove task from list [User]
				- Display updated task list [System]
			
				- Back (Return to main menu) [User]
			
- Remove Subject [DONE]
	- List Subjects (Select by index number) [System]
		- Confirm Selected Subject 'Are you sure you want to remove 'Subject'' [User]
		- Cancle (Return to main menu) [User]

- Check/Uncheck Task
	- List Subject/Tasks Name/Index [System]
		- Select Subject & Task Index [Toggle Checkmark] [User]
		- Display updated list with checked task [System]
		- Return to main menu [System]
 
- Exit
	- Exit Program [User]
