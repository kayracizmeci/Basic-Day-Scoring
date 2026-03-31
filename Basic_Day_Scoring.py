
from datetime import datetime


def get_start_day():
    return datetime.now().strftime("%a").lower()[:2]


def parse_days_input(days_text):
    return [day.strip().lower() for day in days_text.split(",") if day.strip()]


program = {
    'mo': [],  # Monday
    'tu': [],  # Tuesday
    'we': [],  # Wednesday
    'th': [],  # Thursday
    'fr': [],  # Friday
    'sa': [],  # Saturday
    'su': []   # Sunday
}



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
            program[day].append({task_name: False})

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
        continue

    elif input_task == 'bds remove task':
        task_name = input(":! remove task name: ")
        removed_count = 0

        for day_key in program:
            original_len = len(program[day_key])
            program[day_key] = [
                task for task in program[day_key]
                if not (
                    (isinstance(task, dict) and task_name in task)
                    or task == task_name
                )
            ]
            removed_count += original_len - len(program[day_key])

        if removed_count > 0:
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
        toggled_count = 0

        for task in program[start_day_key]:
            if isinstance(task, dict) and task_name in task:
                task[task_name] = not task[task_name]
                toggled_count += 1

        if toggled_count > 0:
            print(f":! task updated for today")
        else:
            print(":! task not found for today")
        continue

    else:
        print(":! invalid command")
        continue
