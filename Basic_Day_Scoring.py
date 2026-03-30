


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
    input_task = input(":! ")

    if input_task == 'bds add task':
        task_name = input(":! add task name: ")
        day = input(":! add task day: ")
        if day in program:
            program[day].append(task_name)
            continue
        else:
            print(":! invalid day")
            continue

    if input_task == 'bds help':
        print('__--**Available Commands**--__')
        print('bds add task - Add a task to the program')
        print('bds help - Show the help menu')
        continue

    elif input_task == 'bds remove task':
        task_name = input(":! remove task name: ")
        day = input(":! remove task day: ")
        if day in program:
            program[day].remove(task_name)
            continue
        else:
            print(":! invalid")
            continue

    elif input_task == 'bds list task':
        print(program)
        continue

    elif input_task == 'bds quit':
        break
