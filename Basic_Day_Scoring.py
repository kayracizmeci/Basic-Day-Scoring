
from datetime import datetime
import json


def get_start_day():
    return datetime.now().strftime("%a").lower()[:2] # Gets the current day of the week


def parse_days_input(days_text):
    return [day.strip().lower() for day in days_text.split(",") if day.strip()] # Converts the day inputs to a list of days


save_file_name = "bds_save.json"


def empty_program():
    return {
        'mo': {},  # Monday
        'tu': {},  # Tuesday
        'we': {},  # Wednesday
        'th': {},  # Thursday
        'fr': {},  # Friday
        'sa': {},  # Saturday
        'su': {}   # Sunday
    }


def save_program(program_data):
    with open(save_file_name, "w", encoding="utf-8") as file:
        json.dump(program_data, file, indent=2)


def normalize_day_tasks(day_data):
    if isinstance(day_data, dict): # Controls the data 
        return {str(task): bool(done) for task, done in day_data.items()}

    if isinstance(day_data, list):
        normalized = {}
        for item in day_data:
            if isinstance(item, dict):
                for task, done in item.items():
                    normalized[str(task)] = bool(done)
            elif isinstance(item, str):
                normalized[item] = False
        return normalized

    return {}


def load_program():
    default_data = empty_program()
    try:
        with open(save_file_name, "r", encoding="utf-8") as file:
            loaded = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        save_program(default_data)
        return default_data

    if not isinstance(loaded, dict):
        save_program(default_data)
        return default_data

    normalized = {
        day: normalize_day_tasks(loaded.get(day, {}))
        for day in default_data
    }
    save_program(normalized)
    return normalized


program = load_program()



# Main Loop
while True:
    start_day_key = get_start_day()

    input_task = input(":! ")


    if input_task == 'bds add task':
        task_name = input(":! add task name: ")
        days_text = input(":! add task day(s) (ex: mo,tu,we): ")
        days = parse_days_input(days_text)

        invalid_days = [day for day in days if day not in program]
        if not days:
            print(":! no day entered")
            continue
        if invalid_days:
            print(f":! invalid day key(s): {', '.join(invalid_days)}")
            continue

        for day in days:
            if task_name not in program[day]:
                program[day][task_name] = False

        save_program(program)
        print(f":! task added to {', '.join(days)}")
        continue

    elif input_task == 'bds help':
        print('__--**Available Commands**--__')
        print('bds add task - Add a task to the program')
        print('bds check task - Toggle task for today')
        print('bds help - Show the help menu')
        print('bds remove task - Remove a task')
        print('bds list task - List this days tasks')
        print('bds quit - Quit the program')
        print('--------------------------------')
        print('days: mo, tu, we, th, fr, sa, su')
        continue

    elif input_task == 'bds remove task':
        task_name = input(":! remove task name: ")
        removed_count = 0

        for day_key in program:
            if task_name in program[day_key]:
                del program[day_key][task_name]
                removed_count += 1

        if removed_count > 0:
            save_program(program)
            print(f":! removed {removed_count} task named '{task_name}'")
        else:
            print(":! task not found")
        continue

    elif input_task == 'bds list task':
        print(program[start_day_key])
        continue

    elif input_task == 'bds quit':
        break

    elif input_task == 'bds check task':
        task_name = input(":! check task name: ")
        if task_name in program[start_day_key]:
            program[start_day_key][task_name] = not program[start_day_key][task_name]
            save_program(program)
            print(f":! task updated for today")
        else:
            print(":! task not found for today")
        continue


    else:
        print(":! invalid command")
        continue
