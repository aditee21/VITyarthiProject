# VITyarthiProject
## **EVENT CONFLICT CHECKER**

The Event Conflict Checker is a straightforward Python CRUD (Create, Read, Update, Delete) application ,ade to help users manage their schedules by adding, updating, and deleting events. The core features of this tool is its ability to detect scheduling conflicts between future and present events, ensuring that no two events overlap at the same time . This makes it ideal for students, professionals, or anyone who needs to keep track of their daily activities efficiently.

## ** FEATURES**

Add Events: User can add new events by specifying the event name, date, start time, and end time.

Delete Events: User can remove existing events from the schedule by name.

Update Events: Modify the details of an existing event, including its name, date, and time slots.

Conflict Detection: Aoutomatically checks for overlapping events when adding or updating, and alerts the user if a conflict is detected.

Interactive CLI: Simple menu-driven interface for easy navigation and management of events.

Console Output: Displays the current schedule and alerts the user if a conflict occurs.

**## TOOLS USED**

Python 3.13: The entire application is written using only Python including usage of built-in libraries for date and time handling.

datetime module: used for comparing time strings

command-line Interface (CLI): No framework used, the program runs entirely in the terminal.

**## STEPS TO INSTALL & RUN THE PROJECT**
1.  **INSTALL PYTHON**
    make sure that you have installed python3.13 in your system.You can download it from python.org .
2. **PIP INSTALL**
    install datetime module in your system through terminal using the command pip install datetime.
3. **CLONE THE REPOSITORY**
    clone the project files to your local machine.
4. **RUN THE PROJECT**
    open terminal and go in the directory where your project is saved  and execute the command python event_conflict_checker.py .


## **INSTRUCTIONS FOR TESTING **

**View Events:**
Select option 1 to view current schedule.


<img width="940" height="538" alt="image" src="https://github.com/user-attachments/assets/0522fab3-ab4b-4176-b643-c293d5d764d9" />


**Add Events:**
Select option 2 to add an event. Enter the event details and observe if the system detects any conflicts with existing events.

<img width="940" height="599" alt="image" src="https://github.com/user-attachments/assets/fe787623-9da7-435f-9a71-451ad68eb3c0" />


**Delete Events:**
Select option 3 and enter the name of the event to remove it from the schedule.

<img width="940" height="571" alt="image" src="https://github.com/user-attachments/assets/38159594-a800-4a7f-a03f-3f02de77dfb7" />

**Update Events:**
Select option 4 to update an event. Change its details and verify that the system checks for conflicts before updating.

<img width="940" height="419" alt="image" src="https://github.com/user-attachments/assets/9eacfb1d-7451-46ae-9208-85768c111ce5" />

**Exit:**
Select option 5 to exit the application.

<img width="940" height="381" alt="image" src="https://github.com/user-attachments/assets/b940004b-e466-45c6-bc73-44b20d4b291f" />

