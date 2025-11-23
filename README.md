# VITyarthiProject
## #### EVENT CONFLICT CHECKER ####
The Event Conflict Checker is a simple Python CRUD (Create, Read, Update, Delete) application designed to help users manage their schedules by adding, updating, and deleting events. The core feature of this tool is its ability to detect scheduling conflicts between events made in advance and present, ensuring that no two events are overlaping in time on the same date. This makes it ideal for students, professionals, or anyone who needs to keep track of their daily activities efficiently.
<h2>
**FEATURES**
</h2>

**Add Events**: Users can add new events by specifying the event name, date, start time, and end time.

**Delete Events**: User can remove existing events from the schedule by name.

**Update Events**: Modify the details of an existing event, including its name, date, and time slots.

**Conflict Detection**: Automatically checks for overlapping events when adding or updating, and alerts the user if a conflict is detected.

**Interactive CLI**: Simple menu-driven interface for easy navigation and management of events.

**Console Output**: Displays the current schedule and relevant messages directly in the terminal.

## **TOOLS USED**


 **Python 3.13**: The entire application is written using only Python including usage of built-in libraries for date and time handling.

 **datetime** module:used for comparing time strings

 **Command-Line** Interface (CLI): No framework used, the program runs entirely in the terminal.


## **STEPS TO INSTALL & RUN THE PROJECT**
1. **INSTALL PYTHON**
    make sure that you have installed python3.13 in your system.You can download it from python.org .
2. **PIP INSTALL** 
    intall datetime module in youre system through terminal using the command pip install datetime 
3. **CLONE THE REPOSITORY** 
    clone the project files to your local machine.
4. **RUN THE PROJECT**
    open terminal and go in the directory where your project is saved  and execute the command python event_conflict_checker.py

## **INSTRUCTIONS FOR TESTING **

**View Events:**
Select option 1 to view current schedule.

**Add Events:**
Select option 2 to add an event. Enter the event details and observe if the system detects any conflicts with existing events.

**Delete Events:**
Select option 3 and enter the name of the event to remove it from the schedule.

**Update Events:**
Select option 4 to update an event. Change its details and verify that the system checks for conflicts before updating.

**Exit:**
Select option 5 to exit the application.

