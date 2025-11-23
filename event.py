#Event Conflict Checker
#A CRUD application to manage events and check for conflicts in events

from datetime import datetime
schedule=[
    {"name":"CSE CLASS","date":"21-11-2025", "start": "09:00", "end": "10:30"},
    {"name":"PHYSICS CLASS","date":"21-11-2025", "start": "12:00", "end": "13:30"},
]
def time(tstr):
     t=datetime.strptime(tstr, "%H:%M")
     return t.hour*60 + t.minute

def view_schedule():
    """Display all events in a formatted way"""
    print("\n---ALL EVENTS ---")
    print("\nschedule:")
    for event in schedule:
        print(f"{event['name']}-{event['date']} from {event['start']} to {event['end']}")
    print()
def add_event():
    """add new event to the list"""
    print("\n--- ADD NEW EVENT ---")
    name = input("Enter name of the event: ")
    date = input("Enter event date(DD-MM-YYYY): ")
    start_time=input("Enter start time (HH:MM): ")
    end_time=input("Enter end time (HH:MM): ")

    new_start = time(start_time)
    new_end = time(end_time)

    for event in schedule:
        if event['date'] == date:
            start = time(event['start'])
            end = time(event['end'])
            if new_start < end and new_end > start:
                print(f" CONFLICT DETECTED!!! \nConflict Detected with: {event['name']}")
                return
    schedule.append({
         "name": name,
         "date": date,
         "sart": start_time,
         "end": end_time,
    })
    print("Event added successfully!")

def delete_event():
    """Delete an event from the list"""
    print("\n---DELETE EVENT---")
    name = input("Enter the name of the event to delete: ")
    for i, event in enumerate(schedule):
        if event['name']==name:
            schedule.pop(i)
            print(f"Event'{name}' deleted successfully!")
    print("event not found")

def update_event():
    """Update an existing event"""
    print("\n---UPDATE EVENT---")
    name = input("Enter the name of the event to update: ")
    event_update = None
    for event in schedule:
        if event['name'] == name:
            event_to_update = event
            break
    if event_update is None:
        print("Event not found!")
        return
    new_name=input(f"Enter new name(or press enter to keep '{event_update['name']}'):")or event_update['name']
    date = input(f"Enter new date(DD-MM-YYYY)(or press enter to keep '{event_update['date']}'):") or event_update['date']
    start_time= input(f"Enter start time (HH:MM) (or press enter to keep '{event_update['start']}':") or event_update['start']
    end_time=input(f"Enter end time (HH:MM) (or press enter to keep '{event_update['end']}':") or event_update['end']

    new_start = time(start_time)
    new_end = time(end_time)

    if new_start >= new_end:
        print("Error: End time must be after start time!")
        return

    for event in schedule:
        if event['name'] != name and event['date'] == date:
            start = time(event['start'])
            end = time(event['end'])
            if new_start < end and new_end > start:
                print(f"Conflict Detected with: {event['name']}")
                return
    event_update['name'] = new_name
    event_update['date'] = date
    event_update['start'] = start_time
    event_update['end'] = end_time
    print("Event updated successfully!")

def main():
    while True:
        """Display the main menu options"""
        print("\n" + "="*50)
        print("         EVENT CONFLICT CHECKER")
        print("="*50)
        print("1. View All Events")
        print("2. Add New Event")
        print("3. Delete Event")
        print("4. Update Event")
        print("5. Exit")
        choice = input("Enter your choice (1-5):")
        print("="*50)
        if choice == '1':
            schedule()
        elif choice == '2':
            add_event()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            update_event()
        elif choice == '5':
            print("Exiting....")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")
if __name__ == '__main__':
    main()
