
from datetime import datetime
import json


def get_start_day():
    return datetime.now().strftime("%a").lower()[:2] # Gets the current day of the week


def parse_days_input(days_text):
    return [day.strip().lower() for day in days_text.split(",") if day.strip()] # Converts the day inputs to a list of days


save_file_name = "bds_save.json"


def empty_program():
    return {
        "score": 0,
        "days": {
            'mo': {},  # Monday
            'tu': {},  # Tuesday
            'we': {},  # Wednesday
            'th': {},  # Thursday
            'fr': {},  # Friday
            'sa': {},  # Saturday
            'su': {}   # Sunday
        }
    }

days_of_the_week = ("mo", "tu", "we", "th", "fr", "sa", "su")


def save_program(program_data): # Overwrites the save file with the new data
    with open(save_file_name, "w", encoding="utf-8") as file:
        json.dump(program_data, file, indent=2)


def normalize_day_tasks(day_data):
    if isinstance(day_data, dict): # Controls the data
        return {
            str(task): bool(done)
            for task, done in day_data.items()
            if isinstance(task, str)
        }
    return {}


def load_program():
    default_data = empty_program()

    # Controls
    try:
        with open(save_file_name, "r", encoding="utf-8") as file:
            loaded = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        save_program(default_data)
        return default_data

    if not isinstance(loaded, dict):
        save_program(default_data)
        return default_data

    if "score" not in loaded or "days" not in loaded:
        save_program(default_data)
        return default_data

    if not isinstance(loaded["days"], dict):
        save_program(default_data)
        return default_data

    try:
        score_value = int(loaded["score"])
    except (TypeError, ValueError):
        score_value = 0

    normalized = {
        "score": score_value,
        "days": {
            day: normalize_day_tasks(loaded["days"].get(day, {}))
            for day in days_of_the_week
        }
    }
    save_program(normalized)
    return normalized


program = load_program()




# Main Loop
while True:
    start_day_key = get_start_day()
    days = program["days"]

    input_task = input(":! ")
    print("type 'bds help' for information")


    if input_task == 'bds add task':
        task_name = input(":! add task name: ")
        days_text = input(":! add task day(s) (ex: mo,tu,we): ")
        selected_days = parse_days_input(days_text)

        invalid_days = [day for day in selected_days if day not in days]
        if not selected_days:
            print(":! no day entered")
            continue
        if invalid_days:
            print(f":! invalid day key(s): {', '.join(invalid_days)}")
            continue

        for day in selected_days:
            if task_name not in days[day]:
                days[day][task_name] = False

        save_program(program)
        print(f":! task added to {', '.join(selected_days)}")
        continue

    elif input_task == 'bds help':
        print('__--**Available Commands**--__')
        print(f":! today: {start_day_key}")
        print(f":! total score: {program['score']}")
        print('bds add task - Add a task to the program')
        print('bds check task - Toggle task for today')
        print('bds help - Show the help menu')
        print('bds status - Show total score')
        print('bds remove task - Remove a task')
        print('bds list task - List this days tasks')
        print('bds finish - Score and reset todays tasks')
        print('bds reset - Score and reset whole weeks tasks')
        print('bds quit - Quit the program')
        print('--------------------------------')
        print('days: mo, tu, we, th, fr, sa, su')
        continue

    elif input_task == 'bds remove task':
        task_name = input(":! remove task name: ")
        removed_count = 0

        for day_key in days:
            if task_name in days[day_key]:
                del days[day_key][task_name]
                removed_count += 1

        if removed_count > 0:
            save_program(program)
            print(f":! removed {removed_count} task named '{task_name}'")
        else:
            print(":! task not found")
        continue

    elif input_task == 'bds list task':
        print(days[start_day_key])


    elif input_task == 'bds status':
        print(f":! total score: {program['score']}")
        continue

    elif input_task == 'bds quit':
        break

    elif input_task == 'bds check task':
        task_name = input(":! check task name: ")
        if task_name in days[start_day_key]:
            days[start_day_key][task_name] = not days[start_day_key][task_name]
            save_program(program)
            print(f":! task updated for today")
        else:
            print(":! task not found for today")
        continue
    
    elif input_task == 'bds finish':
        day_total = 0
        for task_name, is_done in days[start_day_key].items():
            if is_done:
                program["score"] += 1
                day_total += 1
            else:
                program["score"] -= 1
                day_total -= 1
            days[start_day_key][task_name] = False

        save_program(program)
        print(f":! day score: {day_total}")
        print(f":! total score: {program['score']}")
        print(":! all todays tasks reset to false")
        continue

    elif input_task == 'bds reset':
        week_total = 0
        for day_key in days_of_the_week:
            for task_name, is_done in days[day_key].items():
                if is_done:
                    program["score"] += 1
                    week_total += 1
                else:
                    program["score"] -= 1
                    week_total -= 1
                days[day_key][task_name] = False

        save_program(program)
        continue

    else:
        print(":! invalid command")
        continue
