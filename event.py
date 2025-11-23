# Event Conflict Checker
# A simple CRUD application to manage events and check for scheduling conflicts

from datetime import datetime

current_schedule = [
    {"name": "Project Standup", "date": "2025-11-21", "start": "09:00", "end": "10:30"},
    {"name": "Class Lecture", "date": "2025-11-21", "start": "14:00", "end": "16:00"},
]
def time_to_minutes(t_str):
    t = datetime.strptime(t_str, "%H:%M")
    return t.hour * 60 + t.minute

def show_schedule():
     """Display all events in a formatted way"""
     print("\n--- ALL EVENTS ---")
     print("\nCurrent Schedule:")
     for event in current_schedule:
        print(f"{event['name']} - {event['date']} from {event['start']} to {event['end']}")
     print()

def add_event():
    """Add a new event to the list"""
    print("\n--- ADD NEW EVENT ---")
    name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")

    new_start = time_to_minutes(start_time)
    new_end = time_to_minutes(end_time)

    if new_start >= new_end:
        print("Error: End time must be after start time!")
        return

    for event in current_schedule:
        if event['date'] == date:
            start = time_to_minutes(event['start'])
            end = time_to_minutes(event['end'])
            if new_start < end and new_end > start:
                print(f" CONFLICT DETECTED! \nConflict Detected with: {event['name']}")
                return

    current_schedule.append({
        "name": name,
        "date": date,
        "start": start_time,
        "end": end_time
    })
    print("Event added successfully!")

def delete_event():
    """Delete an event from the list"""
    print("\n--- DELETE EVENT ---")
    name = input("Enter the name of the event to delete: ")
    for i, event in enumerate(current_schedule):
        if event['name'] == name:
            current_schedule.pop(i)
            print(f"Event '{name}' deleted successfully!")
            return
    print("Event not found!")

def update_event():
    """Update an existing event"""
    print("\n--- UPDATE EVENT ---")
    name = input("Enter the name of the event to update: ")
    event_to_update = None
    for event in current_schedule:
        if event['name'] == name:
            event_to_update = event
            break

    if event_to_update is None:
        print("Event not found!")
        return

    new_name = input(f"Enter new name (or press Enter to keep '{event_to_update['name']}'): ") or event_to_update['name']
    date = input(f"Enter new date (YYYY-MM-DD) (or press Enter to keep '{event_to_update['date']}'): ") or event_to_update['date']
    start_time = input(f"Enter new start time (HH:MM) (or press Enter to keep '{event_to_update['start']}'): ") or event_to_update['start']
    end_time = input(f"Enter new end time (HH:MM) (or press Enter to keep '{event_to_update['end']}'): ") or event_to_update['end']

    new_start = time_to_minutes(start_time)
    new_end = time_to_minutes(end_time)

    if new_start >= new_end:
        print("Error: End time must be after start time!")
        return

    for event in current_schedule:
        if event['name'] != name and event['date'] == date:
            start = time_to_minutes(event['start'])
            end = time_to_minutes(event['end'])
            if new_start < end and new_end > start:
                print(f"Conflict Detected with: {event['name']}")
                return

    event_to_update['name'] = new_name
    event_to_update['date'] = date
    event_to_update['start'] = start_time
    event_to_update['end'] = end_time
    print("Event updated successfully!")

def main():
    while True:
        """Display the main menu options"""
        print("\n" + "="*50)
        print("        EVENT CONFLICT CHECKER")
        print("="*50)
        print("1. View All Events")
        print("2. Add New Event")
        print("3. Delete Event")
        print("4. Update Event")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        print("="*50)
        if choice == '1':
            show_schedule()
        elif choice == '2':
            add_event()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            update_event()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

if __name__ == '__main__':
    main()

